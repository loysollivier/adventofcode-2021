#!/usr/bin/env python3
import re


input_data = []
with open('input.txt', 'r', encoding="utf-8") as f:
    input_data = f.read().splitlines()

draws = [int(number) for number in input_data.pop(0).split(',')]


class BingoBoard:
    """
    Class representing a bingo board.
    """
    def __init__(self, board):
        """
        The board should be a two dimensional list:
        [[0,1,2,3,4][5,6,7,8,9][...]]
        """
        self.board = []
        for numbers in board:
            self.board.append({})
            for number in numbers:
                self.board[-1][number] = False

    def draw(self, draw):
        """
        If the number drawn is in the board, mark it as drawn
        """
        for line in self.board:
            for number in line.keys():
                if number == draw:
                    line[number] = True

    @property
    def wins(self):
        """
        Returns True if the board has a winning row or column, False oterwise
        """
        # Check if a row has won
        for row in self.board:
            has_won = True
            for drawn in row.values():
                if not drawn:
                    has_won = False
                    break
            if has_won:
                return True
        # Check if a column has won
        for column in range(len(self.board[0])):
            has_won = True
            for row in self.board:
                if not list(row.values())[column]:
                    has_won = False
                    break
            if has_won:
                return True
        # No winner yet
        return False

    def __repr__(self):
        the_rep = ""
        for line in self.board:
            the_rep = f"{the_rep}\n"
            for a_num in line.keys():
                the_rep = f"{the_rep} {a_num:2}"
        return the_rep

    @property
    def unmarked_sum(self):
        unmarked_sum = 0
        for line in self.board:
            for number, drawn in line.items():
                if not drawn:
                    unmarked_sum += number
        return unmarked_sum

board = []
bingo_boards = []
input_data.pop(0)  # Remove the first blank line
for line in input_data:
    # Remove any leading/trailing whitespace
    line = line.strip()
    # Sed duplicate whitespaces
    line = re.sub(r"\s\s+", " ", line)
    if line == '':
        bingo_boards.append(BingoBoard(board))
        board = []
    else:
        board.append([int(number) for number in line.split(" ")])


def draw_for_all(bingo_boards, number):
    """
    Draws for all boards and checks if there is a winning board
    """
    # Function modified for part 2
    # Instead of breaking on the first winner return a list of winners.
    winners = []
    won = False
    for bingo_board in bingo_boards:
        bingo_board.draw(number)
        if bingo_board.wins:
            winners.append(bingo_board)
            won = True
    return winners, won


for draw in draws:
    winners, won = draw_for_all(bingo_boards, draw)
    if won:
        for winner in winners:
            print(f"Winning board is {winner}")
            print(f"Unmarked sum is {winner.unmarked_sum}")
            print(f"Last number drawn is {draw}")
            print(f"Final score is {draw*winner.unmarked_sum}")
            # Part 1 solution: uncomment the break
            # break
            bingo_boards.remove(winner)
