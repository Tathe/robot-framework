*** Settings ***
Library  LoginApp.py


*** Keywords ***
login method
	[Arguments]   ${uname}   ${passw}
	${message}=   login  ${uname}  ${passw}
	[return]  ${message}

*** Test Case ***
TEST FOR VALID USERNAME AND VALID PASSWORD
	[Tags]  lo
	${result}=   login method   yograjshisode@gmail.com   12345
	Should be equal  ${result}  ${TRUE}

TEST FOR INVALID USERNAME AND INVALID PASSWORD
	${result}=  login method  MANOJVAJPEYI@gmail.com  664643
	Should be equal  ${result}  ${False}

TEST FOR VALID USERNAME AND INVALID PASSWORD
	${result}=  login method  yograjshisode@gmail.com  87865
	Should be equal  ${result}  ${False}

TEST FOR INVALID USERNAME AND VALID PASSWORD
	${result}=  login method  MANOJVAJPEYI@gmail.com  12345
	Should be equal  ${result}  ${False}


TEST FOR EMPTY USERNAME AND VALID PASSWORD
	${result}=  login method   ''  12345
	Should be equal  ${result}  ${False}

TEST FOR VALID USERNAME AND EMPTY PASSWORD
	${result}=  login method  MANOJVAJPEYI@gmail.com  ''
	Should be equal  ${result}  ${False}

TEST FOR EMPTY USERNAME AND EMPTY PASSWORD
	${result}=  login method  ''  ''
	Should be equal  ${result}  ${False}

	
