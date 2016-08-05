class Hangman :
    def __init__(self):
        self.wordToGuess = list("yograj")
        self.tempGuessedWord = list("------")
        self.wrongGuessed = ""
        self.maxChance=7

    def wrongGuess(self,ch):
        self.maxChance -= 1
        self.wrongGuessed = self.wrongGuessed + ch
        print "You guessed wrong"
        print "%d Guesses Remaining..." % self.maxChance

    def startGame(self):
        while(1):
            print "".join(self.tempGuessedWord)
            ch = raw_input("Enter Guess : ")
            if ch in self.tempGuessedWord or ch in self.wrongGuessed:
                print "Already Exist "
            else:
                if ch in self.wordToGuess:
                    print "correct"
                    self.addchar(ch)
                else :
                    self.wrongGuess(ch)
            self.checkResult()
            print "You Entered : ", self.wrongGuessed

    def addchar(self,ch):
        for i in range(0, len(self.wordToGuess)):
            if ch == self.wordToGuess[i]:
                self.tempGuessedWord[i] = ch[0]

    def checkResult(self):
        if (self.wordToGuess == self.tempGuessedWord):
            print "Congratulation You Guess it..."
            exit()
        if(self.maxChance>0):
            return
        else:
            print "Sorry... You Loss..."
            exit()

if __name__=='__main__':
    print "==========Welcome to Hangman =========="
    print "You get maximum 7 chances"
    obj=Hangman()
    obj.startGame()

