*** Settings ***
Library  Collections

*** Variables ***
${str}  hiii
*** Keywords ***
clist
	[Arguments]  ${listname}  @{arg}
	${listname}=  Create List    @{arg}
	[return]  ${listname}

rclist
	[Arguments]  @{arg}
	${rlist}=    Create List  @{arg}
	[return]  ${rlist}
	
*** Test Case ***
Test for create list  [Documentation]  Create list test
	[Tags]  clist
	${newlist}=  Create List  a  b  c
	Log  ${newlist[2]}

Test for append List  [Documentation]  Append list test
	[Tags]  appendlist
	${nlist}=  clist  newlist  a  b  c  d
	Append to List  ${nlist}  e  f
	Log  ${nlist}

Test for combine list  [Documentation]  Combine list test
	[Tags]  combinelist
	${nlist1}=  rclist  q  w  e  r
	${nlist2}=  rclist  t  y  u  i  o
	${nlist}=  Combine Lists  ${nlist1}  ${nlist2}
	Log  ${nlist}  

Test for convert items to list  [Documentation]  Convert list test
	[Tags]  convertlist
	${str1}=  Convert To List  ${str}
	Log  ${str1}

Test for list should equal  [Documentation]  List should equal test
	[Tags]  lequal
	${llist1}=  rclist  a  b  c  d 
	${llist2}=  rclist  a  b  c  d  
	${result}=  Lists Should Be Equal  ${llist1}  ${llist2}
	Log  ${result}

Test for dictionary equal  [Documentation]  Dictionary equal test
	[Tags]  dequal
	${dict1}=  Create Dictionary  name=Yograj  address=Chalisgaon
	${dict2}=  Create Dictionary  name=Yograj  address=Chalisgaon
	Dictionaries Should Be Equal  ${dict1}  ${dict2}
	Log  Dictionaries are equal

Test for Removing values from list  [Documentation]  Remove value test
	[Tags]  rvalue
	${nlist}=  rclist  a  b  c  d  a  d  s  e  b
	Remove values from list  ${nlist}  a  b
	Log  ${nlist}

Test for Reverse List  [Documentation]  Reverse list test case
	[Tags]  rlist
	${nlist}=  rclist  34  12  67  45  11  55  22
	Reverse List  ${nlist}
	Log  ${nlist}
	Sort List  ${nlist}
	Log  ${nlist}

Test for length and count of list and dictionary  [Documentation]  Count and length of list and dict test
	[Tags]  cl
	${nlist}=  rclist  a  b  c  d  fd  e  wq  a  ab   b   a
	${lcount}=  Get count  ${nlist}  a
	Log  ${lcount}
	${llength}=  Get Length  ${nlist}
	Log  ${llength}
	${dict1}=  Create Dictionary  name=Yograj  address=Chalisgaon
	${dlength}=  get length  ${dict1} 
	Log  ${dlength}
	
	
	
