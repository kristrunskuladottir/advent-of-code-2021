from solution_1 import check_for_neighbour_flashes


def main():
    energy_levels_all = []

    with open('input.txt') as f:
        for line in f:
            energy_levels_all.append([int(energy_level) for energy_level in list(line.rstrip())])

    total_number_of_octopus = len(energy_levels_all) * len(energy_levels_all[0])

    step = 1
    while step < 1000:
        # lets start with increasing all the energy levels by 1
        flashes = set()
        for y in range(len(energy_levels_all)):
            for x in range(len(energy_levels_all[y])):
                energy_levels_all[y][x] += 1
                if energy_levels_all[y][x] == 10:
                    flashes.add((x, y))

        new_flashes = flashes.copy()

        for x, y in flashes:
            new_flashes = check_for_neighbour_flashes(x, y, energy_levels_all, new_flashes)

        if len(new_flashes) == total_number_of_octopus:
            # in sync!!
            break

        # reset all flashed octopus
        for y in range(len(energy_levels_all)):
            for x in range(len(energy_levels_all[y])):
                if energy_levels_all[y][x] == 10:
                    energy_levels_all[y][x] = 0

        step += 1

    print('we were all in sync at step', step)


if __name__ == '__main__':
    main()
