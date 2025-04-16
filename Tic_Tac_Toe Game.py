import random

def print_board(board):
    print("\nCurrent board: ")
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

def play_again():
    p = tic_tac_toe()
    return p

def check_winner(board, player):
    # Rows, columns, diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False    
    
def is_draw(board):
    return all(cell in ['❌', '⭕'] for row in board for cell in row)    


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_1 = input('Player 1, enter your name: ')
    player_2 = input('Player 2, enter your name: ')
    current_player = random.choice([player_1, player_2])

    while True:
        print("Welcome to the Tic Tac Toe Arena!")
        print(f"{current_player} goes first.")

        while True:
            print_board(board)

            try:
                move = int(input(f"{current_player}, enter your move (each cell represents a number; 1 - 9): "))
            #row, col = map(int, move.strip().split())

            except ValueError:
                print("Invalid input. Use any number from 1 to 9.")
                continue

            if move not in range(1, 10):
                print("Move out of bounds. Try again.")
                continue    

            row = (move - 1) // 3
            col = (move - 1) % 3

        
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue

            symbol = '❌' if current_player == player_1 else '⭕'
            board[row][col] = symbol

            if check_winner(board, symbol):
                print_board(board)
                print(f"🎉{current_player} wins!")
                break
            

            
            
            if is_draw(board):
                print_board(board)
                print("It's a draw! 🤝")
                break

            current_player = player_1 if current_player == player_2  else player_2   



        print('Do you want a rematch? ')
        choice = input('Yes/No \n> ').strip().lower()
        
        if choice != 'yes':
            print('Thanks for playing! 🤝')
            break
    
          
    

tic_tac_toe() 