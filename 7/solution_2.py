def main() -> None:
    with open('input.txt', 'r') as f:
        horizontal_positions = f.readline().rstrip().split(',')
        horizontal_positions = [int(hor_pos) for hor_pos in horizontal_positions]

    position = min(horizontal_positions)

    fuel_required = [0] * (max(horizontal_positions) - min(horizontal_positions))  # normalize the range of positions
    # fuel_required[i] == total fuel that the crabs need to get to position (i + min(horizontal_positions))

    while position < max(horizontal_positions):
        steps_required = [abs(hor_pos - position) for hor_pos in horizontal_positions]

        fuel_required_to_move_to_position = sum([sum(range(steps + 1)) for steps in steps_required])
        fuel_required[position - min(horizontal_positions)] = fuel_required_to_move_to_position

        position += 1

    position = fuel_required.index(min(fuel_required)) + min(horizontal_positions)
    print('min fuel used is at', position, 'and total fuel is', min(fuel_required))


if __name__ == '__main__':
    main()
