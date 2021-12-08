def main():
    outcomes = []

    with open('input.txt', 'r') as f:
        for line in f:
            input = line.rstrip().split(' | ')
            outcomes.append(input[1].split())

    count_of_1_4_7_8 = 0
    for outcome in outcomes:
        count_of_1_4_7_8 += len([digit for digit in outcome if len(digit) in (2, 4, 3, 7)])

    print('couunt', count_of_1_4_7_8)


if __name__ == '__main__':
    main()
