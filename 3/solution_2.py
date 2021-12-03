from typing import List

from solution_1 import convert_binary_to_integer, find_most_common_bytes, flip_binary_number


def get_oxygen_rating(binary_numbers: List[str]) -> str:
    i = 0

    while len(binary_numbers) > 0 and i < len(binary_numbers[0]):
        most_common_bytes = find_most_common_bytes(binary_numbers, include_dashes=True)
        most_common_byte = most_common_bytes[i] if most_common_bytes[i] != '-' else '1'

        binary_numbers = [binary_number for binary_number in binary_numbers if binary_number[i] == most_common_byte]

        i += 1

        if len(binary_numbers) == 1:
            return binary_numbers[0]

    raise ValueError('Found no oxygen rating')


def get_co2_rating(binary_numbers: List[str]) -> str:
    i = 0

    while len(binary_numbers) > 0 and i < len(binary_numbers[0]):
        most_common_bytes = find_most_common_bytes(binary_numbers, include_dashes=True)
        least_common_bytes = flip_binary_number(most_common_bytes, include_dashes=True)

        least_common_byte = least_common_bytes[i] if least_common_bytes[i] != '-' else '0'

        binary_numbers = [binary_number for binary_number in binary_numbers if binary_number[i] == least_common_byte]

        i += 1

        if len(binary_numbers) == 1:
            return binary_numbers[0]

    raise ValueError('Found no co2 rating')


def main():
    with open('input.txt', 'r') as f:
        binary_numbers = [line.rstrip() for line in f]

    oxygen_rating = get_oxygen_rating(binary_numbers)
    oxygen_rating_as_integer = convert_binary_to_integer(oxygen_rating)

    co2_rating = get_co2_rating(binary_numbers)
    co2_rating_as_integer = convert_binary_to_integer(co2_rating)

    life_support_rating = oxygen_rating_as_integer * co2_rating_as_integer
    print('life_support_rating', life_support_rating)

if __name__ == '__main__':
    main()
