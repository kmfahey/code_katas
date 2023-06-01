#!/usr/bin/python3


for n in range(1,64+1):
    binoutp = bin(n)
    print(f"for int value {n}, binary representation {binoutp}",
          ("DOES contain 00" if '00' in binoutp else "DOES NOT contain 00"))


# Q&A
#
# "What is the number for sequences of length 4, 5, 10, n?"
#
# The above loop calculates and prints the number of each for all binary
# integers between 1 and 64.
#
#
# "Having worked out the pattern, there’s a second part to the question: can
# you prove why the relationship exists?"
#
# I don't discern a pattern. I don't know why the relationship exists. If I were
# a mathematician maybe I could answer. Speaking as a programmer, I just write
# the code, sorry.
