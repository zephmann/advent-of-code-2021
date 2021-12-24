
import sys


def find_fuel_cost(positions: list[int]) -> int:
    """Calculate the minimum amount of fuel required to shift all positions
    to be uniform. Distance is simply the different between two positions.
    The minimum total distance will be the sum of the distances of each
    position to the median position.

    :param positions: List of integer positions.
    :return: Lowest possible total fuel cost.
    """
    # Could use quick sort algorithm to find median in log(n)
    # instead of fully sorting.
    mid_index = int(len(positions)/2)
    median = sorted(positions)[mid_index]

    # Calc cost of distances from the median.
    total_fuel = sum(abs(pos - median) for pos in positions)

    return total_fuel


def main():
    with open(sys.argv[1]) as f:
        starting_positions = list(map(int, f.read().split(",")))

    fuel_costs = find_fuel_cost(starting_positions)
    print(f"Total fuel costs are {fuel_costs}")

if __name__ == "__main__":
    main()
