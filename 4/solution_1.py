from typing import List

from bingo import BingoBoard


def create_bingo_boards_from_input(file: List[str]) -> List[BingoBoard]:
    boards_input = []
    for i, line in enumerate(file):
        row = line.split()
        row = [int(field) for field in row]
        if row == []:
            # starting a new board
            boards_input.append([])
        else:
            boards_input[-1].append(row)

    bingo_boards = []
    for board_input in boards_input:
        bingo_boards.append(BingoBoard.create_bingo_board_from_input(board_input))

    return bingo_boards


def main():
    with open('input.txt', 'r') as f:
        numbers_drawn = f.readline().rstrip().split(',')
        numbers_drawn = [int(number) for number in numbers_drawn]

        bingo_boards = create_bingo_boards_from_input([line.rstrip() for line in f])

    winning_board = None

    for number in numbers_drawn:
        if winning_board is not None:
            break

        for board in bingo_boards:
            if board.is_match(number):
                if board.is_bingo():
                    board.i_won(number)
                    winning_board = board
                    break

    print('score', winning_board.get_score())


if __name__ == '__main__':
    main()
