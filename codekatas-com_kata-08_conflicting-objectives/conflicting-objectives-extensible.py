#!/usr/bin/python3

import math
import collections
import functools
import operator
import timeit


WORD_LIST_PATH = "/home/kmfahey/.local/share/dict/words"

OUTPUT_FILE_NAME = "word_combinations_extensible.txt"

WORD_MAX_LENGTH = 6

# Word combination data vector class.
Word_Combination = collections.namedtuple("Word_Combination", ["combo_word", "first_word", "second_word"])


def main():

    # Load words
    words = load_words(WORD_LIST_PATH)

    # Sort words into sets by length
    words_by_len = words_list_to_by_len(words)

    # Run word combinations finding function in a timeit call to record its time
    # of execution (which is logged).
    word_combinations = list()
    total_seconds = timeit.timeit(lambda: word_combinations.extend(find_combining_words(words_by_len)), number=1)

    # Log time elapsed during word combinations finding algorithm execution.
    time_expr = fmt_seconds_elapsed(total_seconds)
    print("time elapsed", time_expr)

    # Save words to a file.
    write_words_to_file(word_combinations)


# Loads words list from file.
def load_words(wordpath):
    words_fh = open(WORD_LIST_PATH, "r")
    words = list(map(str.strip, words_fh))
    words = list(map(str.lower, words))
    words = list(filter(lambda word: len(word) <= WORD_MAX_LENGTH, words))
    return words


# Sorts words into a list of sets such that the index of a set is also the
# length of all words in that set.
def words_list_to_by_len(words):
    words_by_len = [None] + [set() for _ in range(0, WORD_MAX_LENGTH)]
    for word in words:
        words_by_len[len(word)].add(word)
    return words_by_len


# Formats a period of time expressed in seconds to a string showing minutes,
# seconds and microseconds.
def fmt_seconds_elapsed(total_seconds):
    return "{minutes:01.0f}:{seconds:02.0f}.{microseconds:03.0f}".format(
        minutes=total_seconds // 60, seconds=math.floor(total_seconds % 60), microseconds=total_seconds % 1 * 1000)


def find_combining_words(words_by_len):

    word_combinations = list()

    # The length of the starting list, used to log progress
    words_less_than_max_len_count = sum(map(len, words_by_len[1:WORD_MAX_LENGTH]))

    # Iterates over words of length [1,5], with an index for a counter used to
    # log progress
    for outer_iter_counter, left_short_word in enumerate(functools.reduce(operator.or_,
                                                                          words_by_len[1:WORD_MAX_LENGTH]), start=1):

        # Filters words of length 6 for words that start with left_short_word
        # and whose remainder is a real word.
        word_combinations.extend(Word_Combination(result_word,
                                                  left_short_word,
                                                  result_word.removeprefix(left_short_word))
                                 for result_word in filter(
                                     lambda result_word: result_word.startswith(left_short_word)
                                                         and result_word.removeprefix(left_short_word)
                                                             in words_by_len[6 - len(left_short_word)],
                                                           words_by_len[6]))

        # Logging progress to stdout
        if outer_iter_counter % 1000 == 0:
            print(f"finished {outer_iter_counter} of {words_less_than_max_len_count} left word possibles")

    return word_combinations


# Record word list to the output file.
def write_words_to_file(word_combinations):
    word_fh = open(OUTPUT_FILE_NAME, "w")
    for combo in sorted(word_combinations):
        word_fh.write(f"{combo.first_word} + {combo.second_word} => {combo.combo_word}\n")
    print("wrote word combinations to", OUTPUT_FILE_NAME)


if __name__ == "__main__":
    main()
