from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BingoField():
    value: int
    crossed: bool


@dataclass
class BingoBoard():
    rows: List[List[BingoField]]
    winning_board: bool = False
    winning_number: Optional[int] = None


    @classmethod
    def create_bingo_board_from_input(cls, input_board: List[List[int]]) -> 'BingoBoard':
        rows = []
        for row in input_board:
            rows.append([BingoField(value=value, crossed=False) for value in row])

        if any(len(row) != 5 for row in rows):
            raise ValueError('Bingo rows should have length 5')
        if len(rows) != 5:
            raise ValueError('There should be 5 bingo rows in a board')

        return cls(rows=rows)

    def is_match(self, number: int) -> bool:
        for row in self.rows:
            for field in row:
                if field.value == number:
                    field.crossed = True
                    return True

        return False

    def get_columns(self) -> List[List[BingoField]]:
        columns = [[], [], [], [], []]
        for row in self.rows:
            for j, value in enumerate(row):
                columns[j].append(value)

        return columns

    def is_bingo(self):
        for row in self.rows:
            if all(field.crossed for field in row):
                return True

        for column in self.get_columns():
            if all(field.crossed for field in column):
                return True

        return False

    def i_won(self, winning_number: int) -> None:
        self.winning_board = True
        self.winning_number = winning_number

    def get_score(self) -> int:
        if not self.winning_board:
            raise ValueError('This is not a winning board')
        if self.winning_number is None:
            raise ValueError('This board is missing the winning number')

        score = 0
        for row in self.rows:
            score += sum(field.value for field in row if not field.crossed)

        return score * self.winning_number
