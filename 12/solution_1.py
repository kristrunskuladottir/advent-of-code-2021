from collections import defaultdict
from typing import List


def construct_ways(cave_map: List[List[str]], unfinished_ways: List[List[str]]) -> List[List[str]]:
    finished_ways = []

    while len(unfinished_ways) > 0:
        way = unfinished_ways.pop()
        next_caves = cave_map[way[-1]]

        for next_cave in next_caves:
            new_way = way.copy()
            if next_cave == 'end':
                new_way.append('end')
                finished_ways.append(new_way)
            elif next_cave.lower() != next_cave:
                new_way.append(next_cave)
                unfinished_ways.append(new_way)
            elif next_cave.lower() == next_cave and next_cave not in new_way:
                new_way.append(next_cave)
                unfinished_ways.append(new_way)

    return finished_ways


cave_map = defaultdict(list)

with open('input.txt', 'r') as f:
    for line in f:
        beginning, end = line.rstrip().split('-')
        if beginning != 'start' and end != 'end':
            cave_map[end].append(beginning)
        if end != 'start' and beginning != 'end':
            cave_map[beginning].append(end)

ways = construct_ways(cave_map, [['start']])

print(len(ways), 'finished ways')
