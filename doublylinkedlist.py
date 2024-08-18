class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

node1=Node(101)
node2=Node(102)
node3=Node(103)
node4=Node(104)

node1.next=node2
node2.prev=node1

node2.next=node3
node3.prev=node2

node3.next=node4
node4.prev=node3

print("Traversing forward: \n")
currnode=node1
while currnode:
    print(currnode.data,end="->")
    currnode=currnode.next
print("Null")
print("Traversing backward: \n")
currnode=node4
while currnode:
    print(currnode.data,end="->")
    currnode=currnode.prev
print("Null")

