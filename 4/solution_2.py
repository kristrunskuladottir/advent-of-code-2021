from solution_1 import create_bingo_boards_from_input


def main():
    with open('input.txt', 'r') as f:
        numbers_drawn = f.readline().rstrip().split(',')
        numbers_drawn = [int(number) for number in numbers_drawn]

        bingo_boards = create_bingo_boards_from_input([line.rstrip() for line in f])

    winning_row = []

    for number in numbers_drawn:
        for i, board in enumerate(bingo_boards):
            if board.winning_board:
                continue

            if board.is_match(number):
                if board.is_bingo():
                    board.i_won(number)
                    winning_row.append(i)

    losing_board = bingo_boards[winning_row[-1]]

    print('score', losing_board.get_score())


if __name__ == '__main__':
    main()
