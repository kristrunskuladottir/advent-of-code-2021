from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Paper():
    rows: List[List[bool]]

    @classmethod
    def create_from_dots(cls, dots: List[Tuple]) -> 'Paper':
        max_x = max([dot[0] for dot in dots])
        max_y = max([dot[1] for dot in dots])

        rows = [[False] * (max_x + 1)] * (max_y + 1)
        x = 0
        y = 0

        rows = []

        while y <= max_y:
            row = []
            x = 0
            while x <= max_x:
                row.append((x, y) in dots)
                x += 1

            rows.append(row)
            y += 1

        return cls(rows=rows)

    def number_of_painted_dots(self) -> int:
        total_number = 0
        for row in self.rows:
            total_number += len([point for point in row if point])
        return total_number

    def fold(self, value: int, by_x: bool = False, by_y: bool = False) -> None:
        if by_x:
            # vertical folding
            for i in range(len(self.rows[0][value + 1:]) + 1):
                if i == 0:
                    # we don't care about the first column
                    continue

                folded_x = value - i

                for y in range(len(self.rows)):
                    self.rows[y][folded_x] = self.rows[y][folded_x] or self.rows[y][value + i]

            new_rows = []
            for row in self.rows:
                new_rows.append(row[0:value])
            self.rows = new_rows

        elif by_y:
            # horizontal folding
            for i, row in enumerate(self.rows[value + 1:]):
                if i == 0:
                    # we don't care about the first row
                    continue

                folded_y = value - 1 - i
                for x in range(len(row)):
                    self.rows[folded_y][x] = self.rows[folded_y][x] or row[x]

            self.rows = self.rows[0:value]
        else:
            raise ValueError('should either be by x or y')

    def print_rows(self) -> None:
        for row in self.rows:
            print(''.join(['.' if not point else '#' for point in row]))


def parse_input(filename: str) -> Tuple[List[Tuple[str, int]], List[Tuple[int, int]]]:
    fold_instructions = []
    dots = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('fold along '):
                instructions = line.strip('fold along ').split('=')
                fold_instructions.append((instructions[0], int(instructions[1])))
            elif line != '':
                dot = line.split(',')
                dots.append((int(dot[0]), int(dot[1])))

    return fold_instructions, dots


def main() -> None:
    fold_instructions, dots = parse_input('input.txt')

    paper = Paper.create_from_dots(dots)

    fold = fold_instructions[0]
    if fold[0] == 'x':
        paper.fold(value=fold[1], by_x=True)
    else:
        paper.fold(value=fold[1], by_y=True)

    print(paper.number_of_painted_dots(), 'paper after fold')


if __name__ == '__main__':
    main()
