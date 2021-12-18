def main():
    input_file = "input.txt"

    with open(input_file, "r") as f:
        readings = [int(depth) for depth in f.readlines()]

    changes = 0
    for (prev, curr) in zip(readings[:-1], readings[1:]):
        if curr > prev:
            changes += 1
    print(f"part1: changes: {changes}")

    changes = 0
    window_measurements = list(
        map(sum, zip(readings[:-2], readings[1:-1], readings[2:]))
    )
    for (prev, curr) in zip(window_measurements[:-1], window_measurements[1:]):
        if curr > prev:
            changes += 1
    print(f"part2: changes: {changes}")


if __name__ == "__main__":
    main()
