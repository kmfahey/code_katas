#!/usr/bin/python3

import pprint
import mlrose
import numpy as numpy
import random


from eight_queens_util import free_queens_kmf as free_queens


# This code copied wholesale from "Simulated Annealing and the Eight Queen Problem"
# <https://towardsdatascience.com/simulated-annealing-and-the-eight-queen-problem-10f737edbb7e>,
# a Medium article by Sebastián Gerard Aguilar Kleimann <https://medium.com/@sgerardak>.
# No license was included with the code. Including it, a mere 29 lines, in a
# self-educational exercise seemed allowed based on the article's tone. Those
# wishing to include it in a larger project or put it to a commercial use should
# contact the original author to work out permission and licensing issues.


__all__ = "eight_queens_sim_anneal", "free_queens_sgak"


# This objective function has been replaced with
# eight_queens_util.free_queens_kmf(), which in a parallel test of 10000 random
# position arrays, consistently returned a number of free queens that was less
# than or equal to free_queens_sgak()'s measurement, and never returned a value
# that was greater than free_queens_sgak()'s measurement. Between the two I
# think it's this function that has the bug.

# # Defining the objective function
# def free_queens_sgak(position):
# 
#     # We start the count
#     no_attack_on_j = 0
#     queen_not_attacking = 0
# 
#     # Compare for each pair of queens
#     for i in range(len(position) - 1):
# 
#         no_attack_on_j = 0
# 
#         for j in range(i + 1, len(position)):
# 
#             # Check if there is any diagonal or horizontal attack. Iterative
#             # process for each column.
#             if position[j] != position[i] \
#                     and position[j] != position[i] + (j - i) \
#                     and position[j] != position[i] - (j - i):
# 
#                 # If there isn't any attack on the evaluated column. The count
#                 # is increased by one. This counter is only used as a reference.
#                 no_attack_on_j += 1
# 
#                 # If there is no attack on all the columns. The general counter
#                 # is increased by one. This counter indicates the number of
#                 # queens that are correctly positioned.
#                 if no_attack_on_j == len(position) - 1 - i:
#                     queen_not_attacking += 1
# 
#     # The return number is the number of queens not attacking each
#     # other. If this number is 7 we add 1 cause it means the last
#     # queen is also free of attack.
#     if queen_not_attacking == 7:
#         queen_not_attacking += 1
# 
#     return queen_not_attacking


def eight_queens_sim_anneal():
    best_objective = 0.0

    while best_objective != 8.0:
        # Assign the objective function to "CustomFitness" method.
        objective= mlrose.CustomFitness(free_queens)

        #Description of the problem
        problem = mlrose.DiscreteOpt(length=8, fitness_fn=objective, maximize=True, max_val=8)

        # Define decay schedule
        T = mlrose.ExpDecay()

        # Define initial state
        initial_position = numpy.array(range(8))
        random.shuffle(initial_position)

        # Solve problem using simulated annealing
        best_position, best_objective = mlrose.simulated_annealing(problem=problem, schedule=T, max_attempts=500, max_iters=5000,
                                                                   init_state=initial_position)

    return(best_position)
