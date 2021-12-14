from collections import defaultdict
import operator
from typing import Dict, Tuple


def parse_input(filename: str) -> Tuple[str, Dict[str, str]]:
    pair_insertion_rules = {}

    with open(filename, 'r') as f:
        polymer_template = f.readline().rstrip()

        for line in f:
            if line.rstrip() == '':
                continue
            line = line.rstrip().split(' -> ')
            pair_insertion_rules[line[0]] = line[1]

    return polymer_template, pair_insertion_rules


def apply_rules(steps: int, polymer_template: str, pair_insertion_rules: Dict[str, str]) -> str:
    step = 0

    while step < steps:
        i = 0
        while i < len(polymer_template) - 1:
            substring = polymer_template[i:i + 2]
            if substring in pair_insertion_rules:
                polymer_template = polymer_template[0:i + 1] + pair_insertion_rules[substring] + polymer_template[i + 1:]
                i += 1
            i += 1

        step += 1

    return polymer_template


def main() -> None:

    polymer_template, pair_insertion_rules = parse_input('input.txt')
    polymer_template = apply_rules(10, polymer_template, pair_insertion_rules)

    occurrences_map = defaultdict(int)
    for i in polymer_template:
        occurrences_map[i] += 1

    most_common_element = max(occurrences_map.items(), key=operator.itemgetter(1))[0]
    least_common_element = min(occurrences_map.items(), key=operator.itemgetter(1))[0]

    answer = occurrences_map[most_common_element] - occurrences_map[least_common_element]
    print('answer', answer)


if __name__ == '__main__':
    main()
