import re

def login(uname="",passw=""):
     if valid(uname):
        if (uname=="yograjshisode@gmail.com") and (passw=="12345"):
            return True
	else:
	    return False
     else:
         return False

def valid(uname):
 	if (re.match(r'[a-zA-Z](.*)@(.*)\.[a-zA-Z]{2,3}', uname)):
		return True
	else:
		return False


