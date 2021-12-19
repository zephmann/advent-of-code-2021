
import sys
from collections.abc import Iterator


def count_fish(fish_ages: list[int], num_days: int):
    """Simulate fish reproducing for a certain number of days and return the
    final total number of fish. Each fish reproduces after 7 days, and new
    fish take an extra 2 days to mature.

    :param fish_ages: List of integer ages of the starting fish.
    :param num_days: Integer number of days to simulate.
    :return: Integer number of fish after the number of days have elapsed.
    """
    for _ in range(num_days):
        num_babies = 0
        for i, fish_age in enumerate(fish_ages):
            if not fish_age:
                fish_ages[i] = 6
                num_babies += 1
            else:
                fish_ages[i] = fish_age - 1

        fish_ages.extend([8] * num_babies)

    return len(fish_ages)


def main():
    with open(sys.argv[1]) as f:
        fish_ages = list(map(int, f.readline().split(",")))

    num_days = int(sys.argv[2])
    num_fish = count_fish(fish_ages, num_days)
    print(f"total number of fish is {num_fish}")


if __name__ == "__main__":
    main()
