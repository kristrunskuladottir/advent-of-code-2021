from collections import defaultdict
import operator
from typing import Dict

from solution_1 import parse_input


def get_expected_count_of_letters(steps: int, polymer_template: str, pair_insertion_rules: Dict[str, str]) -> Dict[str, int]:
    letter_count = defaultdict(int)
    new_occurrences = defaultdict(int)
    for i in range(len(polymer_template) - 1):
        new_occurrences[polymer_template[i:i + 2]] += 1

    for i in polymer_template:
        letter_count[i] += 1

    for step in range(steps):
        old_occurrences = new_occurrences.copy()
        new_occurrences = defaultdict(int)
        for rule in old_occurrences.keys():
            insertion = pair_insertion_rules[rule]
            new_occurrences[rule[0] + insertion] += old_occurrences[rule]
            new_occurrences[insertion + rule[1]] += old_occurrences[rule]

            letter_count[insertion] += old_occurrences[rule]

    return letter_count


def main() -> None:
    polymer_template, pair_insertion_rules = parse_input('input.txt')
    occurrences_map = get_expected_count_of_letters(40, polymer_template, pair_insertion_rules)

    most_common_element = max(occurrences_map.items(), key=operator.itemgetter(1))[0]
    least_common_element = min(occurrences_map.items(), key=operator.itemgetter(1))[0]

    print('answer', occurrences_map[most_common_element] - occurrences_map[least_common_element])


if __name__ == '__main__':
    main()
