from generation.Generation import Generation
# TMP
import random
#

class Evolution:

    def __init__(self, reward_function, solve_task):
        self._reward = reward_function
        self._solve_task = solve_task


    def start_simulation(self):
        prev_gen = None
        new_gen = Generation()
        i = 0
        while i < 3:
            prev_gen = new_gen
            new_gen = prev_gen.step(reward_function=self._reward,
                                    solve_task=self._solve_task,
                                    _input=[0, 1, 1])
            print(prev_gen.info())
            print('-' * 50)
            i += 1


def tmp_reward(ans, **kwargs):
    correct = [kwargs['_input'][0] ^ kwargs['_input'][1], kwargs['_input'][1] ^ kwargs['_input'][2]]
    return random.uniform(1, 2) * 10 if correct == ans else random.uniform(1, 2)


def solve_task_func(predict, **kwargs):
    return predict(kwargs['_input'])


if __name__ == '__main__':
    evolution = Evolution(tmp_reward, solve_task_func)
    evolution.start_simulation()
