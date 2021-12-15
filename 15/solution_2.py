from typing import List
from solution_1 import dijkstra, RiskLevels


def multiply_map(multiplier: int, risk_levels: List[List[int]]) -> List[List[int]]:
    new_map = []
    for i in range(multiplier * len(risk_levels)):
        new_row = [0 for j in range(multiplier * len(risk_levels[0]))]
        new_map.append(new_row)

    for y in range(len(new_map)):
        for x in range(len(new_map[0])):
            i = 0
            j = 0

            new_x = x
            while new_x >= len(risk_levels[0]):
                new_x -= len(risk_levels[0])
                i += 1

            new_y = y
            while new_y >= len(risk_levels):
                new_y -= len(risk_levels)
                j += 1

            new_value = risk_levels[new_y][new_x] + (i * 1) + (j * 1)
            if new_value > 9:
                new_value -= 9

            new_map[y][x] = new_value

    return new_map


def main() -> None:
    risk_levels = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = list(line.rstrip())
            risk_levels.append([int(risk) for risk in line])

    risk_levels = multiply_map(5, risk_levels)
    with open('multiplied.json', 'w+') as f:
        f.write(str(risk_levels))
    risk_levels = RiskLevels.create(risk_levels)
    shortest_way_cost = dijkstra(risk_levels)
    print('total risk', shortest_way_cost)


if __name__ == '__main__':
    main()
