import random

cards = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9" "10", "Jack", "Queen", "King"]
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

newCard = (random.choice(cards) + " of " + random.choice(suits))

print("You have drawn the " + newCard)