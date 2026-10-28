def minimax(stones, is_computer):
    if stones == 0:
        return -1 if is_computer else 1

    if is_computer:
        best = -float("inf")
        for move in [1, 2]:
            if stones >= move:
                score = minimax(stones - move, False)
                best = max(best, score)
        return best
    else:
        best = float("inf")
        for move in [1, 2]:
            if stones >= move:
                score = minimax(stones - move, True)
                best = min(best, score)
        return best


def best_move(stones):
    move_choice = 1
    best_score = -float("inf")

    for move in [1, 2]:
        if stones >= move:
            score = minimax(stones - move, False)
            if score > best_score:
                best_score = score
                move_choice = move

    return move_choice


def play_game():
    stones = 10
    print("STONE PICKING GAME")
    print("There are 10 stones.")
    print("You can remove 1 or 2 stones per turn.")
    print("The player who takes the last stone wins.")

    while stones > 0:
        print("\nStones remaining:", stones)

        while True:
            try:
                move = int(input("Your move (1 or 2): "))
                if move in [1, 2] and move <= stones:
                    break
                print("Choose 1 or 2 stones, not more than the remaining stones.")
            except ValueError:
                print("Please enter a number.")

        stones -= move

        if stones == 0:
            print("You win!")
            break

        computer_move = best_move(stones)
        print("Computer removes:", computer_move)
        stones -= computer_move

        if stones == 0:
            print("Computer wins!")
            break


play_game()
