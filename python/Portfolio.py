'''Portfolio Tracker

Description

In the financial world a portfolio is a collection of investments. Many investors have a portfolio of stocks or mutual
funds. For this assignment, you will write a program for keeping track of the value of a group of stocks.

Data structure

You should store your data in a list of lists. A sample portfolio might look like this:

[['MMM', '3M', '100', '74.00', '118.30'],
 ['MDT', 'Medtronic', '50', '56.10', '48.00'],
 ['NWAC', 'Northwest Airlines', '100', '67.50', '18.04'],
 ['SGI', 'Silicon Graphics', '100', '22.25', '2.25']]
Note: Storing the prices in cents may make rounding easier in the long run. A lot of financial software uses this
strategy.

This is the most complex program we have written so far. You will team up in groups of four and divide some of the
 tasks between pairs of programmers. For example, one pair could work on the user interface while another writes the
  code to update share prices. You will meet daily with your entire team of four to update one another on your progress
  and troubleshoot problems.

Input

This program will be menu-driven. When you are done you will be able to open a file containing your portfolio data,
save the file back to disk, display a portfolio summary (sorted in several different ways), add a new stock to your
portfolio, delete a stock from your portfolio, and update the prices of the stocks in your portfolio. In order to
accomplish this, you will need to take advantage of a number of the Python features we have studied lately.

See also: Using dictionaries for program menus

You can build whatever kind of user interface you would like. Make sure you pay attention to designing something that
is clear and easy to use.

Output

When you sort the portfolio for display, you should create a dictionary with the sort category as the key and the
list as the value. Then you can iterate through the keys and display the table of stocks. Such a dictionary might
look like:

{'3M': ['MMM', '3M', '100', '74.00', '118.30'],
 'Medtronic': ['MDT', 'Medtronic', '50', '56.10', '48.00'],
 'Northwest Airlines': ['NWAC', 'Northwest Airlines', '100', '67.50', '18.04'],
 'Silicon Graphics': ['SGI', 'Silicon Graphics', '100', '22.25', '2.25']}
Instead of using tab characters to align the fields for displaying, try using the string formatting codes we've used
previously in class.

See also: String formatting codes

Sample run

(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? l
Load file: portfolio.dat

(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? r
Sort output on (N)ame, or (V)alue? n

Company                   Shares   Pur.  Latest   Value     G/L
=================================================================
3M (MMM)                    100   74.00  118.30   11830    59.9%
Medtronic (MDT)              50   56.10   48.00    2400   -14.4%
Northwest Airlines (NWAC)   100   67.50   18.04    1804   -73.3%
Silicon Graphics (SGI)      100   22.25    2.25     225   -89.9%
                                                  ---------------
                                                  16259   -15.2%
                                                  ===============

    '''

str=[['MMM', '3M', '100', '74.00', '118.30'],
    ['MDT', 'Medtronic', '50', '56.10', '48.00'],
    ['NWAC', 'NorthwestAirlines', '100', '67.50', '18.04'],
    ['SGI', 'SiliconGraphics', '100', '22.25', '2.25']]
keys=[0 for i in range(0,len(str))]
dic={}
for i in range(0,len(str)) :
    dic[str[i][1]]=str[i]
    keys[i]=str[i][1]
print dic
print keys
print "Company                    Shares       pur.           Latest          Value         G/L    "
print "============================================================================================"
for i in range(0,len(dic)) :
    for j in range(0,5) :
        print dict[keys[i]][j]

print dic

