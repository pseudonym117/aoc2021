import timeit
from types import FunctionType
from typing import List
from collections import defaultdict


def main():
    with open('input.txt') as f:
        inputs = [line.split('|') for line in f.readlines()]
   
    patterns = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }

    simple_digits = 0
    for full, disp in inputs:
        split = disp.strip().split(' ')
        for rep in split:
            match len(rep):
                case 2 | 3 | 4 | 7:
                    simple_digits += 1
    
    print(f"part1: simple digits: {simple_digits}")

    total = 0
    for full, disp in inputs:
        possibilities = {}

        by_len = defaultdict(lambda: [])
        split = full.strip().split(' ')

        for num in split:
            by_len[len(num)].append(sorted(num))
        
        one = by_len[2][0]
        seven = by_len[3][0]
        diff = ''.join([c for c in seven if c not in one])

        possibilities['a'] = diff
        # solved: a
        possibilities['c'] = one
        possibilities['f'] = one

        four = by_len[4][0]

        possibilities['b'] = [c for c in four if c not in one]
        possibilities['d'] = [c for c in four if c not in one]

        zero_six_nine = by_len[6]
        for possible_b in possibilities['b']:
            if len([val for val in zero_six_nine if possible_b in val]) == 3:
                possibilities['d'] = [c for c in possibilities['b'] if c != possible_b][0]
                possibilities['b'] = possible_b
                break
        # solved: a, b, d

        two_three_five = by_len[5]
        two_three_five_less_solved = [
            [c for c in num if c not in [possibilities[c] for c in 'abd']]
            for num in two_three_five
        ]
        
        char_count = defaultdict(lambda: 0)
        for c in 'abcdefg':
            char_count[c] += len([num for num in two_three_five_less_solved if c in num])
        possibilities['g'] = [char for char, count in char_count.items() if count == 3][0]
        possibilities['e'] = [char for char, count in char_count.items() if count == 1][0]

        # solved: a, b, d, e, g

        zero_six_nine_less_solved = [
            [c for c in num if c not in [possibilities[c] for c in 'abdeg']]
            for num in zero_six_nine
        ]

        char_count = defaultdict(lambda: 0)
        for c in 'abcdefg':
            char_count[c] += len([num for num in zero_six_nine_less_solved if c in num])

        possibilities['c'] = [char for char, count in char_count.items() if count == 2][0]
        possibilities['f'] = [char for char, count in char_count.items() if count == 3][0]

        # solved: all

        reverse_lookup = {value: key for key, value in possibilities.items()}

        final_val_str = ''
        for num in disp.strip().split(' '):
            translated = [reverse_lookup[c] for c in num]
            sorted_num = ''.join(sorted(translated))
            value = patterns[sorted_num.strip()]
            final_val_str += value
        
        final_val = int(final_val_str)
        total += final_val
    
    print(f"part2: total: {total}")


if __name__ == '__main__':
    #timeit.timeit('main()', number=1)
    main()
