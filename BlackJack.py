# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:53:14 2019

@author: Shravan
"""

import random

suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return "{r} of {s}".format(s=self.suit,r=self.rank)
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        print(len(self.deck))
        deck_comp=' '
        for card in self.deck:
            deck_comp+= '\n'+card.__str__()
        return "The deck has :" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
    
    def adjust_for_ace(self):
        while (self.value)>21 and self.aces>0:
            self.value-=10
            self.aces-=1
        return self.value
    

class Chips:
    
    def __init__(self,total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    while(True):
        try:
            chips.bet=int(input("How many chips do you want to play?"))
        except:
            print("Enter again!")
            continue
        else:
            if chips.bet>chips.total:
                print("You do not have enough chips .Please enter correctly.")
                print("Chips left :",chips.total)
                continue
            print("\nAmount Entered :",chips.bet)
            print("Chips left :",chips.total)
            break

def hit(deck,hand):
    new_card=deck.deal()
    hand.add_card(new_card)
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True :
        x=str(input("Hit or Stand? h or s"))
        if x[0].lower()=="h":
            hit(deck,hand)
        elif x[0].lower()=="s":
            print("Player stands. It's Dealer's Turn.")
            playing=False
        else:
            print("Invalid!Please Enter again.")
            continue
        break
        
def show_some(player,dealer):
    print("\nPlayer's Cards\n")
    for i in player.cards :
        print(i)
    print("\nDealer's Cards\n")
    for j in dealer.cards[:-1]:
        print(j)
    
    #for i in range (0,len(dealer.cards)-1):
        #print(dealer.cards)
    
    
def show_all(player,dealer):
    print("\nPlayer's Cards\n")
    for i in player.cards :
        print(i)
    print("\nDealer's Cards\n")
    for j in dealer.cards:
        print(j)
    pass


def player_busts(player,dealer,chips):
    print("Player BUST")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player WINS")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer BUST")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer WINs")
    chips.lose_bet()
    
def push(player,dealer):
    print("Player and Dealer Tied. PUSH")
    pass


while True:

    print("******Welcome to Black Jack******")

    deck=Deck()
    deck.shuffle()
    
    player_hand=Hand()
    dealer_hand=Hand()
    
    for i in range (0,2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    
    player_chips=Chips(1000)
    
    
    print("Place the bet:")
    take_bet(player_chips)
    show_some(player_hand,dealer_hand)
    
    while playing:  
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value<=21:
            
        while dealer_hand.value<17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    print("Total no. of chips:",player_chips.total)
    new_game = input("Would you like to play another hand? Enter (y/n) ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
    

