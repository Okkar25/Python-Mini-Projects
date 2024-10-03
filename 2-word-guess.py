# import random 

# words = ["computer", "science", "recursion", "software", "development", "business", "analyst", "algorithms", "javascript", "decorators", "generators", "codeium", "chatgpt", "openai"]

# word = random.choice(words)

# print("Guess the characters of the word.")
# print(f"The answer is {word}")

# guesses = ""
# turns = 12

# while turns > 0:
#     failed = 0
    
#     for char in word:
#         if char in guesses:
#             print(char, end="\n")
#         else:
#             print("_")
#             failed += 1
    
#     if failed == 0:
#         print("You win.")
#         print(f"The word is {word}")
#         break
        
#     print()
#     guess = input("Guess a character from the word : ")

#     guesses += guess

#     if guess not in word:
#         turns -= 1
#         print('Wrong character.')
#         print(f"You have {turns} more turns to guess.")

#         if turns == 0:
#             print("You loose")
            

# -----------------------------------------------------------------------------------------


import random 

words = ["computer", "science", "recursion", "software", "development", "business", "analyst", "algorithms", "javascript", "decorators", "generators", "codeium", "chatgpt", "openai"]

word = random.choice(words)
hint_characters = random.sample(range(len(word)), 3)
# print(hint_characters)

print("Guess the characters of the word.")
# print(f"The answer is {word}")

guesses = ""
turns = 12

for i in range(len(word)):
    if i in hint_characters:
        guesses += word[i]
# print(guesses)

while turns > 0:
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char, end="\n")
        else:
            print("_")
            failed += 1
    
    if failed == 0:
        print("You win.")
        print(f"The word is {word}")
        break
        
    print()
    guess = input("Guess a character from the word : ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong character.')
        print(f"You have {turns} more turns to guess.")
        print(f"The correct word is {word}")

        if turns == 0:
            print("You loose")


