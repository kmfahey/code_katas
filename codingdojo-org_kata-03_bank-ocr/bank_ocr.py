#!/usr/bin/python3

# User Story 1
#
# You work for a bank, which has recently purchased an ingenious machine to
# assist in reading letters and faxes sent in by branch offices. The machine
# scans the paper documents, and produces a file with a number of entries which
# each look like this:
# 
#     _  _     _  _  _  _  _
#   | _| _||_||_ |_   ||_||_|
#   ||_  _|  | _||_|  ||_| _|
# 
# Each entry is 4 lines long, and each line has 27 characters. The first 3 lines
# of each entry contain an account number written using pipes and underscores,
# and the fourth line is blank. Each account number should have 9 digits, all of
# which should be in the range 0-9. A normal file contains around 500 entries.
#
# Your first task is to write a program that can take this file and parse it
# into actual account numbers.


__all__ = ['text_to_numerals', 'checksum_acct_no']


# Accepts a multi-line string comprised of a series of 4-line blocks, such
# that lines 1-3 of the block is an OCRable block of digits expressed in
# pseudo-7-segment display ASCII art text, and the 4th line is always empty.
# Returns a series of 9-character numeric strings which are the numerals from
# the input text decoded.
def text_to_numerals(text_to_ocr):
    ocr_lines = _text_to_ocr_lines(text_to_ocr)
    numeral_strs = _ocr_lines_to_nums(ocr_lines)
    return numeral_strs

# Partially processes the input text to text_to_numerals(). Breaks it into a
# list of lists, where each inner list in the outer list contains the 3 lines to
# OCR.
def _text_to_ocr_lines(text_to_ocr):
    text_to_ocr_lines = text_to_ocr.split("\n")
    ocr_lines = [list() for _ in range(len(text_to_ocr_lines) // 4)]
    for text_to_ocr_index, ocr_partial_line in enumerate(text_to_ocr_lines):
        if not ocr_partial_line:
            continue
        ocr_lines_index = text_to_ocr_index // 4
        ocr_lines[ocr_lines_index].append(ocr_partial_line)
    return ocr_lines


def _ocr_glyph_to_numeral(ocr_glyph):
    match ocr_glyph:
        case ['   ',
              '  |',
              '  |']:
            return '1'
        case [' _ ',
              ' _|',
              '|_ ']:
            return '2'
        case [' _ ',
              ' _|',
              ' _|']:
            return '3'
        case ['   ',
              '|_|',
              '  |']:
            return '4'
        case [' _ ',
              '|_ ',
              ' _|']:
            return '5'
        case [' _ ',
              '|_ ',
              '|_|']:
            return '6'
        case [' _ ',
              '  |',
              '  |']:
            return '7'
        case [' _ ',
              '|_|',
              '|_|']:
            return '8'
        case [' _ ',
              '|_|',
              ' _|']:
            return '9'
        case other:
            return '?'


# Finishes processing for text_to_numerals(). Scans the line triplets, reading
# left-to-right in parallel, decoding the numerals and building a list of
# account numbers.
def _ocr_lines_to_nums(ocr_lines):
    ocr_numeral_strs = list()
    for ocr_line in ocr_lines:
        ocr_num_segments = list()
        for inner_index in range(9):
            ocr_line_segment = [ocr_line[outer_index][3*inner_index: 3*inner_index+3] for outer_index in range(3)]
            ocr_num_segments.append(_ocr_glyph_to_numeral(ocr_line_segment))
        ocr_numeral_strs.append("".join(ocr_num_segments))
    return ocr_numeral_strs


# User Story 2
# 
# Having done that, you quickly realize that the ingenious machine is not in
# fact infallible. Sometimes it goes wrong in its scanning. The next step
# therefore is to validate that the numbers you read are in fact valid account
# numbers. A valid account number has a valid checksum. This can be calculated
# as follows:
# 
# account number:  3  4  5  8  8  2  8  6  5
# position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1
# 
# checksum calculation:
# (d1+2*d2+3*d3+...+9*d9) mod 11 = 0
# 
# So now you should also write some code that calculates the checksum for a
# given number, and identifies if it is a valid account number.

def checksum_acct_no(acct_no_str):
    return sum((9-index)*int(acct_no_str[index]) for index in range(9)) % 11 == 0

