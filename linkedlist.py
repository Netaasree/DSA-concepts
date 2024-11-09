class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''
a=Node(10)
b=Node(20)
c=Node(30)
a.next=b
b.next=c
'''
'''
for i in range(5):
    nums[i]=Node(int(input(f"Enter your number{i}: ")))
first_num=nums[0]
print(first_num.data)
'''
nums=[]
n=int(input("Enter your range: "))
for i in range(n):
    nums.append(Node(input()))

for i in range(len(nums)-1):
        nums[i].next=nums[i+1]

        