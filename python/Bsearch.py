barray = [34,72,12,78,56,14,18]
for i  in range(len(barray)-1,0,-1) :
    for j in range(i) :
         if barray[j] > barray[j+1] :
            temp=barray[j]
            barray[j]=barray[j+1]
            barray[j+1]=temp
sno=raw_input("Enter the number you want to search : ")
no=int(sno)
first = 0
last = len(barray)-1
found = False

while first<=last and not found:
    midpoint = (first + last)//2
    if barray[midpoint] == no:
        print "number is found"
        found = True
    else:
        if no < barray[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1

