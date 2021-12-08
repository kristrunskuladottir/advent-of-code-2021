from typing import List


def interpret_line(signals: List[str], outcomes: List[str]) -> int:
    mapping = {}
    for signal in signals:
        if len(signal) == 2:
            mapping[1] = frozenset(list(signal))
        elif len(signal) == 3:
            mapping[7] = frozenset(list(signal))
        elif len(signal) == 4:
            mapping[4] = frozenset(list(signal))
        elif len(signal) == 7:
            mapping[8] = frozenset(list(signal))

    length_five = [frozenset(list(signal)) for signal in signals if len(signal) == 5]
    length_six = [frozenset(list(signal)) for signal in signals if len(signal) == 6]

    #  000
    # 1   2
    # 1   2
    # 1   2
    #  333
    # 4   5
    # 4   5
    # 4   5
    #  666

    placements = [''] * 7  # see index placement above
    placements[0] = list(mapping[7] - mapping[1])[0]  # we know the placement of the topmost line if we diff the 1 and the 7

    # we can find the middle line by finding the one that's in common between 4 and all the ones with length 5
    placements[3] = list(mapping[4] & frozenset.intersection(*length_five))[0]

    # we can find the bottom line by finding the one that's in common between all the ones with length 5 and 6
    placements[6] = list(frozenset.intersection(*(length_five + length_six)) - frozenset(placements[0]))[0]

    top_bottom_and_middle = frozenset([placement for placement in placements if placement != ''])

    # we know the three since we know the right most lines and the top, bottom and middle lines
    mapping[3] = mapping[1] | top_bottom_and_middle

    # we can now find the 9, it's the one with length 6 and includes all the same segments as the 3
    for digit in length_six:
        if len(digit - mapping[3]) == 1:
            mapping[9] = digit
            placements[1] = list(digit - mapping[3])[0]

    # we can now find the 5, it's the only one with length 5 that includes the segment placed at 1
    for digit in length_five:
        if placements[1] in digit:
            mapping[5] = digit
            placements[5] = list(digit - top_bottom_and_middle - frozenset([placements[1]]))[0]

    # we now know the 2, its the last one of the length_fives
    length_five.remove(mapping[3])
    length_five.remove(mapping[5])
    mapping[2] = length_five[0]

    # placement 4 is found by getting the single segment that exists for the digit 2 but doesn't exist for 3
    placements[4] = list(mapping[2] - mapping[3])[0]

    # now we are just missing placements[2], mapping[6] and mapping[0]

    # we have all the placements we need for mapping[6]
    mapping[6] = frozenset([placement for placement in placements if placement != ''])

    # and then we can determine 0 by choosing the last of length six
    length_six.remove(mapping[6])
    length_six.remove(mapping[9])
    mapping[0] = length_six[0]

    # placement 2 is found by getting the single segment that exists for the digit 0 but doesn't exist for 6
    placements[2] = list(mapping[0] - mapping[6])[0]

    # now we have all the values we need. lets find the outcome value
    inverted_mapping = {value: key for key, value in mapping.items()}

    value = ''
    for outcome in outcomes:
        value += str(inverted_mapping[frozenset(list(outcome))])

    return int(value)


def main():
    output_sum = 0

    with open('input.txt', 'r') as f:
        for line in f:
            input = line.rstrip().split(' | ')

            output_sum += interpret_line(input[0].split(), input[1].split())

    print('sum', output_sum)


if __name__ == '__main__':
    main()
