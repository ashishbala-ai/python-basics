# efficency of an algorithm
# how well an alogorithm uses resourse 
# Time(how fast it runs)
# space(how much memory does it takes)

# time complexity 
# how the running times increses as input increses
# O(1) CONSTANT
# O(n) LINEAR
# O(logn) LOGARITHMIC TIME
# O(N2) QUADRATIC TIME  

# space complexoty
# how much memory the algorithm needs



# bubble sort()

# compare each pair of adjacent elements
# if the first element is grater than second ,swap them
# largest element in the lat position
# repeat the process for the remaining unsorted list
# stops early if no swaps in pass ,already sorted   


# def bubble(a):
#     n=len(a)
#     for i in range(n):
#         for j in range(n-1):
#             if a[j]>a[j+1]:
#                a[j],a[j+1]=a[j+1],a[j]
#     return a
# l=[5,3,6,8,9]
# # sorted=bubble(l)
# print(bubble(l))

# def selection(a):
#     n=len(a)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if a[j]<a[min_index]:
#                 min_index=j
#         a[i],a[min_index]=a[min_index],a[i]
#     return a
# l=[5,1,2,4,3]
# print(selection(l))

# arr=[10,20,30,40,50,60,70]
# key=70
# low=0
# high=len(arr)-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]==key:
#         print("in index ",mid)
#         break
#     elif key<arr[mid]:
#         high=mid-1
#     else:
#         low=mid+1
# else:
#     print("element not found")

# def linear(a,target):
#     for i in range(len(a)):
#         if a[i]==target:
#             return i
#     return -1
# l=[50,90,10,20,30]
# t=30
# print("target in",linear(l,t))



# DATA STUCTURE

# datavstrucure is  alogical way of organzing data in computer memory so that it can be udesd  effictivrly
# allows data to be addeed reoved stored and maintained in astructued manner
# helps in:
# fast acess
# easy insertionand deletion
# efficent memmory usage


# IT IS DIVIDED INTO
# PRIMITIVE
# NON PRIMITIVEE
# primitivr basic data type stores single value
# non primitive stores multiple value and present complex data

# link list is a linerar data structue in which elemt are not stoed in continous memory location
# item called as node and connected by link
# data and link connects to anothe link

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=node(10)
# n2=node(20)
# n3=node(30)


# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print("stack after push",stack)
# stack.pop()
# print("stack after pop",stack)

# stack=[]
# def push():
#     item=int(input("number"))
#     stack.append(item)
#     print("stack after push",stack)
# def pop():
#     if stack==0:
#         print("no element")
#     stack.pop()
#     print("stack after pop",stack)

# push()
# push()
# push()
# pop()

# l=[]
# l.append("a")
# l.append("b")
# l.append("c")
# print("queue",l)

# poped=l.pop(0)
# print("dequeue",poped)
# print("queue sfter dequeue",l)
# print("size",len(l))


# binary search insertion rule

# insertion

# start from the root
# compare the value to be inserted with the the current node
# if the value is smaller,move the left child
# if value is greater ,move to right child
# repeat until you reach None
# insert the new tree there

# deletion


# leaf node 
# simply remove the node

# one child
# replace the node with its child

# two child
# replace with 
# inoder sucessor(smallest value in right sub tree)
# inoder predecessor(largest on the left sutree)

class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class patient(person):
    pass

class doctor(person):
    def __init__(self,name,specialization):
        self.name=name
        self.specialization=specialization

class appointment(patient,doctor):
    def __init__(self,patient,doctor,date):
        super
        self.patient=patient
        self.doctor=doctor
        self.date=date
    def display(self):
        print("Patient:",self.patient.name)
        print("Patient age:",self.patient.age)
        print("doctor:",self.doctor.name)
        print("doctor specilization:",self.doctor.specialization)
        print("appointment date:",self.date)
p1=patient("arun",23)
d1=doctor("dr rahul","cardiology")
app1=appointment(p1,d1,"20-01-2026")
app1.display()