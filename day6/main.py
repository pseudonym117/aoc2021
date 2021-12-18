from collections import defaultdict
import timeit
from functools import reduce
from typing import Dict, Iterable, List, Tuple


def main():
    with open('input.txt') as f:
        fish = [int(c) for c in f.readline().split(',')]
    
    counts = defaultdict(lambda: 0)
    for f in fish:
        counts[f] += 1

    for round in range(256):
        next_stage = defaultdict(lambda: 0)
        for i in range(9):
            if i == 0:
                next_stage[6] += counts[i]
                next_stage[8] += counts[i]
            else:
                next_stage[i-1] += counts[i]
        
        counts = next_stage

        if round == 79:
            print(f'Part1: fish after 80 rounds: {sum(counts.values())} ({counts})')

    print(f'Part2: fish after 256 rounds: {sum(counts.values())} ({counts})')


if __name__ == '__main__':
    #timeit.timeit('main()', number=5)
    main()
