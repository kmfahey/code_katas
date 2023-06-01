#!/usr/bin/python3

import math
import collections
import timeit


# Because extensibility is a goal of a different exercise, I have not
# refactored this 1st-draft code into my normal array of logical functions. See
# conflicting-objectives-efficient.py for that treatment.


# Data vector class
Word_Combination = collections.namedtuple("Word_Combination", ["combo_word", "first_word", "second_word"])


WORD_LIST_PATH = "wordlist.txt"


word_fh = open(WORD_LIST_PATH, "r")

words = [wordline.strip().lower() for wordline in word_fh]
words = list(filter(lambda word: len(word) <= 6, words))
wordlist_len_6 = list(filter(lambda word: len(word) == 6, words))
wordlist_lens_1_to_5 = list(filter(lambda word: 1 <= len(word) <= 5, words))

word_combinations = set()


def find_combining_words():

    for outer_iter_counter, result_word in enumerate(wordlist_len_6, start=1):

        left_words = list(filter(lambda left_word: result_word.startswith(left_word), wordlist_lens_1_to_5))

        for left_word in left_words:

            left_word_len = len(left_word)
            right_words = list(filter(lambda right_word: result_word.endswith(right_word), wordlist_lens_1_to_5))

            for right_word in right_words:

                # In theory this should occur at most 1 time per iteration of the enclosing loop.
                if left_word_len + len(right_word) == 6:
                    word_combinations.add(Word_Combination(result_word, left_word, right_word))

        if outer_iter_counter % 1000 == 0:

            print(f"finished {outer_iter_counter} of {len(wordlist_len_6)}")


time_elapsed = timeit.timeit(find_combining_words, number=1)

minutes_elapsed = time_elapsed // 60
seconds_elapsed = math.floor(time_elapsed % 60)
microseconds_elapsed = time_elapsed % 1 * 1000

print(f"time elapsed {minutes_elapsed:01.0f}:{seconds_elapsed:02.0f}.{microseconds_elapsed:03.0f}")


word_fh = open("word_combinations_readable.txt", "w")

for combo in sorted(word_combinations):
    word_fh.write(f"{combo.first_word} + {combo.second_word} => {combo.combo_word}\n")

print("wrote word combinations to file word_combinations_readable.txt")

