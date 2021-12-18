import timeit
from types import FunctionType
from typing import List
import math
import statistics


def main():
    with open('input.txt') as f:
        crabs_start = [int(c) for c in f.readline().split(',')]
    
    pos = statistics.median(crabs_start)
    value = cost(crabs_start, pos, distance_const)
    
    print(f'Part1: pos: {pos} fuel: {value}')

    ideal = statistics.mean(crabs_start)
    pos_low, pos_high = math.floor(ideal), math.ceil(ideal)
    value_low, value_high = cost(crabs_start, pos_low, distance_linear), cost(crabs_start, pos_high, distance_linear)

    if value_low < value_high:
        pos, value = pos_low, value_low
    else:
        pos, value = pos_high, value_high

    print(f'Part2: pos: {pos} fuel: {value}')

def cost(crabs_start: List[int], target_pos: int, distance_func: FunctionType) -> int | None:
    return sum(map(lambda crab: distance_func(crab, target_pos), crabs_start))

def distance_const(a: int, b: int) -> int:
    return max(a, b) - min(a, b)

def distance_linear(a: int, b: int) -> int:
    return sum(range(distance_const(a, b) + 1))

if __name__ == '__main__':
    #timeit.timeit('main()', number=1)
    main()
