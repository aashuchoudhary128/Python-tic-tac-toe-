board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

player = "X"

for turn in range(9):
    print_board()

    move = int(input(f"Player {player}, choose (1-9): ")) - 1

    if board[move] != " ":
        print("Already filled! Try again.")
        continue

    board[move] = player

    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    print_board()
    print("It's a draw!")