import random 

start = 1
finish = 30
number_to_guess = random.randrange(start, finish + 1) 
chances = 10
guess_counter = 0

print(f"Hi, Welcome to the game. This is a number guessing game.\nTry guessing the number from {start} to {finish}.\nYou have {chances} chances to guess. Let's start the game.")

# correct number 
print(f"The number is *** {number_to_guess} ***")

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please enter your guess number : "))

    if my_guess == number_to_guess:
        print(f"Congratulations! Your guess number {my_guess} is correct.\nYou found it in the {guess_counter} attempt.")
        break
        
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Sorry! Your chances are all used up. Better luck next time.")
        
    elif 0 < my_guess - number_to_guess <= 5:
        print("You are almost there. Trying guessing a bit lower.")
        
    elif my_guess > number_to_guess:
        print("Your guess is high. Trying guessing lower.")   
    
    elif number_to_guess - my_guess <= 5 :
        print("You are almost there. Trying guessing a bit higher.")   # 20    25
        
    elif my_guess < number_to_guess:
        print("Your guess is low. Trying guessing higher.") 




