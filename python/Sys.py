import sys,getopt
def Parsing():
  myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
  for o,a in myopts:
    if o == '-i':
          arg1=a
    elif o == '-o':
          arg2=a
  arg1_to_int = int(arg1)   
  arg2_to_int = int(arg2)   
  print "Addition of ",arg1,"and",arg2,"is",arg1_to_int + arg2_to_int

if __name__ == "__main__":
   Parsing()

