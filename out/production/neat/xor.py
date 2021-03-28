import random

def generate(n: int, file_path: str):

    with open(file_path, 'w') as f:
        for i in range(n):
            bit_1 = bit()
            bit_2 = bit()
            ans = bit_1 ^ bit_2
            f.write(f'{bit_1} {bit_2} {ans}\n')

def bit():
    return 1 if random.uniform(0, 1) > 0.5 else 0


if __name__ == '__main__':
    generate(10000, '/Users/max/IdeaProjects/neat/data/xor.txt')
