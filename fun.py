# synatx 


# def function_name():
#     block of code
#     function_name

# def is to define a function

# def dis():
#     print("hello")
# dis()
# dis()

# def sum(a,b):
#     print(a+b)
# sum(3,3)

# def greet(name):
#     print("hello",name)
# greet("ash")

# def display(name,course):
#     print(name, "is studying in",course )
# n=(input("enetr the name"))
# s=(input("enetr the course"))
# display(n,s)

# def sad(name,course="da"):
#      print(name, "is studying in",course )
# sad("ash","ds")
# sad("ash")
# with return
# def sum(a,b):
#     return a+b
# result=sum(6,4)
# print(result)
# print(sum(6,4))

# without return


# def sum(a,b):
#     print(a+b)
# sum(3,3)

# print(sum)


# positinging

# def sub (a,b):
#     print(a-b)
# sub(9,3)
# sub(3,9)

# arbitary argument  allows us to pass any numbers of positional arguments

# def dis(*a):
#     print(a)
# dis(1,2,3,4,5) returns tupple

# def add(*num):
#     s=sum(num)
#     print(s)
# add(1,2,3,4,5)

# keyword arguments we can specify parameter names while calling the function

# def dis(a,b,c):
#     print(a,b,c)
# dis(a=10,b=30,c=20)

# # arbitarty keyword arguments
# def dis(**x):
#     print(x)
# dis(a=1,b=2,c=3)

# def cal(a,b):
#     sum=a+b
#     diff=a-b
#     return sum ,diff
# s,d=cal(20,10)
# print(s)
# print(d)

# def stu():
#     name=input("enter a number")
#     age=int(input("enter a number"))
#     return name ,age
# s,n=stu()
# print(s)
# print(n)

# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# n=int(input("enetra anum"))
# m=int(input("enetra anum"))
# print("max is",max(n,m))

# def vow(a):
#     v="aeiouAEIOU"
#     count=0
#     for i in a:
#         if i in v:
#             count+=1
#     return count
# n=input("enter num")
# print(vow(n))

# def evn(a):
#     if a%2==0:
#         return "even"
#     else:
#         return " odd"
# s=int(input("number"))
# print(evn(s))

# def rev(a):
#     return a[::-1]
# s=input("number")
# print(rev(s))

# x=10                  global variable
# def dis():
#     print(x)
# dis()
# print(x)

# def dis():
#     x=10              local
#     print(x)
# dis()
# print(x)


# when variable name is same 

# x=50
# def dis():
#     x=10
#     print(x)
# dis()
# print(x)


# x=50
# def dis():
#     global x
#     x=10
#     print(x)
# dis()
# print(x)

# pass by value when copy of a refernce i passed to the function
# changes made to variable inside the function do not affect the orginal variable
# outside the function 

# def mod(x):
#     x=x+5
#     print("inside",x)
# x=19
# mod(x)
# print(x)

# pass by refernce : when a refrence to the variable is paased to ye function changes made to the 
# variable  insid the function  affect the orginal variable outside the function


# def mod(lst):
#     lst.append(10)
#     print(lst)
# my_list=[1,2,3,4]
# mod(my_list)
# print(my_list)

# def dis(x):
#     if x==0:
#         return x
#     else:
#         return x +dis(x-1)
# n=int(input("enetr anum"))
# print("cumulative sum ",dis(n))

# def fact(n):
#     if n==0 or n==1:
#         return  1
#     else:
#         return n*fact(n-1)
# n=int(input("enetr anum"))
# print("factorial",fact(n))
    
# def dis(n):
#     if n==0 :
#         return 0
#     else:
#         print(n)
#         return n-dis(n-1)
# n=int(input("enetr anum"))
# dis(n)
# l=[1,2,3,4]
# def dis(l):
#     for i in l:
#         print(i**2)   
# dis(l)

# # sum=0
# def dis(l):
#     sum=0
#     for i in l:
#         sum+=i
#     return sum
# l=[1,2,3,4]
# print(dis(l))


# def prime(a):
#     count=0
#     for i in range(2,a):
#         if a%i==0:
#             count+=1
#     if count==0:
#         print("prime")
#     else:
#         print("not")
# n=int(input("number"))
# prime(n)

# def nam(n):
#     f=(n*9/5)+32
#     return f
# c=int(input("num"))
# print(nam(c))


# def lar(n):
#     largest=z[0]
#     for num in n:
#         if num>largest:
#             largest=num 
#     return largest
# z=[1,2,3,9,5,30]
# print(lar(z))

# def ni(n):
#    print( n.title())
# v=input("enter the string")
# (ni(v))


# def pra(v):
#     rev=0
#     rev=0
#     temp=v
#     while v>0:
#         rem=v%10
#         rev=rev*10+rem
#         v=v//10
#     return rev
# x=int(input("number"))
# m=pra(x)
# if m==x:
#     print("palli")
# else:
#     print("not palli")


# def num(a,n):
#     for num in a:
#         if num in n:
#             print(num)
# l=[12348,2783793,7736,78]
# k=[17,648,78]
# num(l,k)

# def mul(a):
#     for i in range(1,11):
#         print(n,'*',i,"=",n*i)
# n=int(input("enter the num"))
# mul(n)

# lambda function 
# lambda fn is amainly uesd when we need to short function just once
# cant give any number of arguments,but a single expression

# x=lambda a:a**2
# n=int(input("enter the number"))
# print(x(n))

# x=lambda a,b:a+b
# n=int(input("enter the number"))
# m=int(input("enter the number"))
# print(x(n,m))

# x=lambda a,b:a if a>b else b
# n=int(input("enter the number"))
# m=int(input("enter the number"))
# print(x(n,m))

# x=lambda a:"even" if a%2==0 else "odd"
# n=int(input("enter the number"))
# print(x(n))

# l=[1,2,3,4,5,6,7,8,9]
# x=filter(lambda a:a%2==0,l)
# # print(list(x))

# map ()is used to aply a function to every item in am sentence(list ,tuple)

# l=[1,2,3,4,5,6,7,8,9]
# x=map(lambda a:a**2,l)
# print(list(x))

# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# x=reduce(lambda a,b:a+b,l)
# print(x)

# # def sum(a):
# #     if a<0:
# #         return 0
# #     else:
# #         return a+sum(a-1)
# # n=int(input("enter the limit"))
# # print(sum(n))

# def rec(n):
#     if n<=1:
#         return n
#     else:
#         return rec(n-1) +rec(n-2)
# def print1(n):
#     for i in range(n):
#         print(rec(i)," ")
# n=int(input("enter the number"))
# print("fibonacci upto ",n,"terms")
# print1(n)

# def pow(x,n):
#     if n==0:
#         return 1
#     else:
#         return x*pow(x,n-1)
# n=int(input("enter the nmber"))    
# x=int(input("enter exp"))
# print(pow(n,x))

# def rev(s):
#     if len(s)==0:
#         return s
#     else:
#         return s[-1]+rev(s[:-1])
# n=(input("enter the nmber"))  
# print(rev(n))


# x=lambda a: a[-1]
# n=input("string")
# print(x(n))

# l=[1,2,3,4,5]
# x=map(lambda a:a*3,l)
# print(list(x))

# x=lambda b:"starts with A" if b[0]=="a" or "A" else"not with A"  
# s=input("string")
# print(x(s))

# x=lambda a,b:a**b
# n=int(input("enter the nmber"))
# d=int(input("enter the nmber"))
# print(x(n,d))


# x=lambda a,b:"first is longer" if len(a)>len(b)else " second is longer"
# n=(input("enter the nmber"))
# d=(input("enter the nmber"))
# print(x(n,d))

# c=["ash","ashi"]
# x=filter(lambda a:len(a)>=4,c)
# print(list(x))

# c=[1,2,3,4,10,11,23,234,43]
# x=filter(lambda a:a>=10,c)
# print(list(x))

# c=["ash","ashi","pass","pall"]
# x=filter(lambda a:a[0]=="p",c)
# print(list(x))

# l=["ash","ashi"]
# x=map(lambda a:a.upper(),l)
# print(list(x))

# l=[36,37]
# x=map(lambda a:a*9/5+32,l)
# print(list(x))

# l=["ash","ashi"]
# x=map(lambda a:a + "_done",l)
# print(list(x))

# l=[1,2,3,4,5]
# l1=[5,4,3,2,1]
# x=map(lambda a,b:a+b,l,l1)
# print(list(x))

# from functools import reduce
# # l=[1,2,3,4,5,6,7,8,9,10]
# # x=reduce(lambda a,b:a+b,l)
# # print(x)

# l=["ash","ashi"]
# x=reduce(lambda a,b:a+b,l)
# print(x)

# def co(a):
#     if a<10:
#         return 1
#     else:
#         a=a//10
#         return 1 +co(a)
# n=int(input("num"))
# print(co(n))

def sum(s):
    if len(s)==0:
        return 0
    else:
        return s[0]+sum(s[1:])
n=[5,10,15,20,30]
print(sum(n))

