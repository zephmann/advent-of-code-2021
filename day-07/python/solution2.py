
import math
import sys


def find_fuel_cost(positions: list[int]) -> int:
    """Calculate the minimum amount of fuel required to shift all positions
    to be uniform. Distance is the arithmetic sum of the difference of two
    positions. The minimum total distance will be the sum of the distances of
    each position to the average position.

    :param positions: List of integer positions.
    :return: Lowest possible total fuel cost.
    """
    # The average seems to be off for the main input, possibly due to
    # floating point precision.
    # Could only calc both if less than an epsilon from 0.5.
    average = sum(positions) / len(positions)
    average_1, average_2 = math.floor(average), math.ceil(average)

    def calc_cost(_position, _center):
        # (N * N+1) / 2
        distance = abs(_position - _center)
        return (distance * (distance + 1)) >> 1

    total_1, total_2 = 0, 0
    for position in positions:
        total_1 += calc_cost(position, average_1)
        total_2 += calc_cost(position, average_2)

    print(f"Average {average}")
    if total_1 < total_2:
        print(f"Using floor average {average_1}")
        return total_1
    print(f"Using ceil average {average_2}")
    return total_2


def main():
    with open(sys.argv[1]) as f:
        starting_positions = list(map(int, f.read().split(",")))

    fuel_costs = find_fuel_cost(starting_positions)
    print(f"Total fuel costs are {fuel_costs}")

if __name__ == "__main__":
    main()
