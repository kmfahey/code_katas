#!/usr/bin/python3

import sys
import collections
import timeit


def main():
    if len(sys.argv) == 1:
        wordfile = "/usr/share/dict/words"
    elif len(sys.argv) == 2:
        wordfile = sys.argv[-1]
    else:
        print("Can't process more than 1 word file as a commandline argument.")

    with open(wordfile) as word_fh:
        word_list = list(filter(str.isalpha, map(str.lower, map(str.strip, word_fh))))

    test_anagram_incidence(word_list)

    test_anagram_builder_runtime(word_list)


# Calculate the statistics of the generatable anagrams.
def test_anagram_incidence(word_list):
    anagram_dict = build_anagram_defdict(word_list)

    total_anagrams, greatest_length, longest_anagrams = calc_word_lengths(anagram_dict)

    greatest_anagram_set_popn, number_of_greatest_anagram_sets = calc_ana_sets_magnitudes(anagram_dict)

    print(f"Found {len(anagram_dict)} sets of anagrams, a total of {total_anagrams} words.",
          f"The longest anagrammable word was {greatest_length} chars long.",
          f"There were {longest_anagrams} anagram sets of that length.",
          f"The most populous anagram sets had {greatest_length} anagrams.",
          f"There were {greatest_anagram_set_popn} anagram sets of that magnitude.", sep="\n")


# Test how fast the anagram dict builder algorithm runs.
def test_anagram_builder_runtime(word_list):
    runs = 200

    print(f"Running {runs} trials to determine running time of anagram dict builder.")

    duration = timeit.timeit(lambda: build_anagram_defdict(word_list), number=runs)

    print("Execution of build_anagram_defdict function runs in", round(duration / runs, 3),
          "seconds on average across", runs, "runs.")


# Build the dict of strings of the chars of a word in order, associated with
# sets of all words that sort to that string.
def build_anagram_defdict(words):
    anagram_dict = collections.defaultdict(set)

    for word in filter(str.isalpha, map(str.lower, map(str.strip, words))):
        ordered_chars = ''.join(sorted(word))
        anagram_dict[ordered_chars].add(word)

    anagram_dict = {chars: anagrams for chars, anagrams in anagram_dict.items() if len(anagrams) > 1}

    return anagram_dict


# Computes the statistics of the longest anagrams in the anagram dict.
def calc_word_lengths(anagram_dict):
    anagram_lengths = list(map(len, anagram_dict.values()))

    total_anagrams = sum(anagram_lengths)

    greatest_length = max(anagram_lengths)

    longest_anagrams = len(list(filter(lambda chars: len(chars) == greatest_length, anagram_dict)))

    return total_anagrams, greatest_length, longest_anagrams


# Computes the statistics of the largest anagram sets in the anagram dict.
def calc_ana_sets_magnitudes(anagram_dict):
    angram_sets_lengths = list(map(len, anagram_dict.values()))

    greatest_anagram_set_popn = max(angram_sets_lengths)

    number_of_greatest_anagram_sets = len(list(filter(lambda anagram_set: len(anagram_set) == greatest_anagram_set_popn,
                                                      anagram_dict.values())))

    return greatest_anagram_set_popn, number_of_greatest_anagram_sets


if __name__ == "__main__":
    main()
