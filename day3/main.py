import timeit
from functools import reduce

def main():
    with open('input.txt') as f:
        inputs = [[int(c) for c in line.strip()] for line in f.readlines()]

    counts = reduce(iter_add, inputs)
    gamma_rate_arr = [1 if c > len(inputs) / 2 else 0 for c in counts]
    
    gamma_rate = int(''.join(map(str, gamma_rate_arr)), base=2)
    epsilon_rate = (~gamma_rate) & int('1' * len(inputs[0]), base=2)

    power_consumption = gamma_rate * epsilon_rate

    print(f"part1: gamma: {gamma_rate}, epsilon: {epsilon_rate}, power_consumption: {power_consumption}")

    o2_filtered = inputs
    co2_filtered = inputs
    for index in range(len(inputs[0])):
        if len(o2_filtered) > 1:
            o2_counts = reduce(iter_add, o2_filtered)
            o2_most_common = [1 if c >= len(o2_filtered) / 2 else 0 for c in o2_counts]
            o2_target = o2_most_common[index]

            o2_filtered = list(filter(lambda line: line[index] == o2_target, o2_filtered))
        if len(co2_filtered) > 1:
            co2_counts = reduce(iter_add, co2_filtered)
            co2_least_common = [0 if c >= len(co2_filtered) / 2 else 1 for c in co2_counts]
            co2_target = co2_least_common[index]

            co2_filtered = list(filter(lambda line: line[index] == co2_target, co2_filtered))
    
    assert len(o2_filtered) == 1
    assert len(co2_filtered) == 1

    o2_rating = int(''.join(map(str, o2_filtered[0])), base=2)
    co2_rating = int(''.join(map(str, co2_filtered[0])), base=2)

    print(f"o2 rating: {o2_rating}, co2 rating: {co2_rating}, life support rating: {o2_rating * co2_rating}")


def iter_add(iter1, iter2):
    return map(sum, zip(iter1, iter2))

if __name__ == '__main__':
    #timeit.timeit('main()', number=5)
    main()
