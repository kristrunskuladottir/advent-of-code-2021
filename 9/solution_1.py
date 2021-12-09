from typing import Dict, List, Tuple


def get_low_points(height_map: List[List[int]]) -> Dict[Tuple, int]:
    low_points: Dict[Tuple, int] = {}
    for x in range(len(height_map[0])):
        for y in range(len(height_map)):
            height = height_map[y][x]

            check_left = x != 0
            check_right = x < len(height_map[0]) - 1
            check_up = y != 0
            check_down = y < len(height_map) - 1

            is_low_point = True

            if check_left and height >= height_map[y][x - 1]:
                is_low_point = False
            if check_right and height >= height_map[y][x + 1]:
                is_low_point = False
            if check_down and height >= height_map[y + 1][x]:
                is_low_point = False
            if check_up and height >= height_map[y - 1][x]:
                is_low_point = False

            if is_low_point:
                low_points[(x, y)] = height

    return low_points


def main():
    height_map = []

    with open('input.txt', 'r') as f:
        for line in f:
            heights = list(line.rstrip())
            height_map.append([int(height) for height in heights])

    low_points = get_low_points(height_map)

    print('risk level', sum(low_points.values()) + len(low_points.values()))


if __name__ == '__main__':
    main()
