#!/usr/bin/python3

import sys


def solve_nqueens(n):
    board = [-1] * n

    def is_valid(row, col):
        for i in range(row):
            if col in (board[i] for i in range(row)) or \
               any(abs(board[i]-col) == abs(i-row) for i in range(row)):
                return False
        return True

    def backtrack(row):
        if row == n:
            print([list(x) for x in zip(range(n), board)])
            return

        for col in [col for col in range(n) if is_valid(row, col)]:
            board[row] = col
            backtrack(row + 1)

    backtrack(0)


if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    solve_nqueens(n)
