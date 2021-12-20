
import sys

DAYS_TO_REPRODUCE = 7
DAYS_TO_MATURE = 2 + DAYS_TO_REPRODUCE


def count_fish(fish_ages: list[int], total_days: int):
    """Simulate fish reproducing for a certain number of days and return the
    final total number of fish. Each fish reproduces after 7 days, and new
    fish take an extra 2 days to mature.

    :param fish_ages: List of integer ages of the starting fish.
    :param total_days: Integer number of days to simulate.
    :return: Integer number of fish after the number of days have elapsed.
    """
    # loop method is way too slow to calculate growth for each fish.
    memo_dict = {}

    def count_children(start_day):
        """Recursive helper method to calculate the total number of children
        a fish would spawn given a specific starting day.

        :param start_day: The first day that the fish will multiply.
        :return: Total number of children created by the fish.
        """
        memo_result = memo_dict.get(start_day)
        if memo_result is not None:
            return memo_result

        # iterate through the day numbers when the fish will reproduce, and
        # count any subsequent children.
        num_children = 1
        for current_day in range(start_day, total_days, DAYS_TO_REPRODUCE):
            child_age = current_day + DAYS_TO_MATURE

            # skip the recursive call if the loop will be skipped.
            if child_age < total_days:
                num_children += count_children(child_age)
            else:
                num_children += 1

        memo_dict[start_day] = num_children
        return num_children

    return sum(map(count_children, fish_ages))


def main():
    with open(sys.argv[1]) as f:
        fish_ages = list(map(int, f.readline().split(",")))

    num_days = int(sys.argv[2])
    num_fish = count_fish(fish_ages, num_days)
    print(f"total number of fish is {num_fish}")


if __name__ == "__main__":
    main()
