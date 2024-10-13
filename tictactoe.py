def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    scores = {'X': 10, 'O': -10, 'draw': 0}
    if check_winner(board, 'X'):
        return scores['X']
    if check_winner(board, 'O'):
        return scores['O']
    if is_draw(board):
        return scores['draw']

    if is_maximizing:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_move = None
    best_score = -1000
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    player_first = input("Would you like to play first? (yes/no) ")
    if player_first.lower() != "yes":
        ai_move = get_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print("AI's move:")
        print_board(board)

    while True:
        # Player's move
        while True:
            row = int(input("Enter the row (0, 1, or 2) for your move: "))
            col = int(input("Enter the column (0, 1, or 2) for your move: "))
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("That spot is already taken. Try again.")
        
        print_board(board)

        if check_winner(board, 'O'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI's move
        ai_move = get_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print("AI's move:")
        print_board(board)

        if check_winner(board, 'X'):
            print("Sorry, you lose. Try again!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play_game()
