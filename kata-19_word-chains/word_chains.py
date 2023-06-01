#!/usr/bin/python3

import collections
import timeit
import operator


WORD_FILE = "wordlist.txt"

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# Load the words set
words = set(filter(str.isalpha, map(str.lower, map(str.strip, open(WORD_FILE, "r")))))


# Executes a breadth-first search of possible word permutations until either
# the target word has been found, or the tree of possible permutations has been
# exhausted.
def find_shortest_word_chain(starting_word, target_word, wordset):
    starting_word, target_word = starting_word.lower(), target_word.lower()

    if not starting_word.isalpha() or not target_word.isalpha():
        raise ValueError("both word arguments must not contain not-alphabetic characters")
    elif starting_word not in wordset:
        raise ValueError("starting_word argument not in supplied word set")
    elif target_word not in wordset:
        raise ValueError("target_word argument not in supplied word set")
    elif len(starting_word) != len(target_word):
        raise ValueError("starting_word and target_word must be of the same length")
    elif starting_word == target_word:
        return [starting_word]

    # Setting up data structures
    queue = collections.deque([(starting_word, [starting_word])])

    visited = set([starting_word])

    # The process of generating permutations from a word in this way naturally
    # yields tree-like data. Without ever dealing with a tree structure, this
    # algorithm executes a bread-first search through the data since the
    # generated data is tree-like.

    while queue:

        # The found words are stored with the path that lead to them, so that
        # that path can be returned if or when the target word is found.
        word, path = queue.popleft()

        if word == target_word:
            return path

        # Generate all permutations of this word, and store the ones that are
        # extant words in the wordset.
        for i in range(len(word)):
            for char in ALPHABET:
                new_word = word[:i] + char + word[i+1:]
                if new_word in wordset and new_word not in visited:
                    queue.append((new_word, path + [new_word]))
                    visited.add(new_word)

    return []


# Testing function that times both directions of a word chain.
def time_both_ways(left_word, right_word):

    print(f"{left_word} to {right_word} vs. {right_word} to {left_word}")

    one_way_time = round(operator.truediv(timeit.timeit(lambda: find_shortest_word_chain("silver", "golden", words),
                                                       number=1000),
                                          1000),
                         ndigits=5)

    other_way_time = round(operator.truediv(timeit.timeit(lambda: find_shortest_word_chain("golden", "silver", words),
                                                         number=1000),
                                            1000),
                           ndigits=5)
    print(f"{one_way_time} seconds vs. {other_way_time} seconds")


# Runs of the testing function to be able to answer a question in the Q&A.

time_both_ways("cat", "dog")

print()

time_both_ways("lead", "gold")

print()

time_both_ways("ruby", "code")

print()

time_both_ways("silver", "golden")


# Output of the above: 
# 
# cat to dog vs. dog to cat
# 0.00988 seconds vs. 0.01283 seconds
# 
# lead to gold vs. gold to lead
# 0.00999 seconds vs. 0.01361 seconds
# 
# ruby to code vs. code to ruby
# 0.01041 seconds vs. 0.01347 seconds
# 
# silver to golden vs. golden to silver
# 0.0099 seconds vs. 0.01361 seconds

# Q&A
#
# "Once your code works, try timing it. Does it take less than a second for the
# above examples given a decent-sized word list?"
#
# Seems to execute in a time between 0.010 seconds and 0.015 seconds. (Bearing
# in mind that these katas date to 2013, processor speed gains in the past 10
# years mean execution time expectations have shifted.)
#
#
# "And is the timing the same forwards and backwards (so 'lead' into 'gold'
# takes the same time as 'gold' into 'lead')?"
#
# In point of fact it is not. In each case one direction took ~130% of the
# execution time of the other. This is not surprising. Reasonably, the virtual
# tree of possible permutations of any two randomly chosen words may not have
# the same dimensions. One word might have a large number of permutations within
# 1 or 2 letters, while another might have a small number; the algorithm would
# run in different times for the two different words.
