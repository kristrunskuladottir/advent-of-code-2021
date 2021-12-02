from typing import List, Tuple


def get_position(commands: List[Tuple[str, int]]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0

    for direction, steps in commands:
        if direction == 'forward':
            horizontal += steps

        if direction == 'down':
            depth += steps

        if direction == 'up':
            depth -= steps

    return horizontal, depth


def main():
    commands = []
    with open('input.txt', 'r') as f:
        for line in f:
            command = line.rstrip().split()
            commands.append((command[0], int(command[1])))

    horizontal, depth = get_position(commands)
    print('product', horizontal * depth)


if __name__ == '__main__':
    main()
