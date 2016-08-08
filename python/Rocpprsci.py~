'''Rock, paper, scissors, also know as roshambo, is a simple child's game that is frequently used to settle disputes.
In the game, a rock breaks the scissors, the scissors cut the paper, and the paper covers the rock. Each option is
equally likely to prevail over another. If the players choose the same object a draw is declared and the game is
repeated until someone prevails. For more information than you ever thought it was possible to collect about rock,
paper, scissors, check out the Web page of the World RPS Society.

In this computerized version the human player competes against the computer which chooses a rock, paper, or
scissors randomly. The game proceeds until the human player quits the game or until a predetermined score is reached
(e.g., 11 pts.) at which time the final tally is displayed. Solutions with fewer numbers of if statements are considered
more elegant.

Input

The human player enters the number of points required for a win. During the play of the game the human player selects
whether to pled in a nay a rock, paper, or scissors by using the keyboard. The human player may also end the game by pressing
the Control-D sequence at any time. (Ending the game early does not allow a winner to be determined if the human player
is ahead.)'''

#temp=int(raw_input("Enter a number : "))
#maxpoint=int(raw_input("How many points required for win? "))'''
import random

choicelist={"r":0,"s":1,"p":2}
chlist=["Rock","Scissor","Paper"]
count=int(raw_input("How many points required for win? "))


scnt=0
hcnt=0
#syschoice=(temp * 23) % 3

while(1) :
    syschoice = random.randint(0, 2)
    choice = raw_input("Choose (r)ock, (s)cissor, (p)aper ? ")
    if syschoice==choicelist[choice] :
        print "Human: ", chlist[choicelist[choice]], "Computer : ", chlist[syschoice], "Result : draw"
    elif syschoice==0 and choicelist[choice]==1 :
        print "Human: ", chlist[choicelist[choice]], "Computer : ", chlist[syschoice], "Result : Computer win"
        scnt+=1
    elif syschoice==1 and choicelist[choice]==0 :
        print "Human: ", chlist[choicelist[choice]], "Computer : ", chlist[syschoice], "Result : Human win"
        hcnt+=1
    elif syschoice==0 and choicelist[choice]==2 :
        print "Human: ", chlist[choicelist[choice]], "Computer : ", chlist[syschoice], "Result : Human win"
        hcnt += 1
    elif syschoice==2 and choicelist[choice]==0 :
        print "Human: ", chlist[choicelist[choice]], "Computer : ", chlist[syschoice], "Result : Computer win"
        scnt += 1
    elif syschoice==1 and choicelist[choice]==2 :
        print "Human: ", chlist[choicelist[choice]], "Computer : ", chlist[syschoice], "Result : Computer win"
        scnt += 1
    elif syschoice==2 and choicelist[choice]==1 :
        print "Human: ", chlist[choicelist[choice]], "Computer : ", chlist[syschoice], "Result : Human win"
        hcnt += 1
    if(count==scnt) :
        print "Final score :    Computer : ", scnt ,"Human : ", hcnt, "Computer win......."
        exit()
    if(count==hcnt) :
        print "Final score :    Human : ", hcnt, "Computer : ", scnt, "Human win........."
        exit()

