#!/usr/bin/python3

import random
import statistics
import operator
import functools

from eight_queens_util import free_queens_kmf as free_queens


__all__ = "eight_queens_genetic",


class MaxMutationsException(Exception):
    pass


class MaxGenerationsException(Exception):
    pass


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


def eight_queens_genetic(max_generations=1000, max_mutations=100):
    successes = list()

    def _8_queens_genetic():
        population = gen_population()
        generations = 1

        while generations <= max_generations:
            cur_popn_mean_fitness = mean_fitness(population)
            mutations = 1
            while mutations <= 100:
                new_population = mutate_population(population)
                new_popn_mean_fitness = mean_fitness(new_population)
                if new_popn_mean_fitness > cur_popn_mean_fitness:
                    break
                mutations += 1
            if new_popn_mean_fitness <= cur_popn_mean_fitness and mutations > max_mutations:
                raise MaxMutationsException(f"mutated the population {max_mutations} times, fitness not increasing")

            population = cull_population(new_population)
            successes.extend(filter_for_successes(population))
            if successes:
                return
            generations += 1
            if generations > max_generations:
                raise MaxGenerationsException(f"ran for {max_generations} generations, and couldn't find solution")

    while not len(successes):
        try:
            _8_queens_genetic()
        except (MaxMutationsException, MaxGenerationsException):
            pass

    return random.choice(successes)
