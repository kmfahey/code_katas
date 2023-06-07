#!/usr/bin/python3

import re


__all__ = ["CLArg_Parser"]



# Implements a parser that can be configured with a set of flags and their data
# types. Once the schema is set up, calling parse() with an argv populates the
# state with flag settings. Thereafter the state can be queries using accessor
# methods.
class CLArg_Parser:
    __slots__ = "flags_schema", "flag_args", "nonflag_args", "nonflag_allowed"

    def __init__(self, flags_to_add=None, nonflag_allowed=True):
        self.flags_schema = dict()
        if flags_to_add is not None:
            for flag, argtype in flags_to_add.items():
                self.flags_schema[flag] = argtype
        self.flag_args = dict()
        self.nonflag_args = list()
        self.nonflag_allowed = nonflag_allowed

    # Add a flag to the schema.
    def add_flag(self, flag, argtype=bool):
        self.flags_schema[flag] = argtype

    # Get a list of all flags in the schema.
    def get_flags(self):
        return list(self.flags_schema.keys())

    # Get a list of all flags that have values set.
    def get_flags_set(self):
        return list(self.flag_args.keys())

    # Get the value of a flag.
    def get_flag_val(self, flag):
        if flag not in self.flag_args:
            return None
        else:
            return self.flag_args[flag]

    # Get the arguments that were left in argv after all the flags and their
    # args were accounted for.
    def get_nonflag_args(self):
        if not self.nonflag_allowed:
            return None
        else:
            return self.nonflag_args.copy()

    # Empty state values set by parsing so parse() can be called again.
    def reset(self):
        self.flag_args.clear()
        self.nonflag_args.clear()

    # Internal method that's used to cast a flag argument to its expected type.
    def _cast_flag_arg(self, flag, argval):
        if self.flags_schema[flag] is bool:
            if argval is None or argval is True:
                return True
            else:
                raise ValueError(f"flag -{flag} does not accept an argument")
        else:
            argtype = self.flags_schema[flag]
            try:
                value = argtype(argval)
            except ValueError:
                raise ValueError(f"flag -{flag} requires an argument of type '{argtype.__name__}'")
            return value

    # Parses an argv and sets internal state with the flags found
    def parse(self, argv):
        if not self.flag_schema:
            raise ValueError("no flags set in schema: can't parse argv")
        elif self.flag_args or self.nonflag_args:
            raise ValueError("object flags state already set; cannot parse another argv while state is set")
        arg_vector = argv.copy()
        while len(arg_vector):
            next_arg = arg_vector.pop(0)
            if re.match("^-([A-Za-z][^A-Za-z]*){2,}$", next_arg):
                self._add_flag_cluster(next_arg)
            elif re.match("^-[A-Za-z]", next_arg):
                self._add_single_flag(next_arg, arg_vector)
            else:
                if any(re.match("^-[A-Za-z]", arg) for arg in arg_vector):
                    flag_arg = next(arg for arg in arg_vector if re.match("^-[A-Za-z]", arg))
                    raise ValueError(f"nonflag argument {next_arg} encountered in argv followed by flag argument {flag_arg}")
                self._add_nonflag_arg(next_arg)

    # Adds an argument to the nonflag args list.
    def _add_nonflag_arg(self, next_arg):
        if self.nonflag_allowed:
            self.nonflag_args.append(next_arg)
        else:
            nonflag_args_expr = ", ".join(f"'{arg}'" for arg in arg_vector)
            if len(nonflag_args_expr) > 70:
                nonflag_args_expr = nonflag_args_expr[:67] + "..."
            raise ValueError(f"commandline arguments included nonflag arguments ({nonflag_args_expr}) "
                             "which is not allowed by the schema")

    # Unpack a cluster of flags (i.e. a string beginning with '-' followed by
    # more than one alphabetic flags, optionally with arguments, packed into a
    # string with no spaces) and set them in state individually.
    def _add_flag_cluster(self, arg_cluster):
        arg_cluster = arg_cluster.removeprefix("-")
        flags_w_args = re.split("(?=[A-Za-z][^A-Za-z]*)", arg_cluster)[1:]
        arg_cluster_d = {match_obj.group(1): match_obj.group(2)
                         for match_obj in map(lambda flag: re.match("^([A-Za-z])([^A-Za-z]+)?$", flag), flags_w_args)}
        recurring_flags = set(arg_cluster_d.keys()) & set(self.flag_args.keys())
        if recurring_flags:
            recurring_flag = next(iter(recurring_flags))
            raise ValueError(f"flag {recurring_flag} occurs more than once in commandline arguments")
        for flag, argval in arg_cluster_d.items():
            arg_cluster_d[flag] = self._cast_flag_arg(flag, argval)
        self.flag_args.update(arg_cluster_d)

    # Add a single flag to internal state.
    def _add_single_flag(self, arg_flag, arg_vector):
        flag = arg_flag.removeprefix("-")
        if self.flags_schema[flag] is bool:
            if len(arg_vector) and not arg_vector[0].startswith("-"):
                raise ValueError(f"flag -{flag} doesn't take an argument (was passed the argument '{arg_vector[0]}'")
            self.flag_args[flag] = True
        else:
            if not len(arg_vector):
                raise ValueError(f"flag -{flag} requires an argument (commandline args ended)")
            elif arg_vector[0].startswith("-"):
                raise ValueError(f"flag -{flag} requires an argument (next commandline element was '{arg_vector[0]}')")
            self.flag_args[flag] = self._cast_flag_arg(flag, arg_vector.pop(0))
