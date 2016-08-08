def bubblesort(mylist):
      for i in range (0, len(mylist)-1):
          for j in range(0,len(mylist)-1-i):
               if mylist[j]>mylist[j+1]:
                     temp = mylist[j]
                     mylist[j] = mylist[j+1]
                     mylist[j+1] = temp
                      #mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
      return mylist

lst = [5,2,8,1,4]
bubblesort(lst)
print(lst)

