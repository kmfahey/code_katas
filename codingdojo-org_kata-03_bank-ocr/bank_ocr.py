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


__all__ = ['text_to_numerals', 'checksum_acct_no', 'bulk_process_acct_no_text', 'bulk_process_acct_no_text_2']


# Accepts a multi-line string comprised of a series of 4-line blocks, such
# that lines 1-3 of the block is an OCRable block of digits expressed in
# pseudo-7-segment display ASCII art text, and the 4th line is always empty.
# Returns a series of 9-character numeric strings which are the numerals from
# the input text decoded.
def text_to_numerals(text_to_ocr):
    ocr_lines = _text_to_ocr_lines(text_to_ocr)
    acct_nos = _ocr_lines_to_nums(ocr_lines)
    return acct_nos

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


# Just a match/case statement that converts text segments to numbers. Done with
# match/case because it's more readable.
def _ocr_glyph_to_numeral(ocr_glyph):
    match ocr_glyph:
        case [' _ ',
              '| |',
              '|_|']:
            return '0'
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
        case _:
            return '?'


# Finishes processing for text_to_numerals(). Scans the line triplets, reading
# left-to-right in parallel, decoding the numerals and building a list of
# account numbers.
def _ocr_lines_to_nums(ocr_lines):
    ocr_acct_nos = list()
    for ocr_line in ocr_lines:
        ocr_num_segments = list()
        for inner_index in range(9):
            ocr_line_segment = [ocr_line[outer_index][3*inner_index: 3*inner_index+3] for outer_index in range(3)]
            ocr_num_segments.append(_ocr_glyph_to_numeral(ocr_line_segment))
        ocr_acct_nos.append("".join(ocr_num_segments))
    return ocr_acct_nos


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


# User Story 3
# 
# Your boss is keen to see your results. He asks you to write out a file of your
# findings, one for each input file, in this format:
# 
# 457508000
# 664371495 ERR
# 86110??36 ILL
# 
# ie the file has one account number per row. If some characters are illegible,
# they are replaced by a ?. In the case of a wrong checksum, or illegible
# number, this is noted in a second column indicating status.

# Extracts account numbers from text, then marks them if they contains a
# nonparsing number, or if they don't checksum, and returns marked-up output.
def bulk_process_acct_no_text(acct_no_text):
    output = list()
    acct_numbers = text_to_numerals(acct_no_text)
    for acct_no_str in acct_numbers:
        if "?" in acct_no_str:
            output.append(f"{acct_no_str} ILL")
        elif not checksum_acct_no(acct_no_str):
            output.append(f"{acct_no_str} ERR")
        else:
            output.append(acct_no_str)
    return "\n".join(output)


# User Story 4
# 
# It turns out that often when a number comes back as ERR or ILL it is because
# the scanner has failed to pick up on one pipe or underscore for one of the
# figures. For example
# 
#     _  _  _  _  _  _     _ 
# |_||_|| || ||_   |  |  ||_ 
#   | _||_||_||_|  |  |  | _|
# 
# The 9 could be an 8 if the scanner had missed one |. Or the 0 could be an
# 8. Or the 1 could be a 7. The 5 could be a 9 or 6. So your next task is to
# look at numbers that have come back as ERR or ILL, and try to guess what they
# should be, by adding or removing just one pipe or underscore. If there is
# only one possible number with a valid checksum, then use that. If there are
# several options, the status should be AMB. If you still can’t work out what
# it should be, the status should be reported ILL.


# Extracts account numbers from text, then marks them if they contains a
# nonparsing number, or if they don't checksum, and returns marked-up output.
#
# Rewrite that un-refactors the code of text_to_numerals(). Tests each number
# and attempts to "repair" it, assuming a missed character. Outputs the repaired
# number if it's reachable, or marks it AMB if more than one number could
# satisfy the constraints. Otherwise applies the ILL flag if it still has an
# unparseable character, or the ERR flag if it doesn't checksum.
def bulk_process_acct_no_text_2(acct_no_text):
    ocr_lines = _text_to_ocr_lines(acct_no_text)
    acct_nos = _ocr_lines_to_nums(ocr_lines)
    for index, acct_no in enumerate(acct_nos):
        if "?" in acct_no or not checksum_acct_no(acct_no):
            repair_attempt = _repair_acct_no(ocr_lines[index])
        if len(repair_attempt) == 1:
            acct_nos[index] = (repair_attempt[0], "")
        elif len(repair_attempt) > 1:
            acct_nos[index] = (acct_no, "AMB")
        elif "?" in acct_no:
            acct_nos[index] = (acct_no, "ILL")
        elif not checksum_acct_no(acct_no):
            acct_nos[index] = (acct_no, "ERR")
        else:
            acct_nos[index] = (acct_no, "")
    output = [acct_no + (" " + flag if flag else "") for acct_no, flag in acct_nos]
    return output


# Private function that applies an algorithm to try to repair an account number
# that contains an illegible character or doesn't checksum. Generates all
# possible permutations of the original glyphic text where a space is replaced
# by either an underscore or pipe. Attempts to parse each one, and then checksum
# it. Returns a list of all parsed numbers, with no illegible chars, that
# checksummed.
def _repair_acct_no(ocr_line):
    space_indexes = list()
    for outer_index in range(3):
        space_indexes.append([inner_index
                                for inner_index, character in enumerate(ocr_line[outer_index])
                                    if character == " "])
    space_coords = [(outer_index, inner_index)
                        for outer_index in range(3)
                            for inner_index in space_indexes[outer_index]]
    ocr_line_permuts = list()
    for outer_index, inner_index in space_coords:
        for alternate_char in ("|", "_"):
            ocr_line_permut = ocr_line.copy()
            ocr_line_permut[outer_index] = (ocr_line_permut[outer_index][:inner_index]
                                            + alternate_char
                                            + ocr_line_permut[outer_index][inner_index+1:])
            ocr_line_permuts.append(ocr_line_permut)
    valid_acct_nos = list(filter(lambda acct_no: "?" not in acct_no and checksum_acct_no(acct_no),
                                 _ocr_lines_to_nums(ocr_line_permuts)))
    return valid_acct_nos
