import random
import tkinter as tk
from tkinter import messagebox

# Class representing a single playing card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # The suit of the card (Hearts, Diamonds, etc.)
        self.rank = rank  # The rank of the card (2-10, J, Q, K, A)

    # Method to get the value of the card for Blackjack
    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10  # Face cards are worth 10
        elif self.rank == 'A':
            return 11  # Ace is worth 11, adjusted later if needed
        return int(self.rank)  # Convert number ranks to integers

    # String representation of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Class representing a deck of cards
class Deck:
    def __init__(self):
        # Create a list of cards (all combinations of ranks and suits)
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(suit, rank) for rank in ranks for suit in suits]
        self.shuffle()  # Shuffle the deck when created

    # Shuffle the deck randomly
    def shuffle(self):
        random.shuffle(self.cards)

    # Deal the top card from the deck
    def deal(self):
        return self.cards.pop()

# Class representing a player's or dealer's hand
class Hand:
    def __init__(self):
        self.cards = []  # List to hold cards in hand
        self.aces = 0  # Count of aces in hand

    # Add a card to the hand
    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.aces += 1  # Increment ace count

    # Calculate the total value of the hand
    def hand_value(self):
        total = sum(card.value() for card in self.cards)  # Sum values of all cards
        # Adjust for aces if total exceeds 21
        while total > 21 and self.aces:
            total -= 10  # Count an Ace as 1 instead of 11
            self.aces -= 1  # Decrement ace count
        return total

    # Check if the hand is a Blackjack (two cards worth 21)
    def is_blackjack(self):
        return len(self.cards) == 2 and self.hand_value() == 21

    # String representation of the hand
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Class to manage the Blackjack game logic and GUI
class BlackJackGame:
    def __init__(self, root):
        self.root = root  # Reference to the main window
        self.root.title("Blackjack Game")  # Set window title
        self.create_widgets()  # Create GUI elements
        self.new_game()  # Start a new game

    # Create and layout the GUI elements
    def create_widgets(self):
        self.player_label = tk.Label(self.root, text="Player's hand:")
        self.player_label.pack()

        self.player_hand_label = tk.Label(self.root, text="")
        self.player_hand_label.pack()

        self.dealer_label = tk.Label(self.root, text="Dealer's hand:")
        self.dealer_label.pack()

        self.dealer_hand_label = tk.Label(self.root, text="")
        self.dealer_hand_label.pack()

        # Buttons for player actions
        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT)

        self.stand_button = tk.Button(self.root, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.LEFT)

        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()

        self.restart_button = tk.Button(self.root, text="Play Again", command=self.new_game)
        self.restart_button.pack()

        # Disable buttons until a game starts
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.DISABLED)

    # Start a new game
    def new_game(self):
        self.deck = Deck()  # Create a new deck
        self.player_hand = Hand()  # Initialize player's hand
        self.dealer_hand = Hand()  # Initialize dealer's hand

        # Deal two cards to both player and dealer
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

        self.update_display()  # Update the display of hands
        self.hit_button.config(state=tk.NORMAL)  # Enable the Hit button
        self.stand_button.config(state=tk.NORMAL)  # Enable the Stand button
        self.restart_button.config(state=tk.DISABLED)  # Disable Play Again button

    # Update the displayed hands and check for Blackjack
    def update_display(self):
        self.player_hand_label.config(text=str(self.player_hand))  # Show player's hand
        self.dealer_hand_label.config(text=str(self.dealer_hand.cards[0]))  # Show one dealer card

        # Check for Blackjacks
        if self.player_hand.is_blackjack() and self.dealer_hand.is_blackjack():
            self.message_label.config(text="Both Player and Dealer have a Blackjack! It's a tie!")
            self.end_game()
        elif self.player_hand.is_blackjack():
            self.message_label.config(text="Player has a Blackjack! Player wins!")
            self.end_game()
        elif self.dealer_hand.is_blackjack():
            self.message_label.config(text="Dealer has a Blackjack. Dealer wins.")
            self.end_game()

    # Handle player hitting (taking another card)
    def hit(self):
        self.player_hand.add_card(self.deck.deal())  # Add a new card to the player's hand
        self.update_display()  # Update the display

        # Check if player has busted (over 21)
        if self.player_hand.hand_value() > 21:
            self.message_label.config(text="Player busts, Dealer wins.")
            self.end_game()

    # Handle player standing (ending their turn)
    def stand(self):
        # Dealer draws cards until they reach 17 or higher
        while self.dealer_hand.hand_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())
        self.update_display()  # Update the display after dealer's turn

        # Determine the outcome of the game
        if self.dealer_hand.hand_value() > 21:
            self.message_label.config(text="Dealer busts, Player wins!")
        elif self.player_hand.hand_value() > self.dealer_hand.hand_value():
            self.message_label.config(text="Player wins!")
        elif self.player_hand.hand_value() < self.dealer_hand.hand_value():
            self.message_label.config(text="Dealer wins.")
        else:
            self.message_label.config(text="It's a tie.")

        self.end_game()  # End the game after standing

    # Disable game buttons and enable restart
    def end_game(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)

# Main function to run the game
def main():
    root = tk.Tk()  # Create the main window
    app = BlackJackGame(root)  # Initialize the Blackjack game
    root.mainloop()  # Start the GUI event loop

# Entry point for the program
if __name__ == "__main__":
    main()
