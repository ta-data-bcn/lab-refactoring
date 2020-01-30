#!/usr/bin/env python
# coding: utf-8

# # Welcome to the Blackjack game

# In the following we will try to beat the dealer in a very simple game. To read the rules please go to README.

# ## Cards

# There are 52 cards in one set. In the casino more than one set is used. Although in this case we only use one set:

# <img src="images-1-4.jpeg">

# In[1]:


#code to define all the cards
cards = {"s-Ace":11, "s-King":10, "s-Queen":10, "s-Jack":10, "s-10":10, "s-9":9, "s-8":8, "s-7":7, "s-6":6, "s-5":5, "s-4":4, "s-3":3, "s-2":2, "c-Ace":11, "c-King":10, "c-Queen":10, "c-Jack":10, "c-10":10, "c-9":9, "c-8":8, "c-7":7, "c-6":6, "c-5":5, "c-4":4, "c-3":3, "c-2":2, "d-Ace":11, "d-King":10, "d-Queen":10, "d-Jack":10, "d-10":10, "d-9":9, "d-8":8, "d-7":7, "d-6":6, "d-5":5, "d-4":4, "d-3":3, "d-2":2, "h-Ace":11, "h-King":10, "h-Queen":10, "h-Jack":10, "h-10":10, "h-9":9, "h-8":8, "h-7":7, "h-6":6, "h-5":5, "h-4":4, "h-3":3, "h-2":2}
print(cards)


# ## First round

# In the first round the dealer will hand out 2 cards to the user. The dealer itself will get 1 card to give the user a hint what the hand of the dealer at the end could be. So summarised in this round gets:
# - the user 2 cards
# - the dealer 1 card

# <img src="Blackjack_game_1.jpg">

# In[10]:


#1st and 2nd card of the user

import random

#1st card
first_card_user = random.choice(list(cards.keys()))
print("Your first card is: "+first_card_user)
user_cards=[cards[first_card_user]]
del cards[first_card_user]

#2nd card
second_card_user = random.choice(list(cards.keys()))
print("Your second card is: "+second_card_user)
user_cards.append(cards[second_card_user])
del cards[second_card_user]

#special Ace rule
if sum(user_cards) == 22:
    user_cards[1]=1    

#check, if the user has blackjack with the first two cards
print("This has a value of: " +str(sum(user_cards)))
if sum(user_cards) == 21:
    print("Congrats, you have blackjack and you won")  
    
#dealer's card
else:
    first_card_dealer = random.choice(list(cards.keys()))
    total_dealer=[cards[first_card_dealer]]
    del cards[first_card_dealer]
    print("The first card of the dealer is: "+ first_card_dealer)
    


# ## Further user rounds

# After the user received 2 cards, he can decide how many more cards he wants to receive. He should be as close to 21 but not over it. And do not forget, the Ace can be used as 11 or 1! So summarised in this round:
# - user gets 1 card at a time
# - and decides if he wants another one
# - if he says "stand", the user will keep the points and does not want to have more cards

# <img src="Blackjack.jpg">

# In[ ]:


#further cards of the user
print("User has a toal of " +str(sum(user_cards)))

def furthercards():
    while sum(user_cards)<22:
        third_card_question=input("Do you want another card? (Yes/No): ")
        if third_card_question=="No":
            print("Your Total is "+str(sum(user_cards))+"! Let us see what the dealer has!")
            break
        else:
            third_card_user = random.choice(list(cards.keys()))
            print("Your next card is: " + str(third_card_user))
            user_cards.append(cards[third_card_user])
            del cards[third_card_user]
            if sum(user_cards)>21:
                for i in range(len(user_cards)):
                    if user_cards[i]==11:
                        user_cards[i]=1
                        break
            total=sum(user_cards)
            print("This is a total of: "+ str(total))
            
furthercards()

#in case user has more than 21, he loses straight away
total=sum(user_cards)        
if sum(user_cards)>21:
    print("Your Total is higher than 21, so you LOST!")
    


# ## The dealers round

# The dealer now gets as many cards as he reaches more than 16. If he reaches 17 or more, he is not allowed to take another card. Summarised this round:
# - cards until a number > 16 is reached

# <img src="Blackjack_game_3.jpg">

# In[ ]:


#Dealer

#as long as dealer has a total <17 he has to take another card
while sum(total_dealer)<17:
    card_dealer = random.choice(list(cards.keys()))
    total_dealer.append(cards[card_dealer])
    del cards[card_dealer]
    print("The next card of the dealer is: "+card_dealer)
    print ("This is a total of: "+str(sum(total_dealer)))
    if sum(total_dealer)>21:
        if 11 in total_dealer:
            for i in range(len(total_dealer)):
                if total_dealer[i]==11:
                    total_dealer[i]=1
                    break
        else: print("The dealer has too much, you WON!")
    


# ## The winner is

# - If the user has blackjack (A & 10-card), he wins straight away.
# - If the user has more than 21, he loses
# - If the bank has more than 21 and the user <21, the user wins
# - If the bank has the same amount as the user and both are below 21, it'd be a draw
# - If the user is closer to 21 than the bank, the user wins.

# In[5]:


#result
print ("The dealer has a total of "+str(sum(total_dealer)))
print ("The user has a total of "+ str(total))
if sum(total_dealer)>21:
    print("The dealer has more than 21. So you WON!")
elif sum(total_dealer)>total:
    print("The dealer has more than you. You LOST!")
elif sum(total_dealer)<total:
    print("You beat the dealer. You WON!")
elif sum(total_dealer)==total:
    print("It's a DRAW!")


# In[ ]:




