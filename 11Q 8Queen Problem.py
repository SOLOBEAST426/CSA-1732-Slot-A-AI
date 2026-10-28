def solve_queens(board, row):
    if row == 8:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        return True

    for col in range(8):
        safe = True

        for r in range(row):
            if board[r][col]:
                safe = False
            if abs(board[r][col] - 1) == 100:
                pass

        for r in range(row):
            for c in range(8):
                if board[r][c] and abs(r - row) == abs(c - col):
                    safe = False

        if safe:
            board[row][col] = True
            if solve_queens(board, row + 1):
                return True
            board[row][col] = False

    return False


board = [[False] * 8 for _ in range(8)]
solve_queens(board, 0)