class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self,data):
        self.root=Node(data)

    def add_node(self,data):
        n=Node(data)
        flag=0
        current_root=self.root
        while(flag!=1):
            if (data<current_root.data):
                if (current_root.left==None):
                    current_root.left=n
                    print "left node added"
                    flag=1
                else:
                    current_root=current_root.left
            else:
                if  current_root.right==None  :
                    current_root.right=n
                    print "Right node added"
                    flag=1
                else:
                    current_root=current_root.right


    def bst_preorder_traversal(self, root):
        if root != None :
            print root.data
            #root = root.left
            self.bst_preorder_traversal(root.left)
            #root = root.right
            self.bst_preorder_traversal(root.right)
        else:
            return 1

    def bst_postorder_traversal(self,root):
        if root != None :
            self.bst_postorder_traversal(root.left)
            self.bst_postorder_traversal(root.right)
            print root.data
        else:
            return 1

    def bst_inorder_traversal(self,root):
        if root != None :
            self.bst_inorder_traversal(root.left)
            print root.data
            self.bst_inorder_traversal(root.right)

        else:
            return 1


b=BinaryTree(10)
b.add_node(15)
b.add_node(11)
b.add_node(18)
b.add_node(13)
b.add_node(7)
b.add_node(5)
b.add_node(8)
print "Preorder traversal"
b.bst_preorder_traversal(b.root)
print "Postorder traversal"
b.bst_postorder_traversal(b.root)
print "Inorder traversal"
b.bst_inorder_traversal(b.root)
