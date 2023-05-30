#!/usr/bin/python3

import re
import math
import collections


# regexp used to extract values from datfile lines
line_re = re.compile("\. ([A-Za-z_]+) .*\D(\d+)  -  (\d+)")


Score_Range_Team = collections.namedtuple("Score_Range_Team", ["team", "score_diff"])

with open("football.dat", "r") as ftbl_fh:
    next(ftbl_fh)

    # initializing loop variables
    smallest_diff = Score_Range_Team(team="", score_diff=float("inf"))

    for next_line in ftbl_fh:
        line_match = line_re.search(next_line)
        if not line_match:
            continue

        # deriving this loop's team and score spread variables
        team = line_match.group(1).replace('_', ' ')
        score_diff = abs(int(line_match.group(3)) - int(line_match.group(2)))

        if score_diff < smallest_diff.score_diff:
            smallest_diff = Score_Range_Team(team, score_diff)

print(f"The smallest difference in scores belonged to {smallest_diff.team}. "
      f"It was {smallest_diff.score_diff} goal{'s' if smallest_diff.score_diff != 1 else ''}.")
