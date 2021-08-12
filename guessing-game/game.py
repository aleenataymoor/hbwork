q

""" Number Guessing Game """

import random

print("Howdy!  What's your name?")
name = input("Type in your name: ")
print(f"{name}, I'm thinking of a number between 1 and 100.  Try to guess my number:")
numrangestart = int(input("Type your start range: "))
numrangeend = int(input("Type your end range: "))
computer_number = random.randint(numrangestart, numrangeend)
#ourNumber = 0
#guess_number = 0 

def playGame(): 
    ourNumber = 0
    guess_number = 0  
    while ourNumber != computer_number:
        ourNumber= int(input('Your guess?'))
        guess_number = guess_number + 1
            #if guess_number > 9:
                #print("Your tries are over.")
                #playAgain= input ("Would you like to play again?")
                #while playAgain != "no": 
        if ourNumber > computer_number:
            print("Your guess is too high- try again please!") 
        elif ourNumber < computer_number:
            print("Your guess is too low- try again please!")
        elif ourNumber == computer_number:
            print(f"{name}, well done!. You found my number in {guess_number} tries!")
    scores = []
    scores.append(guess_number)
    
    min_score = min(scores)
    print(min_score)
playGame()

playAgain= input ("Would you like to play again?")
while playAgain != "no":    
    playGame()
    playAgain= input ("Would you like to play again?")


