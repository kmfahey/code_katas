# CodingDojo.com Kata #14: Eight Queens

## Kata Source

Kata is drawn from codingdojo.com. Original code kata webpage is visible
[here](https://codingdojo.org/kata/eight-queens/).

## Kata Instructions Excerpt

> ### Eight Queens
>
> #### Kata
>
> This kata is based on the classic chess rules. You must put eight chess queens
> on an 8×8 chessboard such that none of them is able to capture any other
> using the standard chess queen’s moves.
>
> Tips: you could have only one queen by row and column.

See the above-linked page for full kata text.

## Licensing Note

The solution code in eight\_queens\_sim\_anneal.py is copied wholesale from
[Simulated Annealing and the Eight Queen Problem](https://towardsdatascience.com/simulated-annealing-and-the-eight-queen-problem-10f737edbb7e),
a Medium article by [Sebastián Gerard Aguilar Kleimann](https://medium.com/@sgerardak).
No license was included with the code. Including it, a mere 29 lines, in a
self-educational exercise seemed allow based on the article's tone. Those
wishing to include it in a larger project or put it to a commercial use should
contact the original author to work out permission and licensing issues.

## Results of Time Trials

The kata suggests comparing the performance of different algorithms. In
this project I implemented a depth-first search, a breadth-first search, a
simulated annealing algorithm (using the `mlrose` module's implementation), a
minimum-conflicts algorithm, a genetic algorithm, and a brute-force approach.
The time trials run by the included program `time_trials.py` yielded these
results:

* **Depth-first search time:** 777.906 μs
* **Breadth-first search time:** 626.844 μs
* **Simulated annealing algorithm time:** 63.059 ms
* **Minimum-conflicts algorithm time:** 1.702 ms
* **Genetic algorithm time:** 382.146 ms
* **Brute force approach time:** 3.115 seconds

For all the time taken implementing more complex algorithms, apparently the
breadth-first search is fastest.
