'''Temperature converter

Description

Write two functions that will convert temperatures back and forth from the Celsius and Fahrenheit temperature scales.
 The formulas for making the conversion are as follows:

  Tc=(5/9)*(Tf-32)
  Tf=(9/5)*Tc+32
where Tc is the Celsius temperature and Tf is the Fahrenheit temperature. More information and further descriptions of
how to do the conversion can be found at this NASA Webpage. If you finish this assignment quickly, add a function to
calculate the wind chill.

Input

Your program should ask the user to input a temperature and then which conversion they would like to perform.'''

def tTof(t) :
    tf = (t * 1.8) + 32
    print ("Temperature in farenheit :%d" % tf)
    return

def fTot(t) :
    tc = (t - 32) * 0.556
    print ("Temperature in celsius : %d" % tc)
    return

t = float(raw_input("Enter a temperature :"))
opt = raw_input("Convert to (f)Fahrenheit or (c)celsius : ")


if ( opt == "f" ) :
    tTof(t)
if ( opt == "c" ) :
    fTot(t)










