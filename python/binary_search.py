def binarySearch(arr,key): 
    low =0
    high =len(arr)-1
    print"key ",key
    while high >= low:
        mid =(low + high)/2
        midval =arr[mid]
        print"low ",low, " mid=",mid, " high=",high, " midval=",midval
        if midval < key :
            low = mid + 1
        elif midval > key:
            high = mid - 1
        else:
            print "found"
            return mid
           # print"found"
    print "Not found"


array =[11,22,33,44,55]
binarySearch(array,22)
