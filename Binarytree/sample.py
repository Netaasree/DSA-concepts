class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data,end=",")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
        
r=TreeNode("R")
a=TreeNode("A")
b=TreeNode("B")
c=TreeNode("C")
d=TreeNode("D")
e=TreeNode("E")
f=TreeNode("F")

r.left=a
r.right=b

a.left=c
a.right=d

b.left=e
b.right=f

print("r.left.right.data: ",r.left.right.data)
preOrderTraversal(r)