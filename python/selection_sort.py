def selection_sort(mylist):
    for i in range(len(mylist)):
       small = i
       for j in range(i + 1, len(mylist)):
            if mylist[j] < mylist[small]:
                small = j
       temp = mylist[small]
       mylist[small] = mylist[i]
       mylist[i] = temp


lst = [43, 1, 67, 3,12]
selection_sort(lst)
print(lst)
