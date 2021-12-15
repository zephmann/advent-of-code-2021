#!/usr/bin/python3

import sys


def count_depth_increases(depth_readings: list):
	"""Count the number of times the depth increases in a series of
	depth readings.

	:param depth_readings: List of integers corresponding to the depth.
	:return: Number of times the depth increased.
	"""
	depth_increases = 0

	if not depth_readings:
		return depth_increases

	prev_depth = int(depth_readings.pop(0))
	for current_depth in depth_readings:
		current_depth = int(current_depth)
		if current_depth > prev_depth:
			depth_increases += 1
		prev_depth = current_depth

	return depth_increases


def main():
	with open(sys.argv[1]) as f:
		depth_readings = f.readlines()

	depth_increases = count_depth_increases(depth_readings)
	print(f"number of depth increases is {depth_increases}")


if __name__ == "__main__":
	main()
