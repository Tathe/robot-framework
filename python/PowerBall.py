'''To win the Powerball lottery (an extremely unlikely event so don't waste your time) you have to pick six numbers
correctly. The first five numbers are drawn from a drum containing 53 balls and the sixth is drawn from a drum containing
 42 balls. The chances of doing this are 1 in 120,526,770. Write a program to generate a set of Powerball numbers by
 utilizing the choice function in Python's random module.'''

temp=int(raw_input("Enter a number : "))
data=[]
i=1
set=int(raw_input("How many set of numbers : "))
for j in range(0,set) :
    while i<=5 :
        no = (temp * 432 * 123 -74) % 53
        if no not in data :
            data.append(no)
            i=i+1
        temp+=13
    no2=(temp * 17 * 23 -74) % 42
    print "Your numbers : ",data, "Powerball : ", no2
    data=[]
    i=1

