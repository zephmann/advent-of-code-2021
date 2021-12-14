
with open("input.txt") as f:
	depth_readings = f.readlines()

prev_depth = int(depth_readings.pop(0))

depth_increases = 0
for current_depth in depth_readings:
	current_depth = int(current_depth)
	if current_depth > prev_depth:
		depth_increases += 1
	prev_depth = current_depth

print("number of depth increases is {0}".format(depth_increases))
