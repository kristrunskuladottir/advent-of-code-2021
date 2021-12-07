def main():
    with open('input.txt', 'r') as f:
        horizontal_positions = f.readline().rstrip().split(',')
        horizontal_positions = [int(hor_pos) for hor_pos in horizontal_positions]

    position = min(horizontal_positions)

    steps_required = [0] * (max(horizontal_positions) - min(horizontal_positions))  # normalize the range of positions
    # steps_required[i] == total number of steps that the crabs need to take to get to position (i + min(horizontal_positions))

    while position < max(horizontal_positions):
        steps_required_to_move_to_position = sum([abs(hor_pos - position) for hor_pos in horizontal_positions])
        steps_required[position - min(horizontal_positions)] = steps_required_to_move_to_position
        position += 1

    position = steps_required.index(min(steps_required)) + min(horizontal_positions)
    print('min fuel used is at', position, 'and total fuel is', min(steps_required))


if __name__ == '__main__':
    main()
