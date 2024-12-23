# Imports
import random

class Cards:
    # Class attributes
    class_attribute = "I belong to the class Cards"
    
    def __init__(self, value, suit):
        # Instance attributes
        self.value = value
        self.suit = suit
    
    # Method
    def display_value(self):
        print(f"{self.value} of {self.suit}")


### Variables and objects ###

# Variables

# Lists
cards_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
cards_suit = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Create a deck of cards using list comprehension from the lists above
deck = [(value,suit) for value in cards_value for suit in cards_suit]

# Create two empty lists to represent the hands of the players
player1_hand = []
player2_hand = []

# Update the players' hands by randomly assigning half of the deck to each player

# Shuffle the deck
random.shuffle(deck)

# Split the deck in half # Find the half way point of the deck
half_deck = len(deck)//2

# Assign the first half of the deck to player 1
# Explaining how the : works
# player1_hand = deck[start:half_deck] # the start point is the first card (index 0) up to the half way point (half_deck) # we don't have to pass out cards 1 by 1 because random shuffle will take care of that
player1_hand = deck[:half_deck]

# Assign the second half of the deck to player 2
# Explaining how the : works
# player2_hand = deck[half_deck:end] # the start point is the half way point (half_deck) up to the last card (index -1) # we didn't have to put start/index0 or end/index-1 because it's assumed by the : operator (it's default)
player2_hand = deck[half_deck:]


# Game loop

print("Welcome the game of WAR!!!")
print("Player 1 will play first and then Player 2 will play")
print("The game will continue until both players have no cards left in their hands")

input("Please press enter to play your card Player 1")
# Remove the first card from each player's hand and set it to a variable to represent the card played
player1_played_card = player1_hand.pop(0)
player2_played_card = player2_hand.pop(0)

# Print the cards in play
print(f"Player 1 played: {player1_played_card}")
print(f"Player 2 played: {player2_played_card}")

# Compare the values of the cards in play
### !!! --- I need to fix this part --- !!! ###
# Because we have not clarified what numerical value the face cards have, the logic below fails to compare strings to integers

# If player 1 wins, they get both cards
if player1_played_card > player2_played_card:
    # Print the winner of the round
    print("Player 1 wins this round")
    # Add the played cards to player 1's hand
    player1_hand.append(player1_played_card)
    player1_hand.append(player2_played_card)

# If player 2 wins, they get both cards
elif player2_played_card > player1_played_card:
    # Print the winner of the round
    print("Player 2 wins this round")
    # Add the played cards to player 2's hand
    player2_hand.append(player1_played_card)
    player2_hand.append(player2_played_card)
    
# If it's a tie, the players go to WAR!
else:
    # Print that it's a tie and it's time for WAR!
    print("It's a tie! Time for WAR!")
    
    # Each player plays 3 cards face down # pop 3 cards out of each player's hand list
    player1_facedown_cards = [player1_hand.pop(0) for i in range(3)]
    player2_facedown_cards = [player2_hand.pop(0) for i in range(3)]
    
    # Each player plays 1 card face up
    player1_faceup_card = player1_hand.pop(0)
    player2_faceup_card = player2_hand.pop(0)
    
    # Print the cards in play
    print(f"Player 1's face up card is: {player1_faceup_card}")
    print(f"Player 2's face up card is: {player2_faceup_card}")
    
    # If player 1 wins the faceup card, they get all the cards
    if player1_faceup_card > player2_faceup_card:
        # Print the winner of the round
        print("Player 2 won WAR! They get all the cards")
        # Add all the played cards to Player 1's hand
        # Player 1's first played card
        player1_hand.append(player1_played_card)
        # Player 2's first played card
        player1_hand.append(player2_played_card)
        # Player 1's WAR facedown cards
        player1_hand.extend(player1_facedown_cards)
        # Player 2's WAR facedown cards
        player1_hand.extend(player2_facedown_cards)
        # Player 1's WAR faceup card
        player1_hand.append(player1_faceup_card)
        # Player 2's WAR faceup card
        player1_hand.append(player2_faceup_card)
        
    # If player 2 wins the faceup card, they get all the cards
    elif player2_faceup_card > player1_faceup_card:
        # Print the winner of the round
        print("Player 2 won WAR! They get all the cards")
        # Add all the played cards to Player 2's hand
        # Player 1's first played card
        player2_hand.append(player1_played_card)
        # Player 2's first played card
        player2_hand.append(player2_played_card)
        # Player 1's WAR facedown cards
        player2_hand.extend(player1_facedown_cards)
        # Player 2's WAR facedown cards
        player2_hand.extend(player2_facedown_cards)
        # Player 1's WAR faceup card
        player2_hand.append(player1_faceup_card)
        # Player 2's WAR faceup card
        player2_hand.append(player2_faceup_card)
        
    # If it's a tie again, the players go to WAR again!
    # Normally they go to war again, but I am going to end the game here so I can figure this out later
    else:
        print("It's a tie again! The game is over!")
        
# Print the number of cards in each player's hand
print(f"Player 1 has {len(player1_hand)} cards")
print(f"Player 2 has {len(player2_hand)} cards")



input("Press enter to exit")


# How to view each player's hand # the values stored in those lists
#print(f"Player 1 Hand: {player1_hand}")
#print(f"Player 2 Hand: {player2_hand}")