import sys
from typing import List


def get_increased(numbers: List[int]) -> int:
    increased = 0
    previous_number = sys.maxsize

    for number in numbers:
        if number > previous_number:
            increased += 1

        previous_number = number

    return increased


def main():
    numbers = []

    with open('input.txt', 'r') as f:
        for line in f:
            numbers.append(int(line.rstrip()))

    increased = get_increased(numbers)

    print('increased', increased)


if __name__ == '__main__':
    main()