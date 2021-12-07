from typing import List


def get_expected_count_of_lantern_fish(fish_stages: List[int], number_of_days: int) -> int:
    new_stages = [0] * 9  # There are 9 possible stages
    for stage in fish_stages:
        new_stages[stage] += 1

    for day in range(number_of_days):
        old_stages = new_stages
        new_stages = [0] * 9

        for i in range(8):
            new_stages[i] = old_stages[i + 1]

        new_stages[8] += old_stages[0]
        new_stages[6] += old_stages[0]

    return sum(new_stages)


def main():
    with open('input.py', 'r') as f:
        input_ages = f.readline().split(',')
        input_ages = [int(age) for age in input_ages]

    number_of_days = 256
    fish_count = get_expected_count_of_lantern_fish(input_ages, number_of_days)

    print('number of fish', fish_count)


if __name__ == '__main__':
    main()
