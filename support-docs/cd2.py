#!/usr/bin/env python3

import random

def main():
    numPlayers = start_game()
    tab1 = Table(numPlayers)
    for j in range(numPlayers):
        tab1.players[j].name = input("Player {0} name: ".format(j + 1))

    nextcard = deal(-1, tab1)

    for pl in range(tab1.noplayers):
        print (tab1.players[pl].name, tab1.players[pl].cards)

    nextcard = nextcard + 2
    print ("Flop: ", " ", end="")
    for j in range(3):
        print (deck.cards[nextcard], " ", end="")
        nextcard = nextcard + 1
    print ()

    nextcard = nextcard + 1
    print ("Turn: ", " ", end="")
    print (deck.cards[nextcard])

    nextcard = nextcard + 2
    print ("River: ", " ", end="")
    print (deck.cards[nextcard])
    print ()

class Card():
    def __init__(self, number):
        random.seed()
        self.ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        self.suits = ["c","d","h","s"]
        self.values = [2,3,5,7,11,13,17,19,23,29,31,37,41]
        self.number = number
    def __str__(self):
        return self.ranks[self.number % 13] + self.suits[int(self.number / 13)]
    def __repr__(self):
        return self.ranks[self.number % 13] + self.suits[int(self.number / 13)]
    def __eq__(self, other):
        return self.number == other.number
    def rank(self):
        return self.ranks[self.number % 13]
    def suit(self):
        return self.suits[int(self.number / 13)]
    def value(self):
        return self.values[self.number % 13]

class Shoe():
    def __init__(self):
        self.cards = []
        for j in range(52):
            self.cards.append(Card(j))
        random.shuffle(self.cards)

class Player():
    def __init__(self, number=0):
        self.number = number
        self.name = ""
        self.cards = []

class Table():
    def __init__(self, noplayers=2):
        self.players = []
        self.noplayers = noplayers
        for j in range(noplayers):
            self.players.append(Player(j))

def deal(d, Table):
    # Initial deal
    c = d
    tab1 = Table
    for holecards in range(2):
        for p in range(tab1.noplayers):
            c = c + 1
            tab1.players[p].cards.append(deck.cards[c])
    return c

def start_game():
    valid_players = (2, 3, 4, 5, 6, 7, 8, 9)
    while True:
        try:
            inputPlayers = input("Number of players: ")
            if inputPlayers:
                numPlayers = int(inputPlayers)
                if numPlayers in valid_players:
                    return numPlayers
                else:
                    print ("Number of players must be between 2 and 9.")
        except ValueError as err:
            print(err)
            continue

deck = Shoe()
for k in range(52):
    c = deck.cards[k]
    if k % 13 == 0:
        print ()
        print (c, "\t", end="")
    else:
        print (c, "\t", end="")

print ()
print ()

main()


"""
$ ./cd.py

5h 	9h 	4c 	Ac 	9s 	Kh 	4h 	Jh 	Ah 	3d 	4d 	Jd 	8s
Js 	4s 	2d 	3s 	5c 	6d 	5s 	Td 	Qd 	9c 	Kc 	3c 	Qc
2c 	Ad 	7d 	7s 	Qh 	Th 	6c 	Qs 	2s 	3h 	7c 	Jc 	Tc
Kd 	Ks 	8h 	2h 	6h 	6s 	8c 	5d 	8d 	9d 	As 	7h 	Ts

Number of players: 3
Player 1 name: Frank
Player 2 name: Bill
Player 3 name: Tony
Ken [5h, Ac]
Bill [9h, 9s]
Tony [4c, Kh]
Flop:   Jh  Ah  3d
Turn:   Jd
River:   Js

"""

