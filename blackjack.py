from random import shuffle
from termcolor import colored
import colorama

colorama.init()

suits = ('Heart',"Spade","Club","Diamond")
# ranks = ("2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace")
ranks = ("2","King","Ace")


values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

adce_dic = {}

def add_ace(card):
    if card.split()[0] == "Ace":
        adce_dic[card] = 1

def check_ace():
    global player_score
    for i in adce_dic:
        if adce_dic[i] == 1:
            player_score -= 10
            adce_dic[i] = 0

# create card
def create_card(rank,suit):
    return rank + ' of ' + suit


# 5 of Heart
# print(create_card("8","Spade"))

# create deck
deck = []
total_chips = 100
player_score = 0
dealer_score = 0
def create_deck():
    for suit in suits: # Heart
        for rank in ranks: # 2 - Ace
            deck.append(create_card(rank,suit))

# take bet
def take_bet():
    while True:
        bet = int(input("Enter your bet."))
        if bet >0 and bet<=100:
            return bet
        else:
            print(f"You don't have enough chips. You have only {total_chips}")
           
def show_some():

    print(colored("Players's card","cyan"))
    for i in player_cards:
        print(i)

    print()
    print(colored("Dealer's card","cyan"))
    for i in dealer_cards:
        if dealer_cards.index(i) == 0:
            print("One card is hidden")
        else:
            print(i)

def show_all():
    
    print(colored("Players's card","cyan"))
    for i in player_cards:
        print(i)

    print()
    print(colored("Dealer's card","cyan"))
    for i in dealer_cards:
        print(i)

# 100 chips + 50 = 150 # 100 - 50 = 50


def player_score_count():
    global player_score
    for card in player_cards:
        # d = {'a':10} d['a']
        # "Ace of Spade" -> ["Ace","of","Spade"][0] -> value['Ace'] - > 11
        # print(values[card.split()[0]])
        player_score += values[card.split()[0]]
        add_ace(card)

    if player_score > 21:
        check_ace()
    

def dealer_score_count():
    global dealer_score
    for card in dealer_cards:
        # d = {'a':10} d['a']
        # "Ace of Spade" -> ["Ace","of","Spade"][0] -> value['Ace'] - > 11
        # print(values[card.split()[0]])
        dealer_score += values[card.split()[0]]
        
def hit_or_stand():
    global player_score
    global playing
    while True:
        ask = input("Enter hit or Stand. H or S") # hit h h
        if ask.lower() == 'h':
            card = deck.pop()
            player_cards.append(card)
            add_ace(card)
            player_score += values[card.split()[0]]
            if player_score > 21:
                check_ace()
            break
        elif ask.lower() == 's':
            playing = False
            break
        else:
            print(colored("you have entered the wrong input."))

# Game begins

print("Welcome To Black Jack")

create_deck()
shuffle(deck)
# print(deck)

bet = take_bet()
# print(bet)

player_cards = []
dealer_cards = []
shuffle(deck)

player_cards.append(deck.pop())
player_cards.append(deck.pop())

dealer_cards.append(deck.pop())
dealer_cards.append(deck.pop())


player_score_count()
print(player_score)


# player's turn 
playing = True

while playing:
    show_some()
    if player_score == 21:
        print("You hit blackjack, you won")
        break
    elif player_score > 21:
        print("You burst, You loose")
        break
    else:
        hit_or_stand()



# dealer turn's
if player_score < 21:
    show_all()
    dealer_score_count()

    while dealer_score < 17:

        card = deck.pop()
        dealer_cards.append(card)
        dealer_score += values[card.split()[0]]
        show_all()
    
    if dealer_score == 21:
        print("Dealer hit the blackjack, you loose")
    elif dealer_score > 21:
        print("Dealer burst, You won")
    elif dealer_score > player_score:
        print("Dealer won")
    elif player_score > dealer_score:
        print("Player won")
    else:
        print("tie")


    

