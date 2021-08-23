import random


suits = ["A", "B", "C", "D"]
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

def shuffle_deck(deck):
    shuffled_deck = random.sample(deck, len(deck))
    return shuffled_deck

def deal_cards(deck):
    players = [[],[]]
    for card in range(0, 10):
        if card % 2 == 0:
            players[0].append(deck.pop(card))
        elif card % 2 != 0:
            players[1].append(deck.pop(card))
    return players

def update_current_card(current_card):
    pass

def format_deck(player_deck):
    pass

def play_game():
    new_deck = shuffle_deck(create_deck(suits, ranks))
    players = deal_cards(new_deck)
    human_player = players[0]
    ai_player = players[1]
    current_card = [new_deck.pop(0)]

    print("The human:\n{}\n\nThe AI:\n{}\n\nThe current card:\n{}".format(human_player, ai_player, current_card))

play_game()