#!/usr/bin/python3

__all__ = "total_scores", "Frame", "Scoreboard"


def total_scores(scoring_1, scoring_2, scoring_3, scoring_4, scoring_5,
                 scoring_6, scoring_7, scoring_8, scoring_9, scoring_10):
    # This is unlovely, but since there must be exactly 10 scoring strings, it
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
    __slots__ = "frame_number", "score_1st", "score_2nd", "is_strike", "is_spare", "next_frame"

    def __init__(self, frame_number, score_1st=0, score_2nd=0, bonus_1st=0, bonus_2nd=0, is_strike=False,
                 is_spare=False, next_frame=None):
        self.frame_number = frame_number
        self.score_1st = score_1st
        self.score_2nd = score_2nd
        self.is_strike = is_strike
        self.is_spare = is_spare
        self.next_frame = next_frame

    def calc_score(self):
        if self.is_strike:                                                  # if the frame is a strike
            score = 10                                                      #  then the base score is 10
            if self.frame_number == 10:                                     #  if it's the 10th frame
                                                                            #  it'll have two bonus rolls.
                score += self.bonus_1st if self.bonus_1st != "X" else 10    #   add the bonus roll scores
                score += self.bonus_2nd if self.bonus_2nd != "X" else 10    #   adding 10 where one is a strike
            elif self.frame_number == 9:                                    #  elif it's the 9th frame
                if self.next_frame.is_spare:                                #   if the 10th frame is a spare
                    score += 10                                             #    add 10
                else:                                                       #   else
                    score += self.next_frame.score_1st                      #    add the first 2 scores 
                    score += self.next_frame.score_2nd                      #    from the 10th frame
            else:                                                           #  else
                if self.next_frame.is_strike:                               #   if the next frame was a strike
                    if self.next_frame.next_frame.is_strike:                #    if the following frame's a strike
                        score += 20                                         #     then add 20
                    else:                                                   #    else
                        score += 10                                         #     then add 10
                        score += self.next_frame.next_frame.score_1st       #     plus following frame's 1st score
                elif self.next_frame.is_spare:                              #   elif the next frame was a spare
                    score += 10                                             #    then add 10
                else:                                                       #   else
                    score += self.next_frame.score_1st                      #    then add the next
                    score += self.next_frame.score_2nd                      #    frame's two scores
        elif self.is_spare:                                                 # elif the frame is a spare
            score = 10                                                      #  then the base score is 10
            if self.frame_number == 10:                                     #  if it's the 10th frame
                score += self.bonus_1st if self.bonus_1st != "X" else 10    #   it'll have one bonus roll
                                                                            #   add the score from the bonus roll
            else:                                                           #  else
                score += self.next_frame.score_1st                          #   add the next frame's 1st roll
        else:                                                               # else
            score = self.score_1st                                          #  the frame is open; the score is the 
            score += self.score_2nd                                         #  1st roll plus the 2nd roll
        return score


class Scoreboard:
    __slots__ = "frame_objs",

    def __init__(self):
        self.frame_objs = list(map(Frame, range(1, 11)))

    def update_from_scoring(self, frame_number, scoring):
        frame_index = frame_number - 1
        frame_obj = self.frames[frame_index]
        if scoring[0] == "X":
            frame_obj.is_tplike = True
            if frame_index == 9:
                frame_obj.bonus_1st = 10 if scoring[1] == "X" else int(scoring[1])
                frame_obj.bonus_2nd = 10 if scoring[2] == "X" else int(scoring[2])
        elif scoring[1] == "/":
            frame_obj.is_spare = True
            if frame_index == 9:
                frame_obj.bonus_1st = 10 if scoring[2] == "X" else int(scoring[2])
        else:
            frame_obj.score_1st = int(scoring[0])
            frame_obj.score_2nd = int(scoring[1])
        if frame_index != 9:
            frame_obj.next_frame = self.frame_objs[frame_index + 1]

    def calc_score(self):
        return sum(frame_obj.calc_score() for frame_obj in self.frames)
