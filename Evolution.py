import sys

from generation.Generation import Generation
from visual.net import construct
from config import number_of_generations


class Evolution:

    def __init__(self, reward_function, solve_task):
        self._reward = reward_function
        self._solve_task = solve_task


    def start_simulation(self, X_train, y_train, score):
        sys.setrecursionlimit(2500)

        new_gen = Generation()
        print('Simulation started...')
        i = 0
        while i < number_of_generations:
            prev_gen = new_gen
            avg_fitness = prev_gen.step(reward_function=self._reward,
                                        solve_task=self._solve_task,
                                        X_train=X_train,
                                        y_train=y_train)

            org = prev_gen.ready(score)
            if org is not None:
                print('Done!')
                print(org)
                construct(org.genome(), 'The Best', view=True)
                break

            print(prev_gen.info())
            prev_gen.visualize_species()
            new_gen = prev_gen.reproduce(avg_fitness)
            i += 1
