#!/usr/bin/python3


alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

non_alpha = " !" + '"' + "#$%&'()*+,-./0123456789:;<=>?@[\]^_`{|}~"

# The translation table needed to use str.translate to lowercase all uppercase
# letters in the string, and strip out all non-alphabetic characters.
upr_to_lwr_strip_others_tr = str.maketrans(alpha_upper, alpha_lower, non_alpha)


# Extracts all alphabetic characters from the string and returns a string
# comprised of those chars in alphabetic order.
def sort_characters(string):
    # Lowercases all uppercase and strips out all non-alphabetic.
    string = string.translate(upr_to_lwr_strip_others_tr)
    chardict = {char: string.count(char) for char in alpha_lower}
    return ''.join(char * chardict[char] for char in alpha_lower)


print(sort_characters("When not studying nuclear physics, Bambi likes to play beach volleyball."))

# Q&A
#
# "Are there any ways to perform this sort cheaply, and without using built-in
# libraries?"
#
# Done. I avoided using sorted(), by composing the return string by iterating
# over a string that comprised the alphabet.
