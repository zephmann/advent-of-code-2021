
import sys

from dataclasses import dataclass


@dataclass
class Point:
    """2D position"""
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def distance(self):
        return self.x * self.y


@dataclass
class Vector:
    """2D Direction"""
    x: int
    y: int

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)


def move_submarine(movements: list):
    """Count the number of times the depth increases in a series of
    depth readings.

    :param movements: List of str movements an integer number of units in
        a specific direction.
    :return: Product of the horizontal and vertical movements.
    """
    directions = {
        "forward": Vector(x=1, y=0),
        "up": Vector(x=0, y=-1),
        "down": Vector(x=0, y=1),
    }

    position = Point(0, 0)
    for movement in movements:
        direction, distance = movement.split()
        direction = int(distance) * directions[direction]
        position = position + direction

    return position.distance()


def main():
    with open(sys.argv[1]) as f:
        depth_readings = f.readlines()

    total_distance = move_submarine(depth_readings)
    print(f"total distance moved is {total_distance}")


if __name__ == "__main__":
    main()
