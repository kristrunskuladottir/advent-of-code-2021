from itertools import product
from typing import List, Set, Tuple


def get_neighbours(point: Tuple[int, int], energy_levels_all: List[List[int]]) -> Tuple[Tuple[int, int], ...]:
    x_range = [i for i in [point[0] - 1, point[0], point[0] + 1] if i >= 0 and i < len(energy_levels_all[0])]
    y_range = [j for j in [point[1] - 1, point[1], point[1] + 1] if j >= 0 and j < len(energy_levels_all)]

    neighbours = list(product(x_range, y_range))
    neighbours.remove(point)

    return neighbours


def check_for_neighbour_flashes(x: int, y: int, energy_levels_all: List[List[int]], flashes: Set[Tuple[int, int]]):
    for neighbour_x, neighbour_y in get_neighbours((x, y), energy_levels_all):
        if (neighbour_x, neighbour_y) in flashes:
            continue

        energy_levels_all[neighbour_y][neighbour_x] += 1

        if energy_levels_all[neighbour_y][neighbour_x] == 10:
            flashes.add((neighbour_x, neighbour_y))
            flashes = check_for_neighbour_flashes(neighbour_x, neighbour_y, energy_levels_all, flashes)

    return flashes


def main():
    energy_levels_all = []

    with open('input.txt') as f:
        for line in f:
            energy_levels_all.append([int(energy_level) for energy_level in list(line.rstrip())])

    total_flash_count = 0
    step = 1
    while step <= 100:
        # lets start with increasing all the energy levels by 1
        flashes = set()
        for y in range(len(energy_levels_all)):
            for x in range(len(energy_levels_all[y])):
                energy_levels_all[y][x] += 1
                if energy_levels_all[y][x] == 10:
                    flashes.add((x, y))

        new_flashes = flashes.copy()

        # now we check the butterfly effect of the flashes
        for x, y in flashes:
            new_flashes = check_for_neighbour_flashes(x, y, energy_levels_all, new_flashes)

        # reset all flashed octopus
        for y in range(len(energy_levels_all)):
            for x in range(len(energy_levels_all[y])):
                if energy_levels_all[y][x] == 10:
                    energy_levels_all[y][x] = 0

        total_flash_count += len(new_flashes)
        step += 1

    print('total_flash_count', total_flash_count)


if __name__ == '__main__':
    main()
