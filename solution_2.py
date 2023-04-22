#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


def generate_deck(_suits, _cards):
    random.seed(0)
    n = 0
    deck = [(i, j) for i in _suits for j in _cards]
    random.shuffle(deck)
    while True:
        yield deck[n]
        n += 1
        if n == 52:
            random.shuffle(deck)
            n = 0


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shuffled_deck = generate_deck(suits, cards)


def get_next_card():
    return next(shuffled_deck)


# In[2]:


def get_properties():

    global king_total, sage_total, case_S, case_H
    
    king_total = total(king_cards)    
    sage_total = total(sage_cards)
        
    king_cards_list = ''
    for i in range(len(king_cards)):
        if is_king_cards_hidden == True:
            king_cards_list =(f"(*){str(king_cards[1])}")
        else:
            king_cards_list +=str(king_cards[i])
        
    sage_cards_list = ''
    for i in range(len(sage_cards)):
        sage_cards_list +=str(sage_cards[i])
        
    if case_S == False and case_H == False :
        
        print(f"King’s cards: {king_cards_list}")
        print(f"Total value: {king_total}")
        
        print(f"Sage's cards:{sage_cards_list}")
        print(f"Total value: {sage_total}")
        
    if case_S :
        print(f"King's cards:{king_cards_list}")
        print(f"Total value: {king_total}")
        
    if case_H :

        print(f"Sage's cards:{sage_cards_list}")
        print(f"Total value: {sage_total}")


# In[3]:


def total(cards):
    total = 0
    
    for i, card in enumerate(cards):
        if cards == king_cards and i == 0 and is_king_cards_hidden == True:  # skip the first card
            continue
        elif card[1] in ['J', 'Q', 'A']:
            total += 10
        elif card[1] == 'K':
            if card[0] in ['Spades', 'Clubs']:  # black-colored
                total += 11
            else:  # red-colored
                total += 1
        else:
            total += int(card[1])
    return total


# In[4]:


def Game():
    
    global money_of_sage, sage_total,sage_cards,king_cards, is_king_cards_hidden, case_S, case_H
    
    money_of_sage = int(input("Sage's money: "))
    number_of_games = int(input("Number of games: "))
    
    for game in range(1,number_of_games+1):

        sage_cards=[]
        king_cards=[]
        
        is_king_cards_hidden = True

        case_H = False
        case_S = False

        print("Game " + str(game))

        for i in range(2):
            sage_cards.append(get_next_card())

        for i in range(2):
            king_cards.append(get_next_card())

        get_properties()

        if sage_total == 21:

            money_of_sage += 50
            print("It is Blackking! You won!")
            break

        if sage_total > 21:    
            money_of_sage -= 50
            print("You busted! You lost!")

        if sage_total < 21:

            hit_or_stand = str(input("Do you want to hit or stand? [H/S]" ))

            while hit_or_stand == 'H':
                case_H = True
                sage_cards.append(get_next_card())
                get_properties()                

                if sage_total == 21:

                    money_of_sage += 50
                    print("It is Blackking! You won!")
                    break

                if sage_total > 21: 

                    money_of_sage -= 50
                    print("You busted! You lost!")
                    break

                if sage_total < 21:

                    hit_or_stand = str(input("Do you want to hit or stand? [H/S]" ))

            while hit_or_stand == 'S':
                case_S = True
                case_H = False
                is_king_cards_hidden = False
                get_properties()
                
                while king_total < 17:

                    king_cards.append(get_next_card())
                    get_properties()

                if king_total > 21: 

                    money_of_sage += 50
                    print("King busted! You won!")
                    break

                if king_total >= 17:

                    if king_total > sage_total:
                        money_of_sage -= 50
                        print("King has higher value. You lost!")
                        break
                    if king_total < sage_total:
                        money_of_sage += 50
                        print("You have higher value. You won!")
                        break
                    if king_total == sage_total:
                        print("It is a tie!")
                        break


            if game == number_of_games:
                print(f"Final money is {money_of_sage}")


# In[5]:


Game()

