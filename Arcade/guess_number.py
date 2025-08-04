import sys
import random
import argparse


def guess(name):
    while True:
        computer_choice = random.randint(1, 3)

        try:
            player_choice = int(input(f"{name}, pick a number between 1 and 3: "))
        except ValueError:
            print("Pick a number between 1 and 3.")
            continue  # keep asking

        if player_choice == computer_choice:
            print(f"🎉 YOU WIN!\nMy number was {computer_choice}, you guessed {player_choice}")
        else:
            print(f"😢 YOU LOSE!\nMy number was {computer_choice}, you guessed {player_choice}")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Thanks for playing, {name}!")
        
            return 
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guess a number game.")

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True,
        help="The name of the person playing the game."
    )

    args = parser.parse_args()
    guess(args.name)
