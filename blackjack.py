#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:40:14 2020

@author: clairepeng
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Apr  5 18:57:05 2020

@author: clairepeng

"""

# Create a deck of 52 cards

import random

suits = ('♥','♣','♠','♦')
ranks = ('two','three','four','five','six','seven',
         'eight','nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,
         'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.rank} {self.suit}'

test_card = Card('♠','2')
#print(test_card)


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = '' # start with an empty string
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self): # Shuffle the deck
        random.shuffle(self.deck)

    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card

test_deck = Deck()
test_deck.shuffle()
# print(test_deck)
# print(test_deck.deal())

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        # from Deck.deal() --> dealt_card
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'ace':
            self.aces += 1 # add to self.aces

    def adjust_for_ace(self):
        
        # If total value > 21 and I have an ace
        # then change my ace to be 1 instead of 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1    
             
test_hand = Hand()
# test_hand.add_card(test_card)
# print(test_hand.value())

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self):
        
        while True: #Ask the Player for their bet
            try:
                self.bet = int(input('How many chips would you like to bet? '))

            except ValueError:
                print('Sorry, a bet must be an integer!')

            except Exception as e:
                print(e)

            else: #Make sure that the Player's bet does not exceed their available chips
                if self.bet > self.total:
                    print(f"Sorry, your bet can't exceed {self.total}")
                    continue
                elif self.bet <= 0:
                    print(f"Sorry, your bet must be above 0.")
                    continue
                else:
                    print(f'You have bet {self.bet} chips for this game.')
                    break

class Play:

    def hit(self,deck,hand):
        # This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17.
        hand.add_card(deck.deal())
        hand.adjust_for_ace()


    def hit_or_stand(self,deck,hand):
        global playing  # to control an upcoming while loop
        
        hit_or_stand = ''
        
        while hit_or_stand != 'h' and hit_or_stand != 's':
            hit_or_stand = input('Hit or stand? Enter "h" or "s"').lower()[0]
            
            if hit_or_stand == 'h':
                self.hit(deck,hand)
                break

            elif hit_or_stand == 's':
                print("Player stands. Dealer is playing.")
                playing = False
                break
            
    def display_some(self,dealer,player):
        print("\n\nDealer's Hand", "<card hidden>" ,dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='  ')
        
    def display_all(self,dealer,player):
        print("\n\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =",dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =",player.value)
                
    def player_busts(self,chips):
        print("\n\nPlayer busts!")
        chips.lose_bet()

    def player_wins(self,chips):
        print("\n\nPlayer wins!")
        chips.win_bet()

    def dealer_busts(self,chips):
        print("\n\nDealer busts!")
        chips.win_bet()
        
    def dealer_wins(self,chips):
        print("\n\nDealer wins!")
        chips.lose_bet()
        
    def push(self):
        print("\n\nDealer and Player tie! It's a push.")

    #test_play = Play(deck,hand)
    #test_play.hit_or_stand(test_deck,test_hand)
    
    def replay(self):
    
        while True:
            replay = input('Are you going to play again? y or n')
            
            if replay == 'y':
                return True
            
            elif replay == 'n':
                print('Goodbye')
                return False
            
            else:
                continue


if __name__ == '__main__':
    
    player_chips = Chips()
    
    while True:
    # Print an opening statement
        print('Hello! Welcome to blackjack! \nDealer hits until she reaches 17. Aces count as 1 or 11.')
    
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        
        
        # Set up the Player's chips
        
    
        # Prompt the Player for their bet
        player_chips.take_bet()
        
    
        # Show cards (but keep one dealer card hidden)
        play = Play()
        play.display_some(dealer_hand,player_hand)

    
        # while playing:  # recall this variable from our hit_or_stand function
        playing = True
        while playing:
        
            # Prompt for Player to Hit or Stand
            play = Play()
            play.hit_or_stand(deck,player_hand)
        
            # Show cards (but keep one dealer card hidden)
            play.display_some(dealer_hand,player_hand)
        
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                play.player_busts(player_chips)
                playing = False
            

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                play.hit(deck,dealer_hand)
                
        # Show all cards
            play.display_all(dealer_hand,player_hand)
    
            # Run different winning scenarios
            if dealer_hand.value > 21:
                play.dealer_busts(player_chips)
                
            elif dealer_hand.value < player_hand.value:
                play.player_wins(player_chips)
                
            elif dealer_hand.value > player_hand.value:
                play.dealer_wins(player_chips)
                
            else:
                play.push()
        
        # Inform Player of their chips total 
        print(f'\nYou have {player_chips.total} chips now.')
    
        # Ask to play again
        if not play.replay():
            break