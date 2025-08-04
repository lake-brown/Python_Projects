import random
import argparse

def display_board(board):
    print('\n' * 100)  # Clears the screen
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    while True:
        choice = input("Pick X or O: ").upper()
        if choice not in ["X", "O"]:
            print("Please pick X or O")
        else:
            return ('X', 'O') if choice == "X" else ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
            (board[4] == mark and board[5] == mark and board[6] == mark) or 
            (board[1] == mark and board[2] == mark and board[3] == mark) or 
            (board[7] == mark and board[4] == mark and board[1] == mark) or 
            (board[8] == mark and board[5] == mark and board[2] == mark) or 
            (board[9] == mark and board[6] == mark and board[3] == mark) or 
            (board[7] == mark and board[5] == mark and board[3] == mark) or 
            (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    if random.randint(1, 2) == 1:
        print("Player 1 goes first")
        return 'Player 1'
    else:
        print("Player 2 goes first")
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(space != ' ' for space in board[1:])

def player_choice(board):
    while True:
        pos = input("Choose a position (1-9): ")
        if pos.isdigit():
            pos = int(pos)
            if 1 <= pos <= 9:
                if space_check(board, pos):
                    return pos
                else:
                    print("Position taken.")
            else:
                print("Choose between 1 and 9.")
        else:
            print("Please enter a number.")

def replay():
    return input("Would you like to play again? (yes or no): ").lower().startswith('y')

def tictac(name):
    print(f"Welcome to Tic Tac Toe, {name}!")
    while True:
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + " will go first.")

        play_game = input("Ready to play? (yes or no): ").lower()
        game_on = play_game.startswith('y')

        while game_on:
            if turn == 'Player 1':
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print("Congratulations! Player 1 has won the game!")
                    game_on = False
                elif full_board_check(theBoard):
                    display_board(theBoard)
                    print("It's a draw!")
                    break
                else:
                    turn = 'Player 2'
            else:
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print("Congratulations! Player 2 has won the game!")
                    game_on = False
                elif full_board_check(theBoard):
                    display_board(theBoard)
                    print("It's a draw!")
                    break
                else:
                    turn = 'Player 1'

        if not replay():
            print("Thanks for playing!")
            return

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Tic Tac Toe with a personalized experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="The name of the person playing the game."
    )

    args = parser.parse_args()
    tictac(args.name)
