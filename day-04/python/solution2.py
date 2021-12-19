
from collections.abc import Iterator
import sys


class BingoBoard:
    """Bingo board of numbers that keeps track of what numbers have been marked.
    A board "has won" if it has either a full row or column of marked spaces.
    The score for a winning board can be calculated by adding the space numbers
    of any unmarked spaces.
    """

    def __init__(self, board_numbers: list[list[int]]):
        """Initialize a new Bingo board with the board numbers.

        :param board_numbers: 2D list of numbers for the board spaces.
        """
        self._marks = []  # 2D list of bools indicating marked spaces
        self._numbers = {}  # map of number to board coordinates
        self._score = 0  # store score and update when numbers are marked off

        for row_num, row in enumerate(board_numbers):
            self._marks.append([False] * len(row))
            self._score += sum(row)
            for col_num, drawn_number in enumerate(row):
                error_message = "Boards cannot have duplicate numbers."
                assert drawn_number not in self._numbers, error_message

                self._numbers[drawn_number] = (row_num, col_num)

    def mark(self, number: int):
        """Mark the space corresponding to the number, if present."""
        coords = self._numbers.get(number)
        if coords:
            self._marks[coords[0]][coords[1]] = True
            self._score -= number

    def has_won(self):
        """Return a bool indicating whether the board has a fully
        marked row or column."""
        # check for winning row, then rotate and check for winning column
        return (
            any(all(row) for row in self._marks) or
            any(all(row) for row in zip(*self._marks))
        )

    @property
    def score(self):
        return self._score

    # def get_score(self):
    #     """Return the winning score for the board, the sum of all
    #     unmarked spaces."""
    #     def is_unmarked(number):
    #         coords = self._numbers[number]
    #         return not self._marks[coords[0]][coords[1]]
    #
    #     return sum(filter(is_unmarked, self._numbers))


def find_last_winning_board(
    drawn_numbers: Iterator[int], board_numbers: list[list[list[int]]]
):
    """Find the bingo board that will win last based on the called numbers
    and calculate its score.

    :param drawn_numbers: List of drawn integer numbers.
    :param board_numbers: List of 2D lists of board numbers.
    :return: Total score of the winning board, the sum of the unmarked spaces
        multiplied by the last drawn number.
    """
    boards = list(map(BingoBoard, board_numbers))

    for number in drawn_numbers:
        active_boards = []
        num_boards = len(boards)
        for board in boards:
            board.mark(number)
            if not board.has_won():
                active_boards.append(board)
            elif num_boards == 1:
                return number * board.score
        boards = active_boards


def main():
    with open(sys.argv[1]) as f:
        depth_readings = f.readline()
        drawn_numbers = map(int, depth_readings.split(","))

        # read line between drawn numbers and boards
        f.readline()

        board_numbers = []
        board = []
        for row in f.readlines():
            if row == "\n":
                board_numbers.append(board)
                board = []
            else:
                board.append(list(map(int, row.split())))
        board_numbers.append(board)

    score = find_last_winning_board(drawn_numbers, board_numbers)
    print(f"The winning score is {score}")


if __name__ == "__main__":
    main()
