#!/usr/bin/env python3

import random

def define_cards():
    card_rank = ("2","3","4","5","6","7","8","9","T","J","Q","K","A")
    card_suit = ("c","d","h","s")
    rank_string = ("2","3","4","5","6","7","8","9","T","J","Q","K","A")
    suit_string = ("c","d","h","s")
    cards = []
    for suit in range(4):
        for rank in range(13):
            card_string = rank_string[rank] + suit_string[suit]
            cards.append(card_string)
    return cards


def deal_card(deck):
    return deck.pop(0)
    
deck = define_cards()

print()
print(deck)

print()
print("Shuffling...")
print()
random.shuffle(deck)

print(deck)
