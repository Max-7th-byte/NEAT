from generation.Generation import Generation
from config import number_of_generations


class Evolution:

    def __init__(self, reward_function, solve_task):
        self._reward = reward_function
        self._solve_task = solve_task


    def start_simulation(self, X_train, y_train):
        new_gen = Generation()
        print('Simulation started...')
        i = 0
        while i < number_of_generations:
            prev_gen = new_gen
            new_gen = prev_gen.step(reward_function=self._reward,
                                    solve_task=self._solve_task,
                                    X_train=X_train,
                                    y_train=y_train)
            print(prev_gen.info())
            prev_gen.visualize_species()
            i += 1
