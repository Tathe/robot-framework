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

    def add_node(self,data):
        temp=Node(data)
        self.head.next=temp
        self.head=temp
        print "node added"

    def list_traversal(self):
        tmp=self.start
        while(tmp.next!=None):
            print tmp.data
            tmp=tmp.next
        else:
            print tmp.data

c=createlist(12)
c.add_node(10)
c.add_node(8)
c.add_node(7)
c.list_traversal()

