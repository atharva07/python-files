class Node:
    def __init__(self,item):
        self.left = None
        self.right = None 
        self.val = item
    
def inorder(root):
    if root:
        # traverse left
        inorder(root.left)
        # traverse root 
        print(str(root.val) + "->", end=" ")
        # traverse right
        inorder(root.right)

def preorder(root):
    if root:
        # traverse root
        print(str(root.val) + "->", end=" ")
        # traverse left
        preorder(root.left)
        # traverse right
        preorder(root.right)

def postorder(root):
    if root:
        # traverse left
        postorder(root.left)
        # traverse right
        postorder(root.right)
        # traverse root
        print(str(root.val) + "->", end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.right.right = Node(7)

print("Inorder Traversal")
inorder(root)

print("\npreorder traversal")
preorder(root)

print("\npostorder traversal")
postorder(root)