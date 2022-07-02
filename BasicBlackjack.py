"""
Basic Blackjack --- play a game of basic blackjack against the computer
"""

import random


computer_total = random.choice([1,2,3,4,5,6,7,8,9,10,10,10,10,11])   
user_total = random.choice([1,2,3,4,5,6,7,8,9,10,10,10,10,11])
user_total += random.choice([1,2,3,4,5,6,7,8,9,10,10,10,10,11])
must_hit = 16

print("your cards equal "+ str(user_total) + " and dealer is showing " + str(computer_total))

user_input = input("Hit (h) or stay (s) or quit (q)? ").lower()

def winner(computer_total, user_total):
    if user_total < computer_total and computer_total <= 21:
        print("Oh no! you lost. Run program and try again.")
    
    elif user_total > computer_total and user_total <= 21:
        print("Congrats! You won. Run program again if you're feeling lucky.")
    
    elif user_total > 21 and computer_total <= 21:
        print("Oh no! You busted. Run program to try again.")

    elif user_total <= 21 and computer_total > 21:
        print("Dealer busted, you win! Run program to play again.")

    elif user_total == computer_total:
        print("Its a wash! you pushed. Run program to try again.")


while True:
    
    if user_input == "q":
        break
    
    elif user_input == "s":
        
        if computer_total <= must_hit:
            computer_total += random.choice([1,2,3,4,5,6,7,8,9,10,10,10,10,11])
            
            if computer_total > must_hit:
                print("your total is " + str(user_total) + " dealer has " + str(computer_total))
                winner(computer_total, user_total)
                break
    
    elif user_input == "h":

        user_total += random.choice([1,2,3,4,5,6,7,8,9,10,10,10,10,11])
        hit_input = input(" your total is " + str(user_total) + " and dealer has " + str(computer_total) + " would you like to hit (h) or stay? (s) ")
            
        if hit_input == "h":
            continue
        
        while hit_input == "s" and computer_total <= must_hit:
            computer_total += random.choice([1,2,3,4,5,6,7,8,9,10,10,10,10,11])

            if computer_total > 16:
                print(" your total is " + str(user_total) + " and dealer has " + str(computer_total))
                winner(computer_total, user_total)
                break
        break
    
    else:
        print("Run program again, and try a valid input: (h), (s), (q)")
        break
        

    
