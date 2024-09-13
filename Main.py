import random

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
playerDeck = []
dealerHand = []

def firstDrawCard ():
    for i in range (0, 2):
        newCard = (random.choice(cards) + " of " + random.choice(suits))
        for i in playerDeck:
           while newCard  in playerDeck or newCard in dealerHand:
              newCard = (random.choice(cards) + " of " + random.choice(suits))
        playerDeck.append(newCard)

    for i in range (0, 2):
        newCard = (random.choice(cards) + " of " + random.choice(suits))
        for i in playerDeck:
           while newCard  in playerDeck or newCard in dealerHand:
              newCard = (random.choice(cards) + " of " + random.choice(suits))
        dealerHand.append(newCard)
    
    
    print("Player's Hand: " + ", " .join(playerDeck))
    print("Player's Hand: " + ", " .join(dealerHand))

def drawCard ():
    newCard = (random.choice(cards) + " of " + random.choice(suits))
    for i in playerDeck:
        while newCard  in playerDeck or newCard in dealerHand:
            newCard = (random.choice(cards) + " of " + random.choice(suits))
    playerDeck.append(newCard)
    print("Player's Hand: " + ", " .join(playerDeck))

print("START GAME")
firstDrawCard()


