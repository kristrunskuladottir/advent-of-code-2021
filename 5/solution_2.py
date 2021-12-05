from collections import defaultdict

from solution_1 import get_coordinates_from_file


def main():
    coordinates = get_coordinates_from_file('input.txt')

    coordinates_covered_by_lines = defaultdict(int)

    for line in coordinates:
        for coordinate in line.coordinates_covered():
            coordinates_covered_by_lines[coordinate] += 1

    coordinates_with_intersections = [coordinate for coordinate, count in coordinates_covered_by_lines.items() if count > 1]
    print('number of intersections', len(coordinates_with_intersections))


if __name__ == '__main__':
    main()
