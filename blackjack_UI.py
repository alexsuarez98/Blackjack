import random
import tkinter as tk
from tkinter import messagebox

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(suit, rank) for rank in ranks for suit in suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.aces += 1

    def hand_value(self):
        total = sum(card.value() for card in self.cards)
        while total > 21 and self.aces:
            total -= 10
            self.aces -= 1
        return total

    def is_blackjack(self):
        return len(self.cards) == 2 and self.hand_value() == 21

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class BlackJackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        self.player_label = tk.Label(self.root, text="Player's hand:")
        self.player_label.pack()

        self.player_hand_label = tk.Label(self.root, text="")
        self.player_hand_label.pack()

        self.dealer_label = tk.Label(self.root, text="Dealer's hand:")
        self.dealer_label.pack()

        self.dealer_hand_label = tk.Label(self.root, text="")
        self.dealer_hand_label.pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT)

        self.stand_button = tk.Button(self.root, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.LEFT)

        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()

        self.restart_button = tk.Button(self.root, text="Play Again", command=self.new_game)
        self.restart_button.pack()

        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.DISABLED)

    def new_game(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

        self.update_display()
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)

    def update_display(self):
        self.player_hand_label.config(text=str(self.player_hand))
        self.dealer_hand_label.config(text=str(self.dealer_hand.cards[0]))

        if self.player_hand.is_blackjack() and self.dealer_hand.is_blackjack():
            self.message_label.config(text="Both Player and Dealer have a Blackjack! It's a tie!")
            self.end_game()
        elif self.player_hand.is_blackjack():
            self.message_label.config(text="Player has a Blackjack! Player wins!")
            self.end_game()
        elif self.dealer_hand.is_blackjack():
            self.message_label.config(text="Dealer has a Blackjack. Dealer wins.")
            self.end_game()

    def hit(self):
        self.player_hand.add_card(self.deck.deal())
        self.update_display()
        if self.player_hand.hand_value() > 21:
            self.message_label.config(text="Player busts, Dealer wins.")
            self.end_game()

    def stand(self):
        while self.dealer_hand.hand_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())
        self.update_display()

        if self.dealer_hand.hand_value() > 21:
            self.message_label.config(text="Dealer busts, Player wins!")
        elif self.player_hand.hand_value() > self.dealer_hand.hand_value():
            self.message_label.config(text="Player wins!")
        elif self.player_hand.hand_value() < self.dealer_hand.hand_value():
            self.message_label.config(text="Dealer wins.")
        else:
            self.message_label.config(text="It's a tie.")

        self.end_game()

    def end_game(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = BlackJackGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

