import sys
import random
from enum import Enum
import argparse


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def rps(name):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    
    def decide_winner(player, computer):
        if player == computer:
            return "draw"
        elif (player == RPS.ROCK and computer == RPS.SCISSORS) or \
             (player == RPS.PAPER and computer == RPS.ROCK) or \
             (player == RPS.SCISSORS and computer == RPS.PAPER):
            return "player"
        else:
            return "computer"
    
    def play_rps():
        nonlocal player_wins, computer_wins, game_count
        
        while True:
            try:
               player_choice = int(input(f"Hello {name}, enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n "))

            except ValueError:
                print("Please enter a valid number: 1, 2, or 3.")
                continue
            
            if player_choice not in [1, 2, 3]:
                print("You must enter 1, 2, or 3.")
                continue
            
            player = RPS(player_choice)
            computer = RPS(random.randint(1, 3))
            
            print(f"{name} chose {player.name}.")
            print(f"Computer chose {computer.name}.\n")
            
            result = decide_winner(player, computer)
            
            if result == "player":
                player_wins += 1
                print("🎉 You win!\n")
            elif result == "computer":
                computer_wins += 1
                print("Computer wins!\n")
            else:
                print("😲 It's a draw!\n")
            
            game_count += 1
            
            print(f"Game count: {game_count}")
            print(f"{name}'s wins: {player_wins}")
            print(f"Computer wins: {computer_wins}\n")
            
            play_again = input("Would you like to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"\n🎉🎉🎉🎉")
                
                return
    
    play_rps()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    
    rps(args.name)
