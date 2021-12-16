
import sys

from dataclasses import dataclass


@dataclass
class SubmarineBearings:
    """Horizontal position, depth, and aim of a Submarine."""
    position: int = 0
    depth: int = 0
    aim: int = 0

    def move_forward(self, distance):
        self.position += distance
        self.depth += distance * self.aim

    def rotate_up(self, units):
        self.aim -= units

    def rotate_down(self, units):
        self.aim += units

    def get_distance(self):
        return self.position * self.depth

    def __repr__(self):
        return f"Submarine: {self.position} {self.depth} {self.aim}"


def move_submarine(movements: list):
    """Count the number of times the depth increases in a series of
    depth readings.

    :param movements: List of str movements an integer number of units in
        a specific direction.
    :return: Product of the horizontal and vertical movements.
    """
    submarine = SubmarineBearings()

    for movement in movements:
        direction, amount = movement.split()
        if direction == "forward":
            submarine.move_forward(int(amount))
        elif direction == "up":
            submarine.rotate_up(int(amount))
        elif direction == "down":
            submarine.rotate_down(int(amount))
        print(submarine)

    return submarine.get_distance()


def main():
    with open(sys.argv[1]) as f:
        depth_readings = f.readlines()

    total_distance = move_submarine(depth_readings)
    print(f"total distance moved is {total_distance}")


if __name__ == "__main__":
    main()
