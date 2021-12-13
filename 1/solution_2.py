from typing import List

from solution_1 import get_increased


def get_sliding_windows(numbers: List[int]) -> List[int]:
    windows = []

    #  i = 0 ... len(numbers) - 2
    for i in range(len(numbers) - 2):
        j = 0  # j = 0, 1, 2
        summed = 0
        while j < 3:
            summed += numbers[i + j]
            j += 1

        windows.append(summed)

    return windows


def main():
    numbers = []

    with open('input.txt', 'r') as f:
        for line in f:
            numbers.append(int(line.rstrip()))

    windows = get_sliding_windows(numbers)
    increased = get_increased(windows)
    print('increased', increased)


if __name__ == '__main__':
    main()
