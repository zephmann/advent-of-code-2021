
import sys


def calc_life_support(readings: list):
    """Calculate the life support rating from the instrument readings.

    :param readings: List of str instrument readings. Each reading should be a
        binary number.
    :return: Product of oxygen generator rating and CO2 scrubber rating.
    """
    if not readings:
        return 0

    # perform an initial split
    ones_readings = []
    zero_readings = []
    for reading in readings:
        if reading[0] == "1":
            ones_readings.append(reading)
        else:
            zero_readings.append(reading)

    if len(ones_readings) > len(zero_readings):
        oxygen_readings, co2_readings = ones_readings, zero_readings
    else:
        oxygen_readings, co2_readings = zero_readings, ones_readings

    # loop through all digits starting at 1
    for i in range(1, len(readings[1])):
        num_oxygen = len(oxygen_readings)
        num_co2 = len(co2_readings)
        if num_oxygen == 1 and num_co2 == 1:
            break

        if num_oxygen > 1:
            half_readings = len(oxygen_readings) / 2
            total = sum(map(lambda r: int(r[i]), oxygen_readings))
            common_digit = "1" if total >= half_readings else "0"
            oxygen_readings = [r for r in oxygen_readings if r[i] == common_digit]

        if num_co2 > 1:
            half_readings = len(co2_readings) / 2
            total = sum(map(lambda r: int(r[i]), co2_readings))
            common_digit = "1" if total >= half_readings else "0"
            co2_readings = [r for r in co2_readings if r[i] != common_digit]

    assert len(oxygen_readings) == 1
    assert len(co2_readings) == 1

    oxygen_rating = int(oxygen_readings[0], 2)
    co2_rating = int(co2_readings[0], 2)

    return oxygen_rating * co2_rating


def main():
    with open(sys.argv[1]) as f:
        readings = f.readlines()

    total_distance = calc_life_support(readings)
    print(f"total distance moved is {total_distance}")


if __name__ == "__main__":
    main()
