import timeit
from functools import reduce
from typing import Dict, Iterable, List, Tuple

from collections import namedtuple, defaultdict

Point = namedtuple('Point', ("x", "y"))

class Line:
    def __init__(self, endpoints: List[Point]) -> None:
        assert len(endpoints) == 2
        self._endpoints = endpoints
    
    def points(self) -> Iterable[Point]:
        left, right = sorted(self._endpoints, key=lambda p: p.x)

        dist = max(abs(right.x - left.x), abs(right.y - left.y))
        x_diff = 0 if left.x == right.x else 1
        y_diff = 0 if left.y == right.y else 1 if left.y < right.y else -1

        # min_x, max_x = sorted([p.x for p in self._endpoints])
        # min_y, max_y = sorted([p.y for p in self._endpoints])
        # if self._endpoints[0].x == self._endpoints[1].x:
        #     for y in range(min_y, max_y + 1):
        #         yield Point(x=self._endpoints[0].x, y=y)
        # elif self._endpoints[0].y == self._endpoints[1].y:
        #     for x in range(min_x, max_x + 1):
        #         yield Point(x=x, y=self._endpoints[0].y)
        # else:
        for diff in range(dist + 1):
            yield Point(x=left.x + diff * x_diff, y=left.y + y_diff * + diff)
    
    @property
    def straight(self):
        return self._endpoints[0].x == self._endpoints[1].x or self._endpoints[0].y == self._endpoints[1].y

def main():
    with open('input.txt') as f:
        lines = [
            Line([
                Point(*[int(c) for c in point.split(',')])
                for point in line.split('->')
            ])
            for line in f.readlines()
        ]
    
    straight_matrix = draw_lines([line for line in lines if line.straight])
    
    print('Part1:')
    for y in range(10):
        row_values = [straight_matrix[Point(x=x, y=y)] for x in range(10)]
        drawn = ''.join(['.' if not val else str(val) for val in row_values])
        print(f"  {drawn}")
    
    overlaps = len([item for item in straight_matrix.values() if item > 1])
    print(f"  Overlaps: {overlaps}")

    full_matrix = draw_lines(lines)
    
    print('Part2:')
    for y in range(10):
        row_values = [full_matrix[Point(x=x, y=y)] for x in range(10)]
        drawn = ''.join(['.' if not val else str(val) for val in row_values])
        print(f"  {drawn}")
    
    overlaps = len([item for item in full_matrix.values() if item > 1])
    print(f"  Overlaps: {overlaps}")


def draw_lines(lines: List[Line]) -> Dict[Point, int]:
    matrix = defaultdict(lambda: 0)
    for line in lines:
        for point in line.points():
            matrix[point] += 1
    return matrix

if __name__ == '__main__':
    #timeit.timeit('main()', number=5)
    main()
