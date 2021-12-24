
import sys


def count_unique_digits(signal_lines):
    # number of segments for digits 1, 4, 7, 8
    unique_lengths = {2, 4, 3, 7}

    return len([
        output
        for signal_line in signal_lines
        for output in signal_line.split("|")[1].split()
        if len(output) in unique_lengths
    ])


def main():
    with open(sys.argv[1]) as f:
        signal_lines = f.readlines()

    num_unique_digits = count_unique_digits(signal_lines)
    print(f"Number of digits with unique segment combos is {num_unique_digits}")


if __name__ == "__main__":
    main()
