
import sys


def calc_power_level(readings: list):
    """Calculate the current power level of the submarine based on a list of
    binary instrument readings.

    :param readings: List of str instrument readings. Each reading should be a
        binary number.
    :return: Product of gamma and epsilon rates.
    """
    if not readings:
        return 0

    # store total required to be "most common"
    half_len = len(readings) / 2

    # rotate the readings matrix to group digits by position
    # ex: [10, 11, 01, 00] -> [1100, 0110]
    readings = zip(*readings)

    # build up the strings
    gamma = ""
    epsilon = ""
    for reading in readings:
        total = sum(map(int, reading))
        gamma += "1" if total > half_len else "0"
        epsilon += "0" if total > half_len else "1"

    # convert to integers and return the product
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


def main():
    with open(sys.argv[1]) as f:
        readings = f.readlines()

    power_level = calc_power_level(readings)
    print(f"current power level is {power_level}")


if __name__ == "__main__":
    main()
