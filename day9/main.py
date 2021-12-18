import timeit
from types import FunctionType
from typing import List, Tuple
from collections import defaultdict, deque
from functools import reduce


def main():
    with open('input.txt') as f:
        floor_map = [[int(c) for c in line.strip()]  for line in f.readlines()]

    low_points = []    
    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            if is_low_point(floor_map, (x, y)):
                low_points.append((x, y))
    
    risk = sum(map(lambda point: floor_map[point[1]][point[0]] + 1, low_points))

    print(f"Part1: sum of risk: {risk}")

    flood_map = [
        [-1 if h == 9 else 0 for h in row]
        for row in floor_map
    ]

    flood_fill_sections(flood_map)
    # print('\n'.join([''.join(['|' if h == -1 else str(h) for h in row]) for row in flood_map]))

    sections = defaultdict(lambda: [])
    for y in range(len(flood_map)):
        for x in range(len(flood_map[y])):
            label = flood_map[y][x]
            if label != -1 and label != 0:
                sections[label].append((x, y))
    
    print(f"{len(sections)} sections total")

    top_3 = sorted(sections.values(), reverse=True, key=lambda cells: len(cells))[:3]
    solution = reduce(lambda a, b: a * b, map(lambda lst: len(lst), top_3), 1)
    print(f"part2: top3 product: {solution}")

def flood_fill_sections(flood_map):
    label_count = 0
    for y in range(len(flood_map)):
        for x in range(len(flood_map[y])):
            if flood_map[y][x] == 0:
                label_count += 1
                flood_fill_from_node(flood_map, (x, y), label_count)
    
    return label_count
    
def flood_fill_from_node(flood_map, cell, label):
    fill_queue = deque()
    fill_queue.append(cell)
    while fill_queue:
        x, y = fill_queue.pop()

        if flood_map[y][x] == 0:
            flood_map[y][x] = label
            
            if y > 0:
                fill_queue.append((x, y-1))
            if y < len(flood_map) - 1:
                fill_queue.append((x, y+1))
            if x > 0:
                fill_queue.append((x-1, y))
            if x < len(flood_map[y]) - 1:
                fill_queue.append((x+1, y))


def is_low_point(floor_map: List[List[int]], point: Tuple[int, int]):
    x, y = point
    val = floor_map[y][x]
    if y > 0:
        if val >= floor_map[y-1][x]:
            return False
    if y < len(floor_map) - 1:
        if val >= floor_map[y+1][x]:
            return False
    if x > 0:
        if val >= floor_map[y][x-1]:
            return False
    if x < len(floor_map[y]) - 1:
        if val >= floor_map[y][x+1]:
            return False
    return True


if __name__ == '__main__':
    #timeit.timeit('main()', number=1)
    main()
