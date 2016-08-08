#operation on string

strng = "We use the built-in Python method"

print "length=",len(strng)
print "lower case=",strng.lower()
print "upper case=",strng.upper()
print "count 't' letter=",strng.count('e')
print "find in string=",strng.find('in')
print "replace string 'use'='try'",strng.replace("use","try")
print "split string ",strng.split()



def reverse(string):
    stn =' ' 
    for i in range(len(string)-1,-1,-1):
        stn =stn + string[i]
        print "reverse=",stn

reverse('hi')


def palindrome(string):
    rev_str = ''
    n = len(string)
    while n:
        n = n-1                  
        rev_str = rev_str + string[n] 
        if string == rev_str:
            print string,"is palindrome string"
        else:
            print string,"is not palindrome string"

palindrome('hii')
