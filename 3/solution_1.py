from math import pow
from typing import List


def convert_binary_to_integer(binary_number: str) -> int:
    result = 0
    for i, byte in enumerate(binary_number):
        result += int(byte) * int(pow(2, len(binary_number) - 1 - i))

    return result


def find_most_common_bytes(binary_numbers: List[str], include_dashes: bool = False) -> str:
    # if include_dashes is True, a dash will be included instead of 0 or 1 if 0 and 1 appeared the same amount
    common_string = ''
    for i in range(len(binary_numbers[0])):
        bytes_list = [int(binary_number[i]) for binary_number in binary_numbers]

        if sum(bytes_list) > len(bytes_list) / 2:
            common_string += '1'
        elif sum(bytes_list) < len(bytes_list) / 2:
            common_string += '0'
        else:
            # if the bytes are equally common we include a dash in that place
            common_string += '-' if include_dashes else '1'

    return common_string


def flip_binary_number(binary_number: str, include_dashes: bool = False) -> str:
    # if include_dashes is True, a dash won't be flipped
    flipped_string = ''
    for i in binary_number:
        if include_dashes:
            flipped_string += '0' if i == '1' else '1' if i == '0' else '-'
        else:
            flipped_string += '0' if i in ('1', '-') else '1'

    return flipped_string


def main():
    with open('input.txt', 'r') as f:
        binary_numbers = [line.rstrip() for line in f]

    gamma_rate = find_most_common_bytes(binary_numbers)
    epsilon_rate = flip_binary_number(gamma_rate)

    gamma_rate_as_integer = convert_binary_to_integer(gamma_rate)
    epsilon_rate_as_integer = convert_binary_to_integer(epsilon_rate)

    print('product', gamma_rate_as_integer * epsilon_rate_as_integer)


if __name__ == '__main__':
    main()
