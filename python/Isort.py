iarray = [23,34,15,11,43,37,87,55]

for i in range(1,len(iarray)):

    no = iarray[i]
    index = i
    while index>0 and iarray[index-1]>no:
        iarray[index]=iarray[index-1]
        index = index-1
    iarray[index]=no

for n1 in iarray :
    print n1

