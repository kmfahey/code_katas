#!/usr/bin/python3

import re
import textwrap


alphabet = "abcdefghijklmnopqrstuvwxyz"

wordlist_file = "/usr/share/dict/words"

wordlist_file_obj = open(wordlist_file, "r")

wordset = set()

words_orig_capitalization = dict()

for wordlist_line in wordlist_file_obj:
    word = wordlist_line.strip()
    if len(word) > 2:
        continue
    words_orig_capitalization[word.lower()] = word
    wordset.add(word.lower())

base_word = "documenting"

anagrams_list = list()

for first_index in range(len(base_word)):
    for second_index in range(len(base_word)):

        if first_index == second_index:
            continue

        first_possible_word = base_word[first_index] + base_word[second_index]
        if first_possible_word in wordset and first_possible_word not in anagrams_list:
            anagrams_list.append(first_possible_word)

        second_possible_word = base_word[second_index] + base_word[first_index]
        if second_possible_word in wordset and second_possible_word not in anagrams_list:
            anagrams_list.append(second_possible_word)

print(f"There are {len(anagrams_list)} possible 2-letter anagrams in the word '{base_word}'. They are:")

anagrams_list = sorted(anagrams_list)

anagrams_list = [words_orig_capitalization[word] for word in anagrams_list]

quoted_anagrams_list = [f"'{anagram}'" for anagram in anagrams_list]

formatted_anagrams_list = ", ".join(quoted_anagrams_list[:-1])

formatted_anagrams_list += ", and " + quoted_anagrams_list[-1]

formatted_anagrams_list = "\n".join(textwrap.wrap(formatted_anagrams_list, width=80))

print(formatted_anagrams_list)



