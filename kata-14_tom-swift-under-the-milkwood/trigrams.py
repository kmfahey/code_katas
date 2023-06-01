#!/usr/bin/python3

import argparse
import collections
import functools
import logging
import operator
import pickle
import random
import re
import sys
import os


# Constants
TRIGRAM_FILE = "initial_digrams_+_trigrams.dat"

TERMINAL_TOKENS = set("!.?…")

CULL_TOKENS = set("“”\"()[]_'‘’")

SINGLE_QUOTES = set("'ʼ’")


# Regular expressions, pre-compiled for efficiency
isalpha_opt_apos_re = re.compile("^[A-Za-z]+(['ʼ’]?[a-z]+)?$")

tokens_wordbound_re = re.compile("(?<=[A-Za-zÀ-ÖØ-öø-ÿ0-9'ʼ’])(?=[^A-Za-zÀ-ÖØ-öø-ÿ0-9'ʼ’])"
                                     "|"
                                 "(?<=[^A-Za-zÀ-ÖØ-öø-ÿ0-9'ʼ’])(?=[A-Za-zÀ-ÖØ-öø-ÿ0-9'ʼ’])")

tokens_diff_chars_bound_re = re.compile(r"(?<=(.))(?!\1)(?=.)")

is_punct_re = re.compile(r'^[!"#$%&\'()*+,./:;<=>?@\[\\\]^_`{|}~—‘“”…-]+$')


# Lambdas, string-testing
isalpha_w_apos = lambda strval: bool(isalpha_opt_apos_re.match(strval))

ispunct = lambda strval: bool(is_punct_re.match(strval))

begins_ends_w_sgl_qt = lambda strval: strval[0] in SINGLE_QUOTES and strval[-1] in SINGLE_QUOTES

begins_w_sgl_qt = lambda strval: strval[0] in SINGLE_QUOTES

ends_w_sgl_qt = lambda strval: strval[-1] in SINGLE_QUOTES


# Data vector class, encapsulates the 3 tiers of data structure: initial_tokens
# for the first token in a sentence, digrams for the second, and trigrams for
# the 3rd and subsequent tokens.
Algo_Output = collections.namedtuple("Algo_Output", ["initial_tokens", "digrams", "trigrams"])


def main():
    logger = set_up_logger()

    options = fetch_args()

    check_files(options.bookfiles, logger, generate_trigrams=options.generate_trigrams)

    # If the -t argument was specified, runs the combined algorithm, builds the
    # initial_tokens, digrams and trigrams data structures, and saves them to a
    # file.
    if options.generate_trigrams:
        algo_output = calc_markov_pvals(options.bookfiles, logger)

        logger.info(f"saving trigram and starting point data structures to file '{TRIGRAM_FILE}'")

        with open(TRIGRAM_FILE, "wb") as tg_fh:
            pickle.dump(algo_output, tg_fh)
    # Otherwise, loads the saved data structures from said file.
    else:
        logger.info(f"loading trigram and starting point data structures from file '{TRIGRAM_FILE}'")

        with open(TRIGRAM_FILE, "rb") as tg_fh:
            algo_output = pickle.load(tg_fh)

    # Extracts the 3 data structures from the saved object.
    initial_tokens = algo_output.initial_tokens

    digrams = algo_output.digrams

    trigrams = algo_output.trigrams

    # If the -g flag was specified, takes that number and generates that number
    # of sentences using a Markov chain algorithm.
    if options.generate_output != 0:
        for i in range(options.generate_output):
            print(generate_sentence(initial_tokens, digrams, trigrams))


# Builds, configures and returns a logger.Logger object.
def set_up_logger():
    logger = logging.getLogger(name="main")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    logger.addHandler(handler)
    return logger


# Uses the argparse module to process the commandline arguments and returns the
# retval of argparser.parse_args().
def fetch_args():
    argparser = argparse.ArgumentParser("dd_add_cereal.py")

    argparser.add_argument("-t", action="store_true", default=False, dest="generate_trigrams",
                           help="generate the trigrams data structures")

    argparser.add_argument("-g", action="store", default=0, dest="generate_output", type=int,
                           help="use a markov chain to generate a number of sentences equal to the argument")

    argparser.add_argument("bookfiles", nargs=argparse.REMAINDER, help="ebook text files to process")

    return argparser.parse_args()


# Validates the filename arguments.
def check_files(files, logger, generate_trigrams=False):
    if generate_trigrams and not len(files):
        logger.warning("-t flag supplied by no files specified on the commandline. Nothing to do.")
        exit(0)
    elif not all(file.lower().endswith(".txt") for file in files):
        nonmatching_file = next(filter(lambda file: not file.lower().endswith(".txt"), files))
        logger.error(f"Filename argument {nonmatching_file} is not a text file. "
                     "Please only specify text files as arguments.")
        exit(1)
    elif not all(os.path.exists(filename) for filename in files):
        nonexistent_file = next(filter(lambda file: not os.path.exists(file), files))
        logger.error(f"Filename argument {nonexistent_file} refers to a nonexistent file.")
        exit(1)


# Accepts a list of filenames and a logging.Logger object. Has the files loaded
# and runs the combined algorithm on them. Derives the initial_tokens, digrams
# and trigrams structures, stores them in an Algo_Output object and returns it.
def calc_markov_pvals(bookfiles, logger):
    initial_trigrams_retval = calculate_initial_and_trigrams(bookfiles, logger)

    initial_tokens = initial_trigrams_retval["initial_tokens"]

    trigrams = initial_trigrams_retval["trigrams"]

    digrams = calculate_digrams(trigrams, logger)

    return Algo_Output(initial_tokens, digrams, trigrams)


# Accepts a list of filenames and a logging.Logger object. Loads the entire
# text of each file, has the text tokenized, and derives the trigrams and
# initial_tokens structures from the lot of them. Stores both values in a 2-pair
# dict and returns them.
def calculate_initial_and_trigrams(bookfiles, logger):
    trigrams = dict()

    for index, bookfile in enumerate(bookfiles, start=1):
        logger.info(f"processing book #{index}: filename '{bookfile}'")
        with open(bookfile) as book_fh:
            booklines = list(book_fh)
        tokenization_retval = tokenize_booklines(booklines)
        tokens_list = tokenization_retval["tokens_list"]
        tokens_inc_d = tokenization_retval["tokens_inc_d"]
        update_trigrams_w_tokens_list(tokens_list, trigrams)

    counts_to_probabilities(tokens_inc_d)

    initial_tokens = prob_d_to_pval_range_table(tokens_inc_d)

    logger.info("converting trigram counts to probabilities")

    for initial_pair, succ_tokens_d in trigrams.items():
        counts_to_probabilities(succ_tokens_d)

        trigrams[initial_pair] = prob_d_to_pval_range_table(succ_tokens_d)

    return dict(initial_tokens=initial_tokens, trigrams=trigrams)


# Accepts a list of lines of text drawn from an imported text. Tokenizes the
# entire input and revises the token list. Also builds a dict where the keys are
# token in the list, and the values are the number of times each token occurs in
# the token list. Returns both these values compacted into a 2-pair dict.
def tokenize_booklines(booklines):
    tokens_inc_d = dict()
    tokens_list = list()
    for line in map(str.strip, booklines):
        line_tokens = functools.reduce(operator.concat,
                                       (tokens_wordbound_re.split(token) for token in line.split()),
                                       list())
        index = 0
        while index < len(line_tokens):
            token = line_tokens[index]
            if token.isalpha() or token.isdigit() or len(token) == 1:
                index += 1
                continue
            if ispunct(token) and len(token) > 1:
                line_tokens[index:index+1] = list(token)
            elif begins_ends_w_sgl_qt(token) and len(token) > 2:
                line_tokens[index:index+1] = [token[0], token[1:len(token)-1], token[-1]]
            elif begins_w_sgl_qt(token):
                line_tokens[index:index+1] = [token[0], token[1:]]
            elif ends_w_sgl_qt(token):
                line_tokens[index:index+1] = [token[:-1], token[-1]]
            index += 1
        tokens_list.extend(filter(lambda token: token not in CULL_TOKENS, line_tokens))
    terminal_token_indexes = [index for index, token in enumerate(tokens_list) if token in TERMINAL_TOKENS]
    initial_token_indexes = [index + 1 for index in terminal_token_indexes
                             if index + 1 < len(tokens_list) and isalpha_w_apos(tokens_list[index + 1])]
    for index in initial_token_indexes:
        token = tokens_list[index]
        if token not in tokens_inc_d:
            tokens_inc_d[token] = 1
        else:
            tokens_inc_d[token] += 1
    return dict(tokens_inc_d=tokens_inc_d, tokens_list=tokens_list)


# Accepts a list of tokens, and updates the trigrams incidence structure with
# all trigrams found in the tokens list.
def update_trigrams_w_tokens_list(tokens_list, trigrams):
    if trigrams is None:
        trigrams = dict()
    for index in range(0, len(tokens_list) - 2):
        initial_pair = tuple(tokens_list[index:index+2])
        subseq_token = tokens_list[index+2]
        if initial_pair not in trigrams:
            trigrams[initial_pair] = {subseq_token: 1}
        else:
            trigrams[initial_pair][subseq_token] = trigrams[initial_pair].get(subseq_token, 0) + 1
    return trigrams


# Accepts a dict where the values are ints that represent counts of the keys
# occurrence in a text. Sums the ints and then returns a derived dict where the
# int val has been divided by the sum val. In this way the values are now floats
# in [0,1] and can be used as p-vals for the probability that a given token
# would occur.
def counts_to_probabilities(count_d):
    total_incidence = sum(count_d.values())
    for key in count_d:
        count_d[key] /= total_incidence


# Accepts a dict where the values are float values in [0,1], and the sum of the
# values is 1. Derives a list of 3-tuples where the 3rd value is the key, and
# the 1st and 2nd values comprise a range whose difference equals the original
# p-value, and the ranges together cover the entire span between 0 and 1 such
# that the retval of a random.random() call could be used to select a random row
# from the list by placing it in one of the intervals.
def prob_d_to_pval_range_table(pval_d):
    pval_table = []

    running_max_pval = 0
    latest_max_pval = 0

    for key, key_pval in pval_d.items():
        running_max_pval = latest_max_pval
        latest_max_pval = running_max_pval + key_pval
        pval_table.append((running_max_pval, latest_max_pval, key))

    if pval_table[-1][1] != 1.0:
        pval_table[-1] = (pval_table[-1][0], 1.0, pval_table[-1][2])

    return pval_table


# Uses the keys of the trigrams structure as a source for developing a simpler
# table of digrams. The digrams structure is a dict of dicts. The keys of the
# outer dict are all tokens found at the 0 index of a key pair in the trigrams
# structure. The keys of each inner dict are all tokens found at the 1 index of
# a key pair in the trigrams structure where the outer key was at the 0 index of
# that pair. The values of the inner dict are counts of such pair.
#
# * Bug: due to how dict keys work, this count can only ever be 1. The sum of
# all counts in the trigrams value would be a better source of counts, but
# it isn't available in the finished trigram structure. If the counts were
# preserved they could be used.
#
# The digrams values are then converted to dicts of p-vals, and then to lists of
# p-val ranges, before the structure is returned.
def calculate_digrams(trigrams, logger):
    logger.info("deriving starter tokens table")

    digrams = dict()

    for key_pair in trigrams.keys():
        first_token, second_token = key_pair
        if first_token not in digrams:
            digrams[first_token] = {second_token: 1}
        elif second_token not in digrams[first_token]:
            digrams[first_token][second_token] = 1
        else:
            digrams[first_token][second_token] += 1

    for initial_token, succ_tokens_d in digrams.items():
        counts_to_probabilities(succ_tokens_d)

        digrams[initial_token] = prob_d_to_pval_range_table(succ_tokens_d)

    return digrams


# Uses the initial_tokens, digrams and trigrams data structures to generate a
# random sentence. Uses pick_at_random with initial_tokens to pick a random
# initial token and appends it to the token list.
#
# Looks up that token in digrams, uses pick_at_random with that value to pick a
# random second token, and appends it to the token list.
#
# Goes into a while loop while the last token in the token list isn't a terminal
# token, looks up the last two tokens in trigrams, uses pick_at_random with the
# value to pick a random subsequent token, and appends it to the token list.
#
# Joins the token list into a sentence, applies some regexes to correct for
# inappropriately space-padded punctuation, and returns the sentence.
#
# Bug: terminates a sentence if a token like Mr occurs because it's followed by
# a period.
def generate_sentence(initial_tokens, digrams, trigrams):
    token_list = [pick_at_random(initial_tokens)]
    token_list.append(pick_at_random(digrams[token_list[0]]))
    while token_list[-1] not in TERMINAL_TOKENS:
        token_list.append(pick_at_random(trigrams[tuple(token_list[-2:])]))
    token_string = ' '.join(token_list)
    token_string = re.subn(" ([-/]) ", lambda m: m.group(1), token_string)[0]
    token_string = re.subn(" ([!,.:;?—])", lambda m: m.group(1), token_string)[0]
    return token_string


# Accepts as an argument a list of 3-tuples, generated by
# prob_d_to_pval_range_table(). The 1st and 2nd elements of each tuple are
# floats in [0.0, 1.0], and the 3rd is a sentence token.
#
# random.random() is used to generate a random float in [0.0, 1.0). The list is
# searched until a row is found where 1st value <= random float <= 2nd value is
# true. (There will always be a row like this.) The 3rd value is returned.
def pick_at_random(pval_table):
    if len(pval_table) == 1:
        return pval_table[0][2]
    rand_pval = random.random()
    for lower_pval_thresh, upper_pval_thresh, token in pval_table:
        if lower_pval_thresh <= rand_pval <= upper_pval_thresh:
            return token


if __name__ == "__main__":
    main()

# Q&A
#
# "What do we do with punctuation? Paragraphs? Do we have to implement
# backtracking if we chose a next word that turns out to be a dead end?"
#
# I treated punctuation as a type of token in its own right. So a sentence
# terminates if a ".", "?", "!", or "…" is selected. This code works at the
# sentence level, so paragraphs are beyond its scope. The code as it stands does
# not handle dead ends; may add handling for that.
#
# It seems like I should have read the questions before writing the code, since
# they show the author of the kata had additional specification clauses that I
# didn't detect in my original readthrough of the assignment. As it stands I've
# already invested an entire day into this one and written an implementation
# whose sloc is a full 7.5 sigma above the mean linecount of my kata answers up
# to this point; I decline to put more work into it.
