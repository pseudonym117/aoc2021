import timeit
from functools import reduce
from statistics import median
from collections import defaultdict, deque
from typing import List

def main():
    with open('input.txt') as f:
        raw_connections = [[c.strip() for c in line.split('-')] for line in f.readlines()]
    
    connections: defaultdict[str, List[str]] = defaultdict(lambda: [])

    for start, end in raw_connections:
        connections[start].append(end)
        connections[end].append(start)
    
    assert 'start' in connections
    assert 'end' in connections
    
    curr_path = deque()

    curr_path.append('start')

    all_paths = dfs_path_find(connections, curr_path, 1)
    #print('\n'.join([','.join(path) for path in all_paths]))

    print(f'Part1: {len(all_paths)} paths')

    with_single_backtrack = dfs_path_find(connections, curr_path, 2)

    print(f'Part2: {len(with_single_backtrack)} paths')
            
def dfs_path_find(connections: dict[str, List[str]], curr_path: deque[str], max_small_cave_visits: int) -> List[List[str]]:
    all_paths = []
    
    # in theory this can be faster by just keeping a running count between executions, but... fuck it
    counts = defaultdict(lambda: 0)
    for node in curr_path:
        if node.islower() and node != 'start':
            counts[node] += 1
    can_revisit_small_cave = len([v for v in counts.values() if v >= max_small_cave_visits]) == 0

    for node in connections[curr_path[-1]]:
        if node == 'end':
            final = list(curr_path)
            final.append(node)
            all_paths.append(final)
        elif not can_revisit_small_cave and node.islower() and node in curr_path:
            continue
        elif node != 'start':
            curr_path.append(node)
            all_paths.extend(dfs_path_find(connections, curr_path, max_small_cave_visits))
            curr_path.pop()

    return all_paths


if __name__ == '__main__':
    #timeit.timeit('main()', number=1)
    main()
