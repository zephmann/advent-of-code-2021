
import sys


def count_depth_increases(depth_readings: list):
    """Count the number of times the depth increases in a series of
    depth readings, comparing groups of 3 readings.

    :param depth_readings: List of integers corresponding to the depth.
    :return: Number of times the depth increased.
    """
    # Because the sum will contain over-lapping values, we don't need to
    # check those. Instead we can just compare the first value of the first
    # group and the last value of the last group.
    depth_increases = 0

    if not depth_readings:
        return depth_increases

    # Create a queue with the first 3 values, removing them from the list.
    prev_depths = [
        depth_readings.pop(0),
        depth_readings.pop(0),
        depth_readings.pop(0)
    ]

    for current_depth in depth_readings:
        # Pop out first value from the queue. This will be the group A and
        # compare with the next value in the readings which will be group B.
        prev_depth = int(prev_depths.pop(0))
        current_depth = int(current_depth)
        if current_depth > prev_depth:
            depth_increases += 1

        # Add the current value to the end of the queue.
        prev_depths.append(current_depth)

    return depth_increases


def main():
    with open(sys.argv[1]) as f:
        depth_readings = f.readlines()

    depth_increases = count_depth_increases(depth_readings)
    print(f"number of depth increases is {depth_increases}")


if __name__ == "__main__":
    main()
