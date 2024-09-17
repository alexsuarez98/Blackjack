import random
import numpy as np

class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

#initializes the card class with suit and rank attributes

  def value(self):
    if self.rank in ['J', 'Q', 'K']:
      return 10
    elif self.rank == 'A':
      return 11
    return int(self.rank)

#returns the value of the card based on its rank

  def __str__(self):
    return f"{self.rank} of {self.suit}"

#returns a string of the card in "rank of suit"

class Deck:
  def __init__(self):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    self.cards = [Card(suit, rank) for rank in ranks for suit in suits]
    self.shuffle()
    #creates the deck with 52 cards
    '''
    iterates through each suit and rank creating a card, first goes through each suit ex. 
    hearts, diamonds, clubs, spades, then adds the rank to the card, ex. 2 of hearts then 
    resets and goes onto next rank
    '''
  def shuffle(self):
    random.shuffle(self.cards)
    #shuffles the deck using the random module

  def deal(self):
    return self.cards.pop()
    #removes and returns the last card in the deck

class Hand:
  def __init__(self):
    self.cards = []
    self.aces = 0
  #creates an empty list for the cards in the hand and keeps track of aces to be 
  #adjusted based on player's hand

  def add_card(self, card):
    self.cards.append(card)
    if card.rank == 'A':
      self.aces += 1
      #adds a card to the hand and increases the ace count if the card is an ace

  def hand_value(self):
    total = sum(card.value() for card in self.cards)
    while total > 21 and self.aces:
      total -= 10
      self.aces -= 1
      '''
      if there is an ace in the hand and the total value is greater than 21, the ace's 
      value will change to 1 and the ace count will be decreased by 1 so if the player 
      gets another ace the same rule will apply
      '''
    return total
   
  def is_blackjack(self):
     return len(self.cards) == 2 and self.hand_value() == 21
     #Checks if the hand is a blackjack

  def __str__(self):
     return ', '.join(str(card) for card in self.cards)
     #returns a string of the cards in the hand

def play_game():
  deck = Deck()
  player_hand = Hand()
  dealer_hand = Hand()
  #creates the deck, player hand, and dealer hand
  number_of_cards_dealer = len(player_hand.cards)
  number_of_cards_player = len(player_hand.cards)

  for _ in range(2):
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    #deals two cards to the player and dealer
  
  print("Player's hand:", player_hand)
  print("Dealer's hand:", dealer_hand.cards[0])
  #prints the player's hand and the dealer's first card

  if player_hand.is_blackjack() and dealer_hand.is_blackjack():
    print("Both Player and Dealer have a BlackJack! It's a tie!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
     print()
     print("-----------------------------")
     print()
     play_game()
    return
  elif player_hand.is_blackjack():
    print("Player has a Blackjack! Player wins!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
      print()
      print("-----------------------------")
      print()
      play_game()
    return
  elif dealer_hand.is_blackjack():
    print("Dealer has a Blackjack. Dealer wins.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
      print()
      print("-----------------------------")
      print()
      play_game()
    return
  #checks for blackjacks and exits the function after

  while player_hand.hand_value() < 21 :
    action = input("Do you want to hit or stand? ").lower()
    if action == 'hit':
      player_hand.add_card(deck.deal())
      print(f"\nPlayer's hand: {player_hand}")
      if player_hand.hand_value() > 21:
       print("\nDealer's hand:", dealer_hand)
       print("\nPlayer busts, Dealer wins.")
       play_again = input("Do you want to play again? (yes/no): ").lower()
       if play_again == 'yes':
         print()
         print("-----------------------------")
         print()
         play_game()
      return
    else:
      break
      #asks the player if they want to hit or stand, if they hit it will add a card to 
      #the player's hand and print it, if they stand it will break the while loop
      #if the player busts then the function stops and the game ends
  
  while dealer_hand.hand_value() < 17:
    dealer_hand.add_card(deck.deal())
    #adds a card to the dealer's hand until it has a value of 17 or more

  
  if dealer_hand.hand_value() > 21:
    print("\nDealer's hand:", dealer_hand)
    print("\nDealer busts, Player wins!")
  elif player_hand.hand_value() > dealer_hand.hand_value():
    print("\nDealer's hand:", dealer_hand)
    print("\nPlayer wins!")
  elif player_hand.hand_value() < dealer_hand.hand_value():
    print("\nDealer's hand:", dealer_hand)
    print("\nDealer wins.")
  else:
    print("\nDealer's hand:", dealer_hand)
    print("\nIt's a tie.")
    #checks the value of the player's and dealer's hand to determine the winner
  play_again = input("Do you want to play again? (yes/no): ").lower()
  if play_again == 'yes':
    print()
    print("-----------------------------")
    print()
    play_game()
    

play_game()
