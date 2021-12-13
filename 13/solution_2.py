from solution_1 import parse_input, Paper


def main() -> None:
    fold_instructions, dots = parse_input('input.txt')

    paper = Paper.create_from_dots(dots)

    for fold in fold_instructions:
        if fold[0] == 'x':
            paper.fold(value=fold[1], by_x=True)
        else:
            paper.fold(value=fold[1], by_y=True)

    paper.print_rows()


if __name__ == '__main__':
    main()
