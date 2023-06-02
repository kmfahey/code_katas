#!/usr/bin/python3

import re

import textwrap



alphabet = "abcdefghijklmnopqrstuvwxyz"

wordlist_file = "/usr/share/dict/words"


wordset = set()

words_orig_capitalization = dict()

wordlist_file_obj = open(wordlist_file, "r")

word_list = list(filter(lambda word: len(word) <= 2,
                        map(str.strip, wordlist_file_obj)))


for word in word_list:

    word_lower = word.lower()

    words_orig_capitalization[word_lower] = word

    wordset.add(word_lower)


all_possible_words = set([left_char + right_char
                            for left_char in "documenting"
                                for right_char in "documenting"
                                    if left_char != right_char
                                        or left_char == "n"
                                        and right_char == "n"])


anagrams_list = list(filter(lambda word: word in wordset, all_possible_words))

anagrams_list = sorted(anagrams_list)

anagrams_list = [words_orig_capitalization[word] for word in anagrams_list]


quoted_anagrams_list = [f"'{anagram}'" for anagram in anagrams_list]

formatted_anagrams_list = ", ".join(quoted_anagrams_list[:-1])

formatted_anagrams_list += ", and " + quoted_anagrams_list[-1]

formatted_anagrams_list = "\n".join(textwrap.wrap(formatted_anagrams_list, width=80))


print(f"There are {len(anagrams_list)} possible 2-letter anagrams in the word 'documenting'. They are:")

print(formatted_anagrams_list)
