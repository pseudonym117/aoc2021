
def main():
    with open('input.txt') as f:
        inputs = [line.split() for line in f.readlines()]

    pos = (0, 0) # horiz, depth

    for cmd, amount in inputs:
        amount = int(amount)

        match cmd:
            case 'forward':
                pos = (pos[0] + amount, pos[1])
            case 'down':
                pos = (pos[0], pos[1] + amount)
            case 'up': 
                pos = (pos[0], pos[1] - amount)
            case _: print(f'invalid direction: {cmd}')
    
    print(f'final coord: {pos}')
    print(f'answer 1: {pos[0] * pos[1]}')

    pos = (0, 0, 0) # horiz, depth, aim

    for cmd, amount in inputs:
        amount = int(amount)

        match cmd:
            case 'forward':
                pos = (pos[0] + amount, pos[1] + pos[2] * amount, pos[2])
            case 'down':
                pos = (pos[0], pos[1], pos[2] + amount)
            case 'up': 
                pos = (pos[0], pos[1], pos[2] - amount)
            case _: print(f'invalid direction: {cmd}')

    print(f'final coord: {pos}')
    print(f'answer 2: {pos[0] * pos[1]}')

if __name__ == '__main__':
    main()
