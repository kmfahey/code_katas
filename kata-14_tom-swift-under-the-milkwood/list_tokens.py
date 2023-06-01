#!/usr/bin/python3

import pickle
import collections


Algo_Output = collections.namedtuple("Algo_Output", ["initial_tokens", "digrams", "trigrams"])


with open("initial_digrams_+_trigrams.dat", "rb") as tg_fh:
    algo_output = pickle.load(tg_fh)

initial_tokens = algo_output.initial_tokens

digrams = algo_output.digrams

trigrams = algo_output.trigrams

tokens = set()

for pair in trigrams:
    tokens |= set(pair)

print("\n".join(tokens))
