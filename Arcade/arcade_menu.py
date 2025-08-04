import sys
import RPS
import guess_number
import tictac

def game_on(name="player 1"):
    while True:
        try:
            game = int(input("Pick a game:\n 1. Rock Paper Scissors \n 2. Guess a Number \n 3. TIC TAC TOE \n 4. Quit arcade \nEnter choice: "))
            
            if game == 1:
                RPS.rps(name) 
            elif game == 2:
                guess_number.guess(name)  
            elif game == 3:
                tictac.tictac(name)
            elif game == 4:
                print(f"Thank you for playing, {name}!\n")
                sys.exit(f"Bye {name}! 👋") 
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Personalized Arcade launcher.")
    parser.add_argument('-n', '--name', default="player 1", help='Player name')
    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")
    game_on(args.name)
