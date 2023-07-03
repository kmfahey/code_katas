#!/usr/bin/python3

from bowling import total_scores


def test_all_strikes():
    scorings = list(map(tuple, "X X X X X X X X X XXX".split(" ")))
    score = total_scores(*scorings)
    assert score == 300

def test_all_nines():
    scorings = list(map(tuple, "9- 9- 9- 9- 9- 9- 9- 9- 9- 9-".split(" ")))
    score = total_scores(*scorings)
    assert score == 90

def test_all_splits():
    scorings = list(map(tuple, "5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5".split(" ")))
    score = total_scores(*scorings)
    assert score == 150

# strike scoring, frame number 10
def test_strike_scoring_frame_10_two_more_strikes():
    scorings = list(map(tuple, "-- -- -- -- -- -- -- -- -- XXX".split(" ")))
    score = total_scores(*scorings)
    assert score == 30

# strike scoring, frame number 10
def test_strike_scoring_frame_10_one_more_strike():
    scorings = list(map(tuple, "-- -- -- -- -- -- -- -- -- X2X".split(" ")))
    score = total_scores(*scorings)
    assert score == 22

# strike scoring, frame number 10
def test_strike_scoring_frame_10_no_more_strikes():
    scorings = list(map(tuple, "-- -- -- -- -- -- -- -- -- X32".split(" ")))
    score = total_scores(*scorings)
    assert score == 15

# strike scoring, frame number 9, frame ten is a strike
def test_strike_scoring_frame_9_frame_10_is_strike():
    scorings = list(map(tuple, "-- -- -- -- -- -- -- -- X X44".split(" ")))
    score = total_scores(*scorings)
    assert score == 42

# strike scoring, frame number 9, frame ten is a spare
def test_strike_scoring_frame_9_frame_10_is_spare():
    scorings = list(map(tuple, "-- -- -- -- -- -- -- -- X 4/7".split(" ")))
    score = total_scores(*scorings)
    assert score == 37

# strike scoring, frame number 9, frame ten is open
def test_strike_scoring_frame_9_frame_10_is_open():
    scorings = list(map(tuple, "-- -- -- -- -- -- -- -- X 8-".split(" ")))
    score = total_scores(*scorings)
    assert score == 26

# strike scoring, frame between 1 - 8, next frame is a strike
def test_strike_scoring_frame_1_thru_8_next_frame_strike():
    scorings = list(map(tuple, "-- -- -- -- -- -- X X 41 --".split(" ")))
    score = total_scores(*scorings)
    assert score == 44

# strike scoring, frame between 1 - 8, next frame is a spare
def test_strike_scoring_frame_1_thru_8_next_frame_spare():
    scorings = list(map(tuple, "-- -- -- -- -- X 7/ 52 -- --".split(" ")))
    score = total_scores(*scorings)
    assert score == 42

# strike scoring, frame between 1 - 8, next frame is open
def test_strike_scoring_frame_1_thru_8_next_frame_open():
    scorings = list(map(tuple, "-- -- -- -- -- X 24 -- -- --".split(" ")))
    score = total_scores(*scorings)
    assert score == 22

# spare scoring, frame between 1 - 9
def test_spare_scoring_frame_1_thru_9():
    scorings = list(map(tuple, "-- -- -- -- -- -- 8/ 1- -- --".split(" ")))
    score = total_scores(*scorings)
    assert score == 12

# spare scoring, frame number 10
def test_spare_scoring_frame_10():
    scorings = list(map(tuple, "-- -- -- -- -- -- -- -- -- -/3".split(" ")))
    score = total_scores(*scorings)
    assert score == 13

## open frame scoring
def test_open_scoring():
    scorings = list(map(tuple, "-- -- -- -- -- -- -- -- 45 --".split(" ")))
    score = total_scores(*scorings)
    assert score == 9
