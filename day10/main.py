import timeit
from functools import reduce
from statistics import median

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    closer = {
        '<': '>',
        '(': ')',
        '[': ']',
        '{': '}',
    }
    corrupt_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    incomplete_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    corrupted_running = 0
    incomplete_running = []
    for line in lines:
        stack = []
        corrupt = False
        for c in line.strip():
            if c in '<([{':
                stack.append(c)
            elif c in '>)]}':
                last_char = stack.pop()
                expected = closer[last_char]
                if c != expected:
                    # error / answer here
                    # print(f'bad closing tag: expected "{expected}", but found "{c}" instead.')
                    corrupt = True
                    corrupted_running += corrupt_score[c]
                    break
            else:
                assert False
        if not corrupt:
            missing = ''.join(map(closer.get, reversed(stack)))
            if missing:
                score = reduce(lambda a, b: a * 5 + b, map(lambda x: incomplete_score[x], missing), 0)
                #print(f"missing characters: {missing}: {score}")

                incomplete_running.append(score)

    print(f"part1: score: {corrupted_running}")
    print(f"part2: winner: {median(incomplete_running)}")


if __name__ == '__main__':
    #timeit.timeit('main()', number=1)
    main()
