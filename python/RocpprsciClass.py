import random
class Rcps:

    def __init__(self,mpoint):
        self.maxpoint=mpoint
        self.choicelist = {"r": 0, "s": 1, "p": 2}
        self.chlist = ["Rock", "Scissor", "Paper"]
        self.compoint = 0
        self.humpoint = 0

    def storeResult(self, flag):
        if (flag == 1):
            self.compoint += 1
        if (flag == 0):
            self.humpoint += 1

    def checkWin(self):
        if (self.maxpoint == self.compoint):
            print "Final score :    Computer : ", self.compoint, "Human : ", self.humpoint, "Computer win......."
            exit()
        if (self.maxpoint == self.humpoint):
            print "Final score :    Human : ", self.compoint, "Computer : ", self.humpoint, "Human win........."
            exit()
    
    def resultDisplay(self,humanchoice,comchoice):
        try:
            if comchoice == self.choicelist[humanchoice]:
                print "Human: ", self.chlist[self.choicelist[humanchoice]], "Computer : ", self.chlist[comchoice], "Result : draw"
            elif comchoice == 0 and self.choicelist[humanchoice] == 1:
                print "Human: ", self.chlist[self.choicelist[humanchoice]], "Computer : ", self.chlist[comchoice], "Result : Computer win"
                self.storeResult(1)
            elif comchoice == 1 and self.choicelist[humanchoice] == 0:
                print "Human: ", self.chlist[self.choicelist[humanchoice]], "Computer : ", self.chlist[comchoice], "Result : Human win"
                self.storeResult(0)

            elif comchoice == 0 and self.choicelist[humanchoice] == 2:
                print "Human: ", self.chlist[self.choicelist[humanchoice]], "Computer : ", self.chlist[comchoice], "Result : Human win"
                self.storeResult(0)

            elif comchoice == 2 and self.choicelist[humanchoice] == 0:
                print "Human: ", self.chlist[self.choicelist[humanchoice]], "Computer : ", self.chlist[comchoice], "Result : Computer win"
                self.storeResult(1)

            elif comchoice == 1 and self.choicelist[humanchoice] == 2:
                print "Human: ", self.chlist[self.choicelist[humanchoice]], "Computer : ", self.chlist[comchoice], "Result : Computer win"
                self.storeResult(1)

            elif comchoice == 2 and self.choicelist[humanchoice] == 1:
                print "Human: ", self.chlist[self.choicelist[humanchoice]], "Computer : ", self.chlist[comchoice], "Result : Human win"
                self.storeResult(0)
        except KeyError:
            print "Please enter correct choice ...."




if __name__=='__main__':
    try:
        maxcount = int(raw_input("How many points required for win? "))
        obj = Rcps(maxcount)
        while (1):
            comchoice = random.randint(0, 2)
            humchoice = raw_input("Choose (r)ock, (s)cissor, (p)aper ? ")
            obj.resultDisplay(humchoice,comchoice)
            obj.checkWin()
    except KeyboardInterrupt:
        print "byyyyyyyyyyyyyyy"





        