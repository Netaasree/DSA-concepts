class Node:
       def __init__(self,data):
           self.data=data
           self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def print(self):
        temp=self.head
        while temp.next:
            print(temp.data,"->",end="")
            temp=temp.next
        print(temp.data)
    def insert_index(self,index:int,data):
        new_node=Node(data)
        if index==0:
            return self.insert_begin(data)
        temp=self.head
        for _ in range(index-1):
                temp=temp.next
        new_node.next=temp.next
        temp.next=new_node




a=Linked_list()
a.insert_begin(10)
a.insert_begin(20)
a.insert_begin(30)
a.insert_begin(40)
a.print()
a.insert_index(1,45)
a.print()