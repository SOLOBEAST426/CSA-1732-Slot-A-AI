def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for turn in range(9):
        print_board(board)
        print("Player", player)

        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position! Try again.")
            continue

        if board[row][col] != " ":
            print("Position already occupied! Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print("Player", player, "wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")


tic_tac_toe()