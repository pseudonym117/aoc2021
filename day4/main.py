import timeit
from functools import reduce
from typing import Iterable, List

diagonals = False

class Board:
    def __init__(self, board, name) -> None:
        assert len(board) == 5
        for row in board:
            assert len(row) == 5
        self._board = board
        self.name = name

        self._test_lines = list(self._board)
        for i in range(5):
            self._test_lines.append([row[i] for row in self._board])

        if diagonals:
            self._test_lines.append([self._board[i][i] for i in range(5)])
            self._test_lines.append([self._board[i][4 - i] for i in range(5)])

    def has_won(self, picks: List[int]) -> bool:
        for test_line in self._test_lines:
            if reduce(lambda a, b: a and b, map(lambda val: val in picks, test_line)):
                return True
        return False
    
    def sum_unmarked(self, picks: List[int]) -> int:
        cur = 0
        for row in self._board:
            cur += sum([val for val in row if val not in picks])
        return cur

def main():
    with open('input.txt') as f:
        pick_order = [int(pick) for pick in f.readline().split(',')]
        remaining = f.readlines()
    
    boards = list(build_boards(remaining))

    part1_done = False
    for ind in range(len(pick_order)):
        picks_so_far = pick_order[:ind + 1]

        winners = [board for board in boards if board.has_won(picks_so_far)]

        if winners:
            if not part1_done:
                print("part1:")
                print(f"  {len(winners)} boards won on pick {ind}")
                for winner in winners:
                    print(f"    {winner.name}: sum: {winner.sum_unmarked(picks_so_far)}, score: {winner.sum_unmarked(picks_so_far) * picks_so_far[-1]}")
                part1_done = True
            
            if len(winners) == len(boards):
                print("part2:")
                print(f"  {len(winners)} boards won last on pick {ind}")
                for winner in winners:
                    print(f"    {winner.name}: sum: {winner.sum_unmarked(picks_so_far)}, score: {winner.sum_unmarked(picks_so_far) * picks_so_far[-1]}")
                break
            else:
                for winner in winners:
                    boards.remove(winner)
            
            

def build_boards(lines: List[str]) -> Iterable[Board]:
    buffer = []
    board_num = 0
    for line in lines:
        if not line.strip():
            if buffer:
                yield Board(buffer, f"board_{board_num}")
                buffer = []
                board_num += 1
        else:
            buffer.append([int(val) for val in line.split()])
    if buffer:
        yield Board(buffer, f"board_{board_num}")

if __name__ == '__main__':
    #timeit.timeit('main()', number=5)
    main()
