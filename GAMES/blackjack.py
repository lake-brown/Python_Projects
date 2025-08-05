import random

# Constants for suits, ranks, and card values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
    'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':11
}

# Game control flag to control player's turn
playing = True

# Card class to represent each card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

# Deck class to create a deck of 52 cards, shuffle and deal cards
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def __str__(self):
        return 'The deck has:' + ''.join(f'\n{card}' for card in self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# Hand class to keep track of cards in hand, their value, and aces for adjustment
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # Number of aces counted as 11

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    # Adjust ace values from 11 to 1 if total value goes over 21
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Chips class to manage player's total chips and bets
class Chips:
    def __init__(self):
        self.total = 100  # Starting chips
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# Function to take a bet from the player, with validation
def take_bet(chips):
    # Check if player has any chips left
    if chips.total <= 0:
        print("You have no chips left to bet. Game over!")
        return False  # Signal to end game

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, bet must be a number.')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips. You have {chips.total}.')
            elif chips.bet <= 0:
                print('Bet must be greater than 0.')
            else:
                return True  # Valid bet accepted

# Function to add a card to a hand (hit)
def hit(deck, hand):
    hand.add_card(deck.deal())

# Function to ask player to hit or stand during their turn
def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter 'h' or 's': ")

        if not x:
            print("Please enter 'h' or 's' only.")
            continue

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer's turn.")
            playing = False
        else:
            print("Please enter 'h' or 's' only.")
            continue
        break

# Function to display some cards: dealer's first card hidden, player's all cards shown
def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n')

# Function to display all cards and values for both dealer and player
def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand value:", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("Player's Hand value:", player.value)

# Game outcome functions
def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.")

# Main game loop
player_chips = Chips()  # Initialize chips once before game starts

while True:
    print("\nWelcome to Blackjack!")

    # Check if player has chips to play
    if player_chips.total <= 0:
        print("You have run out of chips! Game over.")
        break

    # Create and shuffle deck
    deck = Deck()
    deck.shuffle()

    # Deal two cards to player and dealer
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Take player's bet; if player cannot bet, end game
    if not take_bet(player_chips):
        break

    # Show cards (dealer shows one card hidden)
    show_some(player_hand, dealer_hand)

    playing = True  # Player's turn flag

    # Check for immediate blackjack for player and dealer
    if player_hand.value == 21:
        show_all(player_hand, dealer_hand)
        if dealer_hand.value == 21:
            push(player_hand, dealer_hand)
        else:
            print("Blackjack! Player wins automatically.")
            player_chips.win_bet()
    else:
        # Player's turn: hit or stand
        while playing:
            hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # Dealer's turn, if player hasn't busted
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards and values
            show_all(player_hand, dealer_hand)

            # Determine outcome
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

    # Display player's total chips after the round
    print(f"\nPlayer's total chips: {player_chips.total}")

    # Ask player if they want to play again
    new_game = input("Would you like to play another hand? (y/n): ")

    if new_game[0].lower() != 'y':
        print("Thanks for playing!")
        break
