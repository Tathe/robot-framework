def addchar(wordToGuess,tempGuessedWord,ch):
    for i in range(0, len(wordToGuess)):
        if ch == wordToGuess[i]:
            tempGuessedWord[i] = ch[0]
    return(tempGuessedWord)



def result(wordToGuess,tempGuessedWord):
    if (wordToGuess == tempGuessedWord):
        print "Congratulation You Guess it..."
    else:
        print "Sorry... You Loss..."



wordToGuess = list("yograj")
tempGuessedWord=list("------")
guessed=""
wrongGuessed=""
wguess=7
while(wguess>0) and (wordToGuess!=tempGuessedWord) :
    print "".join(tempGuessedWord)
    ch = raw_input("Enter Guess : ")
    if ch in guessed or ch in wrongGuessed :
        print "Already Exist "
    else:
        if ch in wordToGuess:
            print "correct"
            guessed= guessed+ch
            tempGuessedWord=addchar(wordToGuess,tempGuessedWord,ch)
        else :
            wguess-=1
            wrongGuessed=wrongGuessed+ch
            print "You guessed wrong"
            print "%d Guesses Remaining..." % wguess
    print "You Entered : ", wrongGuessed
else :
    result(wordToGuess,tempGuessedWord)









