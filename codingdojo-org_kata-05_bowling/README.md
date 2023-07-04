# CodingDojo.com Kata #5: Bowling

## Kata Source

Kata is drawn from codingdojo.com. Original code kata webpage is visible
[here](https://codingdojo.org/kata/Bowling/).

## Kata Partial Instructions

> ### Bowling
> 
> This description is based on that at [Adventures in C#: The Bowling Game
> Problem Description](http://ronjeffries.com/xprog/articles/acsbowling/)
> 
> Create a program, which, given a valid sequence of rolls for one line of
> American Ten-Pin Bowling, produces the total score for the game. Here are some
> things that the program will not do:
> 
> * We will not check for valid rolls.
> * We will not check for correct number of rolls and frames.
> * We will not provide scores for intermediate frames.
> 
> Depending on the application, this might or might not be a valid way to define
> a complete story, but we do it here for purposes of keeping the kata light. I
> think you’ll see that improvements like those above would go in readily if
> they were needed for real.

See the above-linked page for full kata text.

## Pseudocode

This is the pseudocode of the scoring process. This pseudocode
reflects the logic in bowling.Frame.\_calc\_is\_strike\_score(),
bowling.Frame.\_calc\_is\_spare\_score(), and
bowling.Frame.calc\_is\_open\_frame\_score().

<pre>
if the frame is a strike
    then the base score is 10
    if it's the 10th frame, it'll have two bonus rolls.
        add the 2nd and 3rd bonus roll scores
    elif it's the 9th frame
        if the 10th frame is a strike
            add 10 plus the first bonus roll
        else if it's a spare
            add 10
        else
            add both the rolls of the 10th frame
    else
        if the next frame was a strike
            add 10
            if the next next frame was a strike
                add 10
            else
                then add the next next frame's 1st roll
        elif the next frame was a spare
            then add 10
        else
            then add both rolls from the next frame
elif the frame is a spare
    then the base score is 10
    if it's the 10th frame
        then add the first bonus roll
    else
        then add the next frame's first roll
else
    the score is the 1st roll plus the 2nd roll
</pre>
