from typing import Optional

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

opening_closing_mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def get_first_incorrect_closing_character(line: str) -> Optional[str]:
    # returning the first incorrect closing character - None if line is not corrupted
    chars_stack = []

    for char in line:
        if char in opening_closing_mapping:
            chars_stack.append(char)
        else:
            if char == opening_closing_mapping[chars_stack[-1]]:
                chars_stack.pop()
            else:
                return char

    return None


def line_is_corrupted(line: str) -> bool:
    return get_first_incorrect_closing_character(line) is not None


def main():
    incorrect_closing_characters = []
    with open('input.txt', 'r') as f:
        for line in f:
            if line_is_corrupted(line.rstrip()):
                incorrect_closing_characters.append(get_first_incorrect_closing_character(line.rstrip()))

    print('score', sum([SCORES[closing_char] for closing_char in incorrect_closing_characters]))


if __name__ == '__main__':
    main()
