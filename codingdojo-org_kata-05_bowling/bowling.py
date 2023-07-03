#!/usr/bin/python3

__all__ = "total_scores", "Frame", "Scoreboard"


def total_scores(scoring_1, scoring_2, scoring_3, scoring_4, scoring_5,
                 scoring_6, scoring_7, scoring_8, scoring_9, scoring_10):
    # This is unlovely, but since there must be exactly 10 scoring tuples, it
    # seems better to let python's own function signature enforcement handle it
    # than manually length-test an *argl variable.
    scoring_tpl = (scoring_1, scoring_2, scoring_3, scoring_4, scoring_5,
                   scoring_6, scoring_7, scoring_8, scoring_9, scoring_10)
    scoreboard_obj = Scoreboard()
    for frame_number, scoring in zip(range(1, 11), scoring_tpl):
        scoreboard_obj.update_from_scoring(frame_number, scoring)
    total_score = scoreboard_obj.calc_score()
    return total_score


class Frame:
    __slots__ = ("frame_number", "score_1st", "score_2nd", "bonus_1st", "bonus_2nd", "is_strike", "is_spare",
                 "next_frame")

    def __init__(self, frame_number, score_1st=0, score_2nd=0, bonus_1st=0, bonus_2nd=0, is_strike=False,
                 is_spare=False, next_frame=None):
        self.frame_number = frame_number
        self.score_1st = score_1st
        self.score_2nd = score_2nd
        self.bonus_1st = bonus_1st
        self.bonus_2nd = bonus_2nd
        self.is_strike = is_strike
        self.is_spare = is_spare
        self.next_frame = next_frame

    def calc_score(self):
        if self.is_strike:
            return self._calc_is_strike_score()
        elif self.is_spare:
            return self._calc_is_spare_score()
        else:
            return self._calc_is_open_frame_score()

    def _calc_is_strike_score(self):
        score = 10
        if self.frame_number == 10:
            score += self.bonus_1st + self.bonus_2nd
        elif self.frame_number == 9:
            if self.next_frame.is_strike:
                score += 10 + self.next_frame.bonus_1st
            elif self.next_frame.is_spare:
                score += 10
            else:
                score += self.next_frame.score_1st + self.next_frame.score_2nd
        else:
            if self.next_frame.is_strike:
                score += 10
                if self.next_frame.next_frame.is_strike:
                    score += 10
                else:
                    score += self.next_frame.next_frame.score_1st
            elif self.next_frame.is_spare:
                score += 10
            else:
                score += self.next_frame.score_1st + self.next_frame.score_2nd
        return score

    def _calc_is_spare_score(self):
        score = 10
        if self.frame_number == 10:
            score += self.bonus_1st
        else:
            score += self.next_frame.score_1st
        return score

    def _calc_is_open_frame_score(self):
        score = self.score_1st + self.score_2nd
        return score

    def __repr__(self):
        return ("Frame(frame_number={frame_number}, score_1st={score_1st}, score_2nd={score_2nd}, "
                       "bonus_1st={bonus_1st}, bonus_2nd={bonus_2nd}, is_strike={is_strike}, "
                       "is_spare={is_spare}, next_frame=<next_frame>)"
                ).format(frame_number=repr(self.frame_number), score_1st=repr(self.score_1st),
                         score_2nd=repr(self.score_2nd), bonus_1st=repr(self.bonus_1st),
                         bonus_2nd=repr(self.bonus_2nd), is_strike=repr(self.is_strike),
                         is_spare=repr(self.is_spare))


class Scoreboard:
    __slots__ = "frame_objs",

    def __init__(self):
        self.frame_objs = list(map(Frame, range(1, 11)))

    def update_from_scoring(self, frame_number, scoring):
        frame_index = frame_number - 1
        frame_obj = self.frame_objs[frame_index]
        if scoring[0] == "X":
            frame_obj.is_strike = True
            frame_obj.score_1st = 10
            if frame_index == 9:
                frame_obj.bonus_1st = 10 if scoring[1] == "X" else 0 if scoring[1] == "-" else int(scoring[1])
                frame_obj.bonus_2nd = 10 if scoring[2] == "X" else 0 if scoring[2] == "-" else int(scoring[2])
        elif scoring[1] == "/":
            frame_obj.is_spare = True
            frame_obj.score_1st = 0 if scoring[0] == "-" else int(scoring[0])
            if frame_index == 9:
                frame_obj.bonus_1st = 10 if scoring[2] == "X" else 0 if scoring[2] == "-" else int(scoring[2])
        else:
            frame_obj.score_1st = 0 if scoring[0] == "-" else int(scoring[0])
            frame_obj.score_2nd = 0 if scoring[1] == "-" else int(scoring[1])
        if frame_index != 9:
            frame_obj.next_frame = self.frame_objs[frame_index + 1]

    def calc_score(self):
        scores = [frame_obj.calc_score() for frame_obj in self.frame_objs]
        return sum(scores)
