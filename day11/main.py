import timeit
from functools import reduce
from statistics import median

def main():
    with open('input.txt') as f:
        octopi = [[int(c) for c in line.strip()] for line in f.readlines()]
    total_octopi = sum(map(len, octopi))
    
    final_steps = 100
    step = 0
    flashed = 0

    complete_flashed = None

    while complete_flashed is None:
        step += 1
        step_flashed = 0
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                step_flashed += increase_and_flash(octopi, x, y)
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                if octopi[y][x] > 9:
                    octopi[y][x] = 0
        
        
        if step_flashed == total_octopi:
            complete_flashed = step

        if step <= final_steps:
            flashed += step_flashed
    
        #print('\n'.join([''.join([str(o) for o in row]) for row in octopi]))
        #print()

    print(f"Part1: flashed: {flashed}")
    print(f"Part2: first total flash @ step {complete_flashed}")
    

def increase_and_flash(octopi, x, y) -> int:
    if x < 0 or y < 0:
        return 0
    if y >= len(octopi) or x >= len(octopi[y]):
        return 0
    octopi[y][x] += 1
    if octopi[y][x] == 10:
        flashed = 1
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx or dy:
                    flashed += increase_and_flash(octopi, x + dx, y + dy)
        return flashed
    return 0
    

if __name__ == '__main__':
    #timeit.timeit('main()', number=1)
    main()
