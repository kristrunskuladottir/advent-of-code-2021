from collections import defaultdict
from typing import Dict, List


def simulate_lantern_fish(start_stages: List[int], number_of_days: int) -> Dict[int, List[int]]:
    lantern_fish_status_per_day = defaultdict(list)
    lantern_fish_status_per_day[0] = start_stages

    start_day = 1

    while start_day <= number_of_days:
        new_lantern_fish = []
        for stage in lantern_fish_status_per_day[start_day - 1]:
            if stage == 0:
                lantern_fish_status_per_day[start_day].append(6)
                new_lantern_fish.append(8)
            else:
                lantern_fish_status_per_day[start_day].append(stage - 1)

        lantern_fish_status_per_day[start_day].extend(new_lantern_fish)

        start_day += 1

    return lantern_fish_status_per_day


def main():
    with open('test_input.py', 'r') as f:
        input_stages = f.readline().split(',')
        input_stages = [int(stage) for stage in input_stages]

    number_of_days = 80
    lantern_fish_status_per_day = simulate_lantern_fish(input_stages, number_of_days)

    print('number of fish', len(lantern_fish_status_per_day[number_of_days]))


if __name__ == '__main__':
    main()
