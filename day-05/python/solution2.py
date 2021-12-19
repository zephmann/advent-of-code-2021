
from collections import defaultdict
from collections.abc import Iterator
import sys


def get_danger_areas(vent_lines: list[Iterator[int]]):
    """Count the number of times the depth increases in a series of
    depth readings.

    :param vent_lines: List of vents as start and end positions.
    :return: Total number of positions with a danger level of 2 or greater.
    """
    # map positions to danger levels.
    # since we only care about values 2 or greater, start at negative 1
    # so we can easily filter against 0
    danger_levels = defaultdict(lambda: -1)

    for vent_line in vent_lines:
        start_x, start_y, end_x, end_y = vent_line

        step_x = 1 if start_x < end_x else -1
        step_y = 1 if start_y < end_y else -1

        x_range = range(start_x, end_x + step_x, step_x)
        y_range = range(start_y, end_y + step_y, step_y)

        # vertical line
        if start_x == end_x:
            for y in y_range:
                danger_levels[(start_x, y)] += 1

        # horizontal line
        elif start_y == end_y:
            for x in x_range:
                danger_levels[(x, start_y)] += 1

        # diagonal line
        else:
            for x, y in zip(x_range, y_range):
                danger_levels[(x, y)] += 1

    # count total vent areas greater than 0
    return len(list(filter(None, danger_levels.values())))


def main():
    with open(sys.argv[1]) as f:
        vent_lines = [
            map(int, line.replace("->", ",").split(","))
            for line in f.readlines()
        ]

    num_danger_areas = get_danger_areas(vent_lines)
    print(f"total number of danger areas is {num_danger_areas}")


if __name__ == "__main__":
    main()
