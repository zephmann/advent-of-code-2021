
import sys


def sum_signals(signal_lines: list[str]) -> int:
    total = 0

    # iterate through lines of segment codes
    for signal_line in signal_lines:
        input_codes, output_codes = signal_line.split("|")

        digit_map = _find_digits(input_codes.split())

        output_value = 0
        for segments in output_codes.split():
            output_value *= 10
            output_value += digit_map["".join(sorted(segments))]

        total += output_value

    return total


def _find_digits(segment_codes: list[str]) -> dict:
    """Determine which segment code corresponds to which digit. Return a
    map of each segment code pointing to the corresponding digit.

    :param segment_codes: List of string segment codes.
    :return: Map of sorted segment codes to the corresponding digit.
    """
    digit_map = {}

    # find digits with unique segment lengths
    unique_lengths = {2: 1, 4: 4, 3: 7, 7: 8}
    for segments in segment_codes:
        digit = unique_lengths.get(len(segments))
        if digit:
            digit_map[digit] = set(segments)

    # find digits with length 6
    # TODO could probably combine these two loops
    for segments in segment_codes:
        if len(segments) != 6:
            continue

        # 9 will overlap 4 completely
        # 0 will overlap 1 but not 4
        # 6 doesn't overlap 4 or 1
        if not digit_map[4].difference(segments):
            digit_map[9] = segments
        elif not digit_map[1].difference(segments):
            digit_map[0] = segments
        else:
            digit_map[6] = set(segments)

    # find digits with length 5
    for segments in segment_codes:
        if len(segments) != 5:
            continue

        # 3 will overlap 1 completely
        # 5 will overlaps all but 1 of 6
        # 2 doesn't overlap 1 and overlaps all but 2 of 6
        if not digit_map[1].difference(segments):
            digit_map[3] = segments
        elif len(digit_map[6].difference(segments)) == 1:
            digit_map[5] = segments
        else:
            digit_map[2] = segments

    # can't hash a set.
    return {
        "".join(sorted(segments)): digit
        for digit, segments in digit_map.items()
    }


def main():
    with open(sys.argv[1]) as f:
        signal_lines = f.readlines()

    num_unique_digits = sum_signals(signal_lines)
    print(f"Sum of output values is {num_unique_digits}")


if __name__ == "__main__":
    main()
