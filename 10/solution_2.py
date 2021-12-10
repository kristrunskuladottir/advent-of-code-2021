from solution_1 import line_is_corrupted, opening_closing_mapping

SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def complete_line(line: str) -> str:
    # we can assume here the line is not corrupt
    chars_stack = []

    for char in line:
        if char in opening_closing_mapping:
            chars_stack.append(char)
        else:
            if opening_closing_mapping[chars_stack[-1]] == char:
                chars_stack.pop()
            else:
                raise ValueError('These lines were not supposed to be corrupted')

    closing_sequence = ''

    i = len(chars_stack) - 1
    while i >= 0:
        closing_sequence += opening_closing_mapping[chars_stack[i]]
        i -= 1

    return closing_sequence


def main():
    incomplete_lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            if not line_is_corrupted(line.rstrip()):
                incomplete_lines.append(line.rstrip())

    completing_sequences = []
    for incomplete_line in incomplete_lines:
        completing_sequence = complete_line(incomplete_line)
        completing_sequences.append(completing_sequence)

    sequence_scores = []
    for completing_sequence in completing_sequences:
        score = 0
        for char in completing_sequence:
            score *= 5
            score += SCORES[char]
        sequence_scores.append(score)

    sequence_scores.sort(reverse=False)

    print('middle score', sequence_scores[int(len(sequence_scores) / 2)])


if __name__ == '__main__':
    main()
