#!/usr/bin/python3

import math
import random

__all__ = ['iterative_binary_chop', 'recursive_binary_chop', 'segmenting_binary_chop', 'indexlist_binary_chop',
           'bogosort_binary_chop']


def iterative_binary_chop(target, seq):
    # This is a standard iterative binary search algorithm.

    lb_idx = 0
    ub_idx = len(seq) - 1
    while lb_idx <= ub_idx:
        midp_idx = math.floor((lb_idx + ub_idx) / 2)
        if seq[midp_idx] < target:
            lb_idx = midp_idx + 1
        elif seq[midp_idx] > target:
            ub_idx = midp_idx - 1
        else:
            return midp_idx
    return -1


def recursive_binary_chop(target, seq):
    # This is a standard recursive binary search algorithm. Rather than calling
    # the primary function to recurse, an inner function specialized for the
    # recursive step is used.

    def _inner_rec_chop(lb_idx, ub_idx):
        if lb_idx > ub_idx:
            return -1
        midp_idx = math.floor((lb_idx + ub_idx) / 2)
        if seq[midp_idx] < target:
            return _inner_rec_chop(midp_idx + 1, ub_idx)
        elif seq[midp_idx] > target:
            return _inner_rec_chop(lb_idx, midp_idx - 1)
        else:
            return midp_idx
    return _inner_rec_chop(0, len(seq) - 1)


def segmenting_binary_chop(target, seq):
    # My first invented binary search algorithm.
    #
    # This one works by enumerating the list, and then it iteratively divides
    # the sequence in half and throws away the half whose lowest element is
    # greater than the target value, or whose highest element is less than the
    # target value. If halving the sequence yields a target half that's length
    # one, the enumerated index is returned.
    if not len(seq) or target < seq[0] or target > seq[-1]:
        return -1
    elif len(seq) == 0 and seq[0] == target:
        return 0
    divide_seq = lambda seq: [seq[0:math.ceil(len(seq)/2)], seq[math.ceil(len(seq)/2):len(seq)]]
    seq_pieces = divide_seq(list(enumerate(seq)))
    while len(seq_pieces[0]) or len(seq_pieces[1]):
        lower_half, upper_half = seq_pieces
        if len(lower_half) and target <= lower_half[-1][1]:
            chosen_half = lower_half
        elif len(upper_half) and target >= upper_half[0][1]:
            chosen_half = upper_half
        else:
            return -1
        if len(chosen_half) == 1 and chosen_half[0][1] == target:
            return chosen_half[0][0]
        else:
            seq_pieces = divide_seq(chosen_half)
    return -1


def indexlist_binary_chop(target, seq):
    # My second invented binary search algorithm.
    #
    # This one isn't too different from an iterative algorithm, but it works
    # over a list of the indexes to elements in the sequence, instead of the
    # sequence itself.
    index_list = list(range(0, len(seq)))
    while len(index_list):
        midpoint = len(index_list)//2
        if seq[index_list[midpoint]] > target:
            # If the midpoint value is greater than the target, then the target's correct index is lower.
            del index_list[midpoint:]
        elif seq[index_list[midpoint]] < target:
            del index_list[:midpoint+1]
        else:
            return index_list[midpoint]
    return -1


def bogosort_binary_chop(target, seq):
    # My third invented binary search algorithm.
    # 
    # This one works with an enumerated sequence again. It starts by shuffling
    # the enumerated sequence. Then it iteratively picks a median value from
    # the sequence, and effects the halving of the search area by filtering out
    # of the sequence pairs whose 2nd value is greater than, or less than, the
    # median value.
    enum_seq = list(enumerate(seq))
    random.shuffle(enum_seq)
    while len(enum_seq) > 0:
        midp_val = list(sorted(enum_seq, key=lambda pair: pair[1]))[len(enum_seq)//2][1]
        midp_idx, = [idx for idx in range(len(enum_seq)) if enum_seq[idx][1] == midp_val]
        if midp_val > target:
            enum_seq = [pair for pair in enum_seq if pair[1] < midp_val]
        elif midp_val < target:
            enum_seq = [pair for pair in enum_seq if pair[1] > midp_val]
        elif midp_val == target:
            return enum_seq[midp_idx][0]
        else:
            return -1
    return -1


# Q & A:
#
# As you’re coding each algorithm, keep a note of the kinds of error you
# encounter. A binary search is a ripe breeding ground for “off by one” and
# fencepost errors. As you progress through the week, see if the frequency of
# these errors decreases (that is, do you learn from experience in one technique
# when it comes to coding with a different technique?).
#
# Not in so many words. I never try and write an algorithm from scratch given
# just its description when I can find existing pseudocode and adapt that. In
# both the iterative and recursive soltutions, I coded from pseudocode, and so
# avoided off-by-one errors.
#
#
# What can you say about the relative merits of the various techniques you’ve
# chosen? Which is the most likely to make it in to production code? Which was
# the most fun to write? Which was the hardest to get working? And for all these
# questions, ask yourself “why?”.
#
# I happened to find the segmenting solution the most aesthetically pleasing.
# I'd only use an iterative or recursive solution in production code, but the
# idea behind the segmenting approach might make it into production code in some
# other way.
#
#
# It’s fairly hard to come up with five unique approaches to a binary chop.
# How did you go about coming up with approaches four and five? What techniques
# did you use to fire those “off the wall” neurons?
#
# The segmented solution came to me as inspiration. I just got lucky. my
# 4th solution is pretty derivative of the canonical iterative approach, no
# creativity there. And the idea of incorporating a bogosort-inspired approach
# to algorithm #5 came to me just because the algorithms are based on sorting.
