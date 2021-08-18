import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "10", "Jack", "Queen", "King"]

# Creating the deck of cards from the initial suits and ranks #
def create_deck(suits, ranks):
    deck = []
    for element in ranks:
        for suit in suits:
            new_card = [element, suit]
            deck.append(new_card)
    return deck

deck = create_deck(suits, ranks)

def shuffle_deck(deck):
    shuffled_deck = random.sample(deck, len(deck))
    return shuffled_deck

print(shuffle_deck(deck))