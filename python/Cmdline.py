import sys

def cmdparse(arg) :
	
	if(len(arg)==1) and (arg[0]=='~h') :
		
			print "~i : Input File"
			print "~o : Output file"
			print "~h : Help"

	elif(len(arg)==4) :		 
		if(arg[0]=='~i') :
			ifile=arg[1]
		if(arg[2]=='~o') :
			ofile=arg[3]
		print("Input file : %s" % ifile)
		print("Output file : %s" % ofile)
		a=open(ifile,"r+")
		b=open(ofile,"r+")
		str1=a.read();
		b.write(str1);
		a.close()
		b.close()

	else :
		print "Incorrect Choice"
	return

cmdparse(sys.argv[1:])

