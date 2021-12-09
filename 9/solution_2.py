from typing import Dict, List, Set, Tuple
from solution_1 import get_low_points


def check_for_basin(basin: Set[Tuple[int, int]], height_map: List[List[int]], new_point: Tuple[int, int], low_point: Tuple[int, int]) -> bool:
    x, y = new_point
    height = height_map[y][x]

    check_left = x != 0
    check_right = x < len(height_map[0]) - 1
    check_up = y != 0
    check_down = y < len(height_map) - 1

    if check_left:
        if height_map[y][x - 1] < 9 and height_map[y][x - 1] > height:
            basin.add((x - 1, y))
            check_for_basin(basin, height_map, (x - 1, y), low_point)
    if check_right:
        if height_map[y][x + 1] < 9 and height_map[y][x + 1] > height:
            basin.add((x + 1, y))
            check_for_basin(basin, height_map, (x + 1, y), low_point)
    if check_down:
        if height_map[y + 1][x] < 9 and height_map[y + 1][x] > height:
            basin.add((x, y + 1))
            check_for_basin(basin, height_map, (x, y + 1), low_point)
    if check_up:
        if height_map[y - 1][x] < 9 and height_map[y - 1][x] > height:
            basin.add((x, y - 1))
            check_for_basin(basin, height_map, (x, y - 1), low_point)

    return basin


def get_basins(height_map: List[List[int]]) -> List[int]:
    basins = {}
    low_points = get_low_points(height_map)
    for low_point, height in low_points.items():
        basins[low_point] = check_for_basin({low_point}, height_map, low_point, low_point)

    return basins


def main():
    height_map = []

    with open('input.txt', 'r') as f:
        for line in f:
            heights = list(line.rstrip())
            height_map.append([int(height) for height in heights])

    basins = get_basins(height_map)
    basin_sizes = [len(basin) for basin in basins.values()]

    basin_sizes.sort(reverse=True)
    print('basin sizes multiplied', basin_sizes[0] * basin_sizes[1] * basin_sizes[2])


if __name__ == '__main__':
    main()
