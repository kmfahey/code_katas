#!/usr/bin/python3

import pprint
import random
import statistics
import operator
import functools


from eight_queens_util import free_queens_kmf as free_queens

from test_eight_queens_min_confl import KNOWN_SOLUTIONS


def gen_rand_positions():
    positions = list(range(8))
    random.shuffle(positions)
    return positions


def gen_population():
    population = list()
    while len(population) < 20:
        new_positions = gen_rand_positions()
        if new_positions not in population:
            population.append(new_positions)
    return population


def mutate_positions(positions):
    mutants = list()
    first_index = random.randint(0, 7)
    for second_index in filter(lambda index: index != first_index, range(8)):
        mutant = positions.copy()
        mutant[first_index], mutant[second_index] = mutant[second_index], mutant[first_index]
        mutants.append(mutant)
    return mutants


def mean_fitness(population):
    return statistics.mean(free_queens(positions) for positions in population)


def mutate_population(population):
    return functools.reduce(operator.concat, (mutate_positions(positions) for positions in population))


def cull_population(population):
    bins = {i: [] for i in range(0, 9)}
    for positions in population:
        bins[free_queens(positions)].append(positions)
    population_by_bin = functools.reduce(operator.concat, [[(bin, positions)
                                                            for positions in bins[bin]]
                                                           for bin in bins.keys()])
    population_by_bin.sort(reverse=True)
    new_population = list(map(operator.itemgetter(1), population_by_bin))
    new_population = new_population[:20]
    return new_population


def filter_for_successes(population):
    return list(filter(lambda positions: free_queens(positions) == 8, population))


class MaxMutationsException(Exception):
    pass


class MaxGenerationsException(Exception):
    pass


def eight_queens_genetic():
    population = gen_population()
    generations = 1

    while generations <= 1000:
        print("generation #", generations)

        cur_popn_mean_fitness = mean_fitness(population)
        print("current population mean fitness:", cur_popn_mean_fitness)

        mutations = 1

        while mutations <= 100: 
            new_population = mutate_population(population)
            new_popn_mean_fitness = mean_fitness(new_population)
            if new_popn_mean_fitness > cur_popn_mean_fitness:
                print("mutation lead to improvement, new population mean fitness:", new_popn_mean_fitness)
                break
            else:
                print("mutation did not improve, insuficient mean fitness was:", new_popn_mean_fitness)
            mutations += 1

        if new_popn_mean_fitness <= cur_popn_mean_fitness:
            if mutations == 101:
                raise MaxMutationsException("hit max mutation attempts, none are improvement")
            else:
                raise RuntimeError("can't happen error: fell off the end of function's inner while loop without obvious reason")

        population = cull_population(new_population)
        print("culled population")

        if successes := filter_for_successes(population):
            return random.choice(successes)

        generations += 1

    if generations >= 1000:
        raise MaxGenerationsException("ran for", generations, "and didn't find solution")
    else:
        raise RuntimeError("can't happen error: fell off the end of function's main while loop without obvious reason")


if __name__ == "__main__":
    positions = None
    trial = 1
    while positions is None:
        print("trial", trial)
        try:
            positions = eight_queens_genetic()
        except MaxMutationsException as exception:
            print(exception.args[0])
        except MaxGenerationsException as exception:
            print(exception.args[0])
        trial += 1
    assert positions in KNOWN_SOLUTIONS
    print("on trial", trial, "found a valid positions list:", positions)
