#!/usr/bin/python3

import re


def main():
    # Calculate score spread case
    calculate_score_spread()

    # Calculate temperature range case
    calculate_temp_range()


# Use process_fh() and find_smallest_difference() to calculate the smallest
# score spread in football.dat
def calculate_score_spread():
    line_re = re.compile("\. ([A-Za-z_]+) .*\D(\d+)  -  (\d+)")

    with open("football.dat", "r") as ftbl_fh:
        values = process_fh(ftbl_fh, re.compile("^-+$"), re.compile("\. ([A-Za-z_]+) .*\D(\d+)  -  (\d+)"))

    best_team, smallest_diff = find_smallest_difference(values, absval=True)

    best_team = best_team.replace('_', ' ')

    print(f"The smallest difference in scores belonged to {best_team}. "
          f"It was {smallest_diff} goal{'s' if smallest_diff != 1 else ''}.")

# Use process_fh() and find_smallest_difference() to calculate the smallest
# temperature range in weather.dat
def calculate_temp_range():
    with open("weather.dat", "r") as wdat_fh:
        values = process_fh(wdat_fh, re.compile(r"^(mo\b|$)"), re.compile("^(\d+) +(\d+)\*? +(\d+)\*?\D"))

    best_day_no, smallest_diff = find_smallest_difference(values, absval=False)

    best_day_no = int(best_day_no)

    day_no_suffixes = {0:"th", 1:"st", 2:"nd", 3:"rd", 4:"th", 5:"th", 6:"th", 7:"th", 8:"th", 9:"th"}

    number_suffix = day_no_suffixes[best_day_no % 10]

    print(f"The smallest temperature range occurred on the {ord_w_suff(best_day_no)} day. "
          f"It was a range of {smallest_diff}°.")


# Attaches the correct suffix to an ordinal number and returns as a str.
def ord_w_suff(ordinal):
    day_no_suffixes = {0:"th", 1:"st", 2:"nd", 3:"rd", 4:"th", 5:"th", 6:"th", 7:"th", 8:"th", 9:"th"}
    return str(ordinal) + day_no_suffixes[ordinal % 10]


# Loads all finds from the file obj,
# Filters out lines that match bad line regex,
# Applies the get values regex to the remaining lines,
# and returns a list of the Match.groups() method retvals for each regex match.
def process_fh(datfile_fh, bad_line_re, get_values_re):
    lines = list(map(str.strip, datfile_fh))
    del lines[0]
    lines = list(filter(lambda line: not bad_line_re.search(line), lines))
    values = list(map(lambda line: get_values_re.search(line).groups(), lines))
    return values


# Iterates over the return value of a process_fh() call,
# computing abs val differences between the second and third values,
# and recording which first value is associated with the smallest difference.
# A 2-tuple of the first value # for the smallest difference, and the smallest difference, is returned.
def find_smallest_difference(values, absval=False):
    best_first_val = None
    smallest_diff = float("inf")
    for first_val, second_val, third_val in values:
        second_val = int(second_val)
        third_val = int(third_val)
        diff = abs(second_val - third_val) if absval else second_val - third_val
        if diff < smallest_diff:
            best_first_val = first_val
            smallest_diff = diff
    return best_first_val, smallest_diff


if __name__ == "__main__":
    main()


# Q & A
# 
# To what extent did the design decisions you made when writing the original
# programs make it easier or harder to factor out common code?
#
# Having already written an extraction regex in both cases was helpful. But
# process_fh() is de novo code, it's a complete rewrite. The common code of the
# previous scripts was too messy to simply extract.
#
#
# Was the way you wrote the second program influenced by writing the first?
#
# Yes. I used the first program's code as a starting point for writing the
# second.
#
#
# Is factoring out as much common code as possible always a good thing? Did the
# readability of the programs suffer because of this requirement? How about the
# maintainability?
#
# Looking back on the higher-order functions I wrote for my 3rd term project
# of my coding bootcamp, I'd say definitely not. Those were unmaintainable
# gibberish. In *this* case I don't think the readability or maintainability
# suffered.
