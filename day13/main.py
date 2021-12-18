import timeit
from functools import reduce
from statistics import median
from collections import defaultdict, deque
from typing import List
import re

def main():
    points = set()
    folds = []
    with open('input.txt') as f:
        process_folds = False
        fold_re = re.compile('([xy])=([0-9]+)')
        for line in f.readlines():
            line = line.strip()
            if not process_folds and line:
                x, y = [int(c) for c in line.split(',')]
                points.add((x, y))
            elif process_folds and line:
                match = fold_re.search(line)
                if match:
                    folds.append([match.group(1), int(match.group(2))])
            else:
                process_folds = True

    part1_done = False
    for axis, fold_point in folds:
        next_set = set()
        assert axis == 'x' or axis == 'y'
        if axis == 'x':
            for point in points:
                x, y = point
                if x > fold_point:
                    diff = x - fold_point
                    new_x = fold_point - diff
                    next_set.add((new_x, y))
                elif x < fold_point:
                    next_set.add((x, y))
        else:
            for point in points:
                x, y = point
                if y > fold_point:
                    diff = y - fold_point
                    new_y = fold_point - diff
                    next_set.add((x, new_y))
                elif y < fold_point:
                    next_set.add((x, y))
        points = next_set

        if not part1_done:
            print(f"Part1: {len(points)} total points")
            part1_done = True
    
    xs = [x for x, y in points]
    ys = [y for x, y in points]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    print("Part2:")
    for y in range(miny, maxy + 1):
        print(''.join(['#' if (x, y) in points else '.' for x in range(minx, maxx + 1)]))


if __name__ == '__main__':
    #timeit.timeit('main()', number=1)
    main()
