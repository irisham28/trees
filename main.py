class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None

#creating the tree
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)

root.left.left = Tree(4)
root.left.right = Tree(5)

root.right.left = Tree(6)
root.right.right = Tree(7)

#Inorder traversal--> left subtree, root, right subtree
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end="-")
        inorder_traversal(node.right)

inorder_traversal(root)

#Preorder traversal --> root, left subtree, right subtree
def preorder_traversal(node):
    if node:
        print(node.data, end="-")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

print()
preorder_traversal(root)
    
#postorder traversal --> left subtree, right subtree, root
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end="-")
print()
postorder_traversal(root)


    




