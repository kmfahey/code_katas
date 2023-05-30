#!/usr/bin/python3

import math
import collections
import functools
import operator
import timeit
import datetime


# Because extensibility is a goal of a different exercise, I have not
# refactored this 1st-draft code into my normal array of logical functions. See
# conflicting-objectives-efficient.py for that treatment.

Word_Combination = collections.namedtuple("Word_Combination", ["combo_word", "first_word", "second_word"])


# Load the word list, filter out words that are longer than 6 characters or
# contain nonalpha chars (e.g. an apostrophe), and then apportion words into
# different sets by word length.
WORD_LIST_PATH = "/home/kmfahey/.local/share/dict/words"

words = list(filter(lambda word: word.isalpha() & len(word) <= 6,
                    map(str.lower,
                        map(str.strip,
                            open(WORD_LIST_PATH, "r")))))

# Using a list rather than a dict so that slicing syntax can be used later.
words_by_len = [None, set(), set(), set(), set(), set(), set()]

for word in words:
    word_len = len(word)
    if not (1 <= len(word) <= 6):
        continue
    words_by_len[word_len].add(word)


# Computing the possible word combinations. Using a function so that timeit can
# measure its execution time and that time can be logged to stdout. The function
# saves its output to the global word_combinations bc the timeit framework
# discards its return value.

word_combinations = list()


def find_combining_words():

    # The length of the starting list, used to log progress
    words_len_1_to_5_count = sum(map(len, words_by_len[1:6]))

    # Iterates over words of length [1,5], with an index for a counter used to
    # log progress
    for outer_iter_counter, left_short_word in enumerate(functools.reduce(operator.or_, words_by_len[1:6]), start=1):

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
            print(f"{datetime.datetime.today().isoformat()}: "
                  f"Finished {outer_iter_counter} of {words_len_1_to_5_count} left word possibles.")


time_elapsed = timeit.timeit(find_combining_words, number=1)


# Displaying the time the combining_words() function took to execute.
minutes_elapsed = time_elapsed // 60
seconds_elapsed = math.floor(time_elapsed % 60)
microseconds_elapsed = time_elapsed % 1 * 1000

print(f"time elapsed {minutes_elapsed:01.0f}:{seconds_elapsed:02.0f}.{microseconds_elapsed:03.0f}")


# Saving the word combinations to a file.
word_fh = open("word_combinations_efficient.txt", "w")

for combo in sorted(word_combinations):
    word_fh.write(f"{combo.first_word} + {combo.second_word} => {combo.combo_word}\n")

print("wrote word combinations to file word_combinations_efficient.txt")

