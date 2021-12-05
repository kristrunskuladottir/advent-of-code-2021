from collections import defaultdict
from typing import List

from coords import Line


def get_coordinates_from_file(filename: str) -> List[Line]:
    coordinates_input = []
    with open(filename, 'r') as f:
        coordinates_input = f.readlines()
        coordinates_input = [coordinate.rstrip() for coordinate in coordinates_input]

    return [Line.create_from_string(coordinates) for coordinates in coordinates_input]


def main():
    coordinates = get_coordinates_from_file('input.txt')

    coordinates_covered_by_lines = defaultdict(int)

    for line in coordinates:
        if not line.is_horizontal() and not line.is_vertical():
            continue

        for coordinate in line.coordinates_covered():
            coordinates_covered_by_lines[coordinate] += 1

    coordinates_with_intersections = [coordinate for coordinate, count in coordinates_covered_by_lines.items() if count > 1]
    print('number of intersections', len(coordinates_with_intersections))


if __name__ == '__main__':
    main()
