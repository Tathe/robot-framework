from array import *
sarray=array('i',[5,3,6,8,2,87,34,654,213])
flag = 0
no=raw_input("Enter Element to search : ")
for index,i in enumerate(sarray) :
    if (int(no) == i) :
            print "number is found at %d position : "%(index)
            exit(1)

print "number is not found"

