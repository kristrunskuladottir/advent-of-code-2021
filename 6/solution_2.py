from typing import List


def get_expected_count_of_lantern_fish(fish_stages: List[int], number_of_days: int) -> int:
    new_stages = [0] * 9  # one 0 for each possible stage
    for stage in fish_stages:
        new_stages[stage] += 1

    for day in range(number_of_days):
        old_stages = new_stages.copy()
        new_stages = [0] * 9

        new_stages[8] = old_stages[0]
        new_stages[7] = old_stages[8]
        new_stages[6] = old_stages[0] + old_stages[7]
        new_stages[5] = old_stages[6]
        new_stages[4] = old_stages[5]
        new_stages[3] = old_stages[4]
        new_stages[2] = old_stages[3]
        new_stages[1] = old_stages[2]
        new_stages[0] = old_stages[1]

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
