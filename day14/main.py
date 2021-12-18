import timeit
from functools import reduce
from statistics import median
from collections import defaultdict, deque
from typing import List
import re

def main():
    with open('input.txt') as f:
        lines = f.readlines()

        starting = lines[0].strip()
        insertions = {
            line.split('->')[0].strip(): line.split('->')[1].strip()
            for line in lines[2:]
        }

    pattern = starting
    for step in range(40):
        next_pattern = []
        for a, b in zip(pattern[:-1], pattern[1:]):
            next_pattern.append(a)
            next_pattern.append(insertions[f'{a}{b}'])
        next_pattern.append(pattern[-1])
        pattern = next_pattern

        if step == 9:
            print(f"Part1: {get_answer(pattern)}")
    
    print(f"Part2: {get_answer(pattern)}")

def get_answer(pattern):
    counts = defaultdict(lambda: 0)
    for c in pattern:
        counts[c] += 1
    min_element = min(counts.items(), key=lambda i: i[1])
    max_element = max(counts.items(), key=lambda i: i[1])

    return max_element[1] - min_element[1]

if __name__ == '__main__':
    #timeit.timeit('main()', number=1)
    main()
