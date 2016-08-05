class Node:
    def __init__(self,data):
        print "Node Created"
        self.data = data
        self.next = None




class createlist:
    def __init__(self,data):
        n=Node(data)
        self.start=n
        self.head=n
        self.head.next=n

    def add_node(self,data):
        temp=Node(data)
        temp.next=self.start
        self.head.next=temp
        self.head=temp
        print "node added"

    def next_node(self):
        print self.head.data
        self.head=self.head.next

    def list_traversal(self):

        self.head=self.start
        while(self.head.next!=self.start):
            self.next_node()

        else:
            print self.head.data
            self.head = self.head.next






c=None
while(True):
    print "=======Menu=========="
    print "1. Create New List"
    print "2. Add Node"
    print "3. Traverse List"
    print "4. Next Node"
    print "5. Exit"
    ch = int(raw_input("Enter your choice: "))
    if(ch==1):
        data = raw_input("Enter a value : ")
        c=createlist(data)

    elif (ch==2):
        data=raw_input("Enter a value : ")
        c.add_node(data)

    elif (ch==3):
        c.list_traversal()

    elif (ch==4):
        c.next_node()

    elif (ch==5):
        exit()

    else:
        print "Enter correct choice : "





