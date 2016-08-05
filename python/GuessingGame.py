'''Guessing game

Description

The computer will pick a number between 1 and 100. (You can choose any high number you want.) The purpose of the game
is to guess the number the computer picked in as few guesses as possible.

Input

The user will enter his or her guess until the correct number is guessed.

Output

The program will keep asking the user to guess until he or she gets the number correct. Then the program will
 print how many guesses were required.'''

a=int(raw_input("Enter the number : "))

a= (a * 522 * 123 + 23) % 100
count=1
no=int(raw_input("Enter number between 1 and 100"))
while no != a :
    if(no>a) :
        print "Too high. Try again : "
    else :
        print "Too low, Try again : "
    count+=1
    no=input()

print "Congratulations! You got it in %d guesses." % count