def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, is_maximizing):
    if check_winner(board, 'X'):
        return 1
    if check_winner(board, 'O'):
        return -1
    if is_board_full(board):
        return 0
    if is_maximizing:
        best_score = float('-inf')
        for i, j in get_valid_moves(board):
            board[i][j] = 'X'
            score = minimax(board, False)
            board[i][j] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_valid_moves(board):
            board[i][j] = 'O'
            score = minimax(board, True)
            board[i][j] = ' '
            best_score = min(best_score, score)
        return best_score

def computer_move(board):
    best_score = float('-inf')
    best_move = None
    for i, j in get_valid_moves(board):
        board[i][j] = 'X'
        score = minimax(board, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe: You are O, Computer is X. Enter row,col (0-2) for your move.")
    while True:
        # Human move
        print_board(board)
        try:
            row, col = map(int, input("Enter your move (row,col): ").split(','))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = 'O'
            else:
                print("Invalid move. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Use format 'row,col' (e.g., '1,1').")
            continue
        # Check game state
        if check_winner(board, 'O'):
            print_board(board)
            print("You win! (This shouldn't happen with minimax.)")
            break
        if is_board_full(board):
            print_board(board)
            print("Draw!")
            break
        # Computer move
        row, col = computer_move(board)
        board[row][col] = 'X'
        print(f"Computer moves to ({row}, {col})")
        if check_winner(board, 'X'):
            print_board(board)
            print("Computer wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("Draw!")
            break

if __name__ == "__main__":
    main()
