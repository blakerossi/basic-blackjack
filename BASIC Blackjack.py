import random
computer_total = 0
user_total = 0

computer_total += random.randint(1,11)
    
user_total += random.randint(1,11)
user_total += random.randint(1,11)

print("your cards equal ", user_total, " and dealer is showing", computer_total)

user_input = input("Hit (h) or stay (s) or quit (q)? ").lower()

while True:
    
    if user_input == "q":
        break
    
    elif user_input == "s":
        
        if computer_total <= 16:
            computer_total += random.randint(1,11)
            
        
            if computer_total > 16:
                print("your total is " + str(user_total) + " dealer has " + str(computer_total))
                break
    
    elif user_input == "h":

        user_total += random.randint(1,11)
        hit_input = input(" your total is " + str(user_total) + " and dealer has " + str(computer_total) + " would you like to hit (h) or stay? (s) ")
            
        if hit_input == "h":
            continue
        
        
        while hit_input == "s" and computer_total <= 16:
            computer_total += random.randint(1,11)

            if computer_total > 16:
                print(" your total is " + str(user_total) + " and dealer has " + str(computer_total))
                break
        break
   
        

    

    
        

    
