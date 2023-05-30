#!/usr/bin/python3

import collections

Temp_Range_Day = collections.namedtuple("Temp_Range_Day", ["temp_range", "day_no"])


with open("weather.dat", "r") as wdat_fh:
    next(wdat_fh) # discarding unused header line
    next(wdat_fh) # discarding blank line

    # initializing loop variables
    smallest_range = Temp_Range_Day(temp_range=float("inf"), day_no=None)
    line_vals = next(wdat_fh).strip().split()

    while line_vals[0].isdigit():
        day_no = int(line_vals[0])

        # computing temp range
        max_temp = int(line_vals[1].strip('*'))
        min_temp = int(line_vals[2].strip('*'))
        temp_range = max_temp - min_temp

        # checking newest range against running 
        if temp_range < smallest_range.temp_range:
            smallest_range = Temp_Range_Day(temp_range, day_no)
        line_vals = next(wdat_fh).strip().split()

    # doesn't need to check for StopIteration bc the last line of the data file
    # doesn't satisfy `line_vals[0].isdigit()`


# Attaches the correct suffix to an ordinal number and returns as a str.
def ord_w_suff(ordinal):
    day_no_suffixes = {0:"th", 1:"st", 2:"nd", 3:"rd", 4:"th", 5:"th", 6:"th", 7:"th", 8:"th", 9:"th"}
    return str(ordinal) + day_no_suffixes[ordinal % 10]


print(f"The smallest temperature range occurred on the {ord_w_suff(smallest_range.day_no)} day. "
      f"It was a range of {smallest_range.temp_range}°.")
