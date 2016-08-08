class Node:
    def __init__(self,data):
        print "Node Created"
        self.data = data
        self.next = None
        self.prev = None


class createlist:
    def __init__(self,data):
        n=Node(data)
        self.start=n
        self.head=n
        self.head.next=n
        self.head.prev=n

    def add_node(self,data):
        temp=Node(data)
        temp.next=self.start
        self.start.prev=temp
        temp.prev=self.head
        self.head.next=temp
        self.head=temp
        print "node added"

    def next_node(self):
        print self.head.data
        self.head=self.head.next

    def prev_node(self):
        print self.head.data
        self.head = self.head.prev

    def list_traversal(self):

        self.head=self.start
        while(self.head.next!=self.start):
            self.next_node()

        else:
            print self.head.data
            self.head = self.head.next

    def reverse_list_traversal(self):
        self.head = self.start.prev
        while (self.head != self.start):
            self.prev_node()
        else:
            self.prev_node()

c=None
while(True):
    print "=======Menu=========="
    print "1. Create New List"
    print "2. Add Node"
    print "3. Traverse List"
    print "4. Reverse Traverse List"
    print "5. Next Node"
    print "6. Previous Node"
    print "7. Exit"
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
        c.reverse_list_traversal()

    elif (ch==5):
        c.next_node()

    elif (ch==6):
        c.prev_node()

    elif (ch==7):
        exit()

    else:
        print "Please Enter correct choice : "


