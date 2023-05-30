#!/usr/bin/python3

import _md5
import numpy
import datetime
import math
import random
import statistics


# Load the word list, create a Bloom filter, then run tests on the filter to
# determine what the probability of false positives is.
def main():
    wordlist = list(filter(str.isalpha, map(str.lower, map(str.strip, open("/usr/share/dict/words")))))

    bloom_filter = compose_bloom_filter(wordlist)

    test_bloom_filter(bloom_filter, wordlist)


# Instance a Bloom Filter, and populate it with words from the loaded word list.
def compose_bloom_filter(wordlist):
    bloom_filter = Bloom_Filter(1000960, 10)

    for index, word in enumerate(wordlist, start=1):
        bloom_filter.add_string_to_filter(word)
        if index % 5000 == 0:
            print(f"{datetime.datetime.now().isoformat()}: added {index}/{len(wordlist)} words to Bloom filter", )

    print(f"{datetime.datetime.now().isoformat()}: added {len(wordlist)}/{len(wordlist)} words to Bloom filter", )

    return bloom_filter


# Run a series of tests on the Bloom filter. Run a number of trials (default
# 100), where in each trial, randomly generated sequences of alphabetic chars
# are tested for membership in the Bloom filter.
def test_bloom_filter(bloom_filter, wordlist, number_of_trials=100, words_per_trial=10000):
    wordset = set(wordlist)

    false_pos_list = []
    true_pos_list = []

    for index in range(number_of_trials):
        run_bloom_filter_trial(index, bloom_filter, wordset, false_pos_list, true_pos_list)

    # Computes the ratios between false positives and true negatives for each trial.
    false_pos_true_neg_list = [false_pos / (10000 - false_pos - true_pos)
                               for false_pos, true_pos in zip(false_pos_list, true_pos_list)]

    # Computes the average ratio between false positives and true negatives.
    # This ratio is the probability of getting a false positive.
    avg_false_pos_true_neg_prop = round(statistics.mean(false_pos_true_neg_list), 5)

    print(f"Average ratio of false positives to true negatives was {avg_false_pos_true_neg_prop}.")


# Runs a single trial on the Bloom filter. Generates a series of random strings
# of alphabetic characters (default 10000), and tests each one for membership in
# the Bloom filter. True positives and false positives are recorded, and true
# negatives are computed.
def run_bloom_filter_trial(index, bloom_filter, wordset, false_pos_list, true_pos_list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    false_positives = 0
    true_positives = 0

    for _ in range(10000):
        strlen = random.randint(3,8)
        randstr = ''.join(random.choice(alphabet) for _ in range(strlen))
        if bloom_filter.is_string_in_filter(randstr):
            if randstr in wordset:
                true_positives += 1
            else:
                false_positives += 1

    false_pos_list.append(false_positives)
    true_pos_list.append(true_positives)

    print(f"Trial {index}. False positives: {false_positives}; true positives: {true_positives}; "
          f"negatives: {10000 - false_positives - true_positives}")


class Bloom_Filter:
    __slots__ = 'm', 'k', 'bloom_filter',

    # m is the width of the filter in bits.
    #
    # k is the number of hash functions to use. m % k must equal 0.
    #
    # Each hash function's output is an array of bits of a length m / k, where
    # only one bit is 1 and all other bits are 0. In this way, each word added
    # to the filter will set at most k bits to 1 across the entire filter.

    def __init__(self, m, k):
        if m % k:
            raise Exception("m must be a multiple of k")
        self.m = m
        self.k = k
        self.bloom_filter = numpy.array(numpy.zeros(self.m, dtype=bool), dtype=bool)

    # __getstate__ and __setstate__ are dunder methods needed to be compatible
    # with pickle serialization.
    def __getstate__(self):
        return (self.m, self.k, self.bloom_filter)

    def __setstate__(self, state):
        self.m, self.k, self.bloom_filter = state

    # Applies the k hash functions to the argument strval. For convenience,
    # rather than returning a bitlist of length m, returns an array of indexes
    # in that bitlist that would be set to 1.
    def _string_hashidxs(self, strval):
        # calculates the md5sum of strval + n for n in [0,9], which amounts to
        # 10 difference hash functions.
        md5sums = [_md5.md5((strval + str(offset)).encode("utf8"),
                            usedforsecurity=False).hexdigest() for offset in range(10)]

        # interprets the md5sums as hexadecimal integers and converts them to
        # base-10 ints with a range of [0,2**128-1]
        chksums = [int('0x' + md5sum, 16) for md5sum in md5sums]

        # takes the int values of the checksums and applies a scaling factor.
        # Adjusted values are now in a range of [0, m/k]
        rescaled = [int(math.floor(chksum * (self.m / self.k / (2**128 - 1)))) for chksum in chksums]

        # Applies an offset to each index, such that the nth hash x is now equal
        # to x + n * (m / k). In this way the 10 indexes are spread across the m
        # / k bits of the bloom filter.
        hashidxs = [int(intval + offset * (self.m / self.k)) for offset, intval in enumerate(rescaled)]
        return hashidxs

    # Accepts a list of indexes, and for each sets the bit at that index in the
    # bloom filter to 1.
    def _add_hashidxs_to_filter(self, hashidxs):
        for index in hashidxs:
            self.bloom_filter[index] = True

    # Computes hash indexes for the string argument and then sets those indexes
    # to 1 in the bloom filter.
    def add_string_to_filter(self, string):
        self._add_hashidxs_to_filter(self._string_hashidxs(string))

    # Tests whether a string is in the bloom filter.
    def is_string_in_filter(self, string):
        return all(self.bloom_filter[index] for index in self._string_hashidxs(string))

    # Debugging method. Returns the first 128 bits of the bloom filter as a binary number.
    def bloom_filter_in_binary(self):
        return "0b" + ''.join("1" if bit else "0" for bit in self.bloom_filter[:128])


if __name__ == "__main__":
    main()
