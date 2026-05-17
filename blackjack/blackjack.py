import random as rd

import art

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]  # 11 is Ace

def adjust_for_ace(deck):
    #If total is over 21 and there’s an Ace (11), turn it into 1.
    while sum(deck) > 21 and 11 in deck:
        deck[deck.index(11)] = 1
    return deck

def first_deal():
    return [rd.choice(cards), rd.choice(cards)]

def score(deck):
    return sum(deck)

age = input("Are you above 18? Type yes or no: ")
if age.lower() != 'yes':
    print("Sorry, you can’t play.")
    exit()

consent = input("Do you want to play Blackjack? Type y or n: ")

if consent == 'y':
    print (art.newlogo)
    your_deck = first_deal()
    dealer_deck = first_deal()

    your_deck = adjust_for_ace(your_deck)
    dealer_deck = adjust_for_ace(dealer_deck)

    while True:
        print(f"Your cards: {your_deck}, current score: {score(your_deck)}")
        print(f"Dealer's first card: {dealer_deck[0]}")

        if score(your_deck) == 21:
            print("Blackjack! You win! 🥳")
            break
        if score(your_deck) > 21:
            print("Bust! You lose 💀")
            break

        next_step = input("Type 'y' to draw another card, 'n' to pass: ")

        if next_step == 'y':
            your_deck.append(rd.choice(cards))
            your_deck = adjust_for_ace(your_deck)
        else:
            while score(dealer_deck) < 17:
                dealer_deck.append(rd.choice(cards))
                dealer_deck = adjust_for_ace(dealer_deck)

            print(f"Your final hand: {your_deck}, final score: {score(your_deck)}")
            print(f"Dealer's final hand: {dealer_deck}, final score: {score(dealer_deck)}")

            if score(dealer_deck) > 21 or score(your_deck) > score(dealer_deck):
                print("You win! 🎉")
            elif score(your_deck) == score(dealer_deck):
                print("Draw 🤝")
            else:
                print("Dealer wins 😬")
                
            break
