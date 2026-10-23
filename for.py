# # # for digit in "123":
# # #     print(digit)

# # # for i in range(1,11):
# # #     print(i)

# # # for i in range(2,11,2):
# # #     print(i)
 
# # # for i in  range(1,11):
# # #     if i==5:
# # #         break
# # #     else:
# # #         print(i)
# # # else:
# # #     print("loop ends")

# # # for i in  range(1,11):
# # #     if i==5:
# # #         continue
# # #     else:
# # #         print(i)
# # # else:
# # #     print("loop ends")

# # # s=input("enter a string")
# # # rev=""
# # # for char in s:
# # #     rev=char + rev
# # # print("reversed string id ",rev)
# # # if rev==s:
# # #     print("palli")
# # # else:
# #     # print("not palli")

# # # n=int(input("enter a number"))
# # # k=1
# # # for i in range(1,11):
# # #     k=n*i
# # #     print(n,"*",i,"=",k)

# # # n=int(input("enter a number"))
# # # count=0
# # # while n>0:
# # #     n=n//10
# # #     count+=1
# # #     # i+=0
# # # print("count is",count)

# # # n=int(input("enter a number"))
# # # sum=0
# # # while n>0:
# # #      dig=n%10
# # #      sum+=dig
# # #      n=n//10
# # # print(sum)

# # # n=int(input("enter a number"))
# # # pro=1
# # # while n>0:
# # #      dig=n%10
# # #      pro*=dig
# # #      n=n//10
# # # print(pro)

# # # n=int(input("enter a number"))
# # # num = n
# # # count=0

# # # while n>0:
# # #     count+=1 
# # #     n=n//10
# # # print("count is",count) 
# # # n = num
# # # sum = 0
# # # while n>0:

# # #     dig=n%10
# # #     sum += dig**count
# # #     n=n//10
# # # print("sum:",sum)

# # # if sum==num:
# # #     print("amstrong")
# # # else:
# # #     print("not amstrong")

# # # n=int(input("enter a number"))
# # # f=1
# # # i=1
# # # while n>0:
# # #     f*=n
# # #     n-=1
# # # print(f)

# # # n=input("enter the string")
# # # reverse=""
# # # for char in n:
# # #     reverse=char+reverse
# # # print(reverse)
# # # if reverse==n:
# # #     print("palli")
# # # else:
# # #     print("not")

# # # n=int(input("enetr the num"))
# # # a=0
# # # b=1
# # # while n>0:
# # #     print(a)
# # #     c=a+b
# # #     a=b
# # #     b=c
# # #     n=n-1

# # # n=int(input("entr the num"))
# # # for i in range(2,n,1):
# # #     if n%i==0:
# # #         print(" not prime")
# # #         break
# # # else:
# # #     print("prime")


# # # a=int(input("enter the lim 1:"))
# # # b=int(input("enter the lim 2:"))
# # # for i in range(a+2,b,2):
# # #      print(i)


# # # NESTED FOR
# # # for i in range(1,5):
# # #     for j in range(1,5)  
# # #         print(i,j)

# # # for i in range(1,5):
# # #     for j in range(1,5):
# # #         print(j,end="")
# # #     print()

# # # for i in range(1,5):
# # #     for j in range(1,5):
# # #         print("*",end="")
# # #     print()

# # # n=5
# # # for i in range(5):
# # #      for j in range(n-i):
# # #          print("*",end="")
# # #      print()

# # # a="hello"
# # # b="world"
# # # print(a + b)

# # # a="hello"
# # # b="world"
# # # print(a *4)
 
# # # a="hello"
# # # b="world"
# # # print("w" in b)
# # # print(a not in a)

# # # p="python"
# # # print(p[0])

# # # p="ASHISH BALAKRISHNAN"
# # # print(p[0:15:2])


# # # p="ASHISH BALAKRISHNAN"
# # # # print(p[0:10])

# # # p="ASHISH BALAKRISHNAN"
# # # print(p[15:])

# # # p="ASHISH BALAKRISHNAN"
# # # print(p[-10:])


# # # p="ASHISH BALAKRISHNAN"
# # # print(p[:-10])


# # # Reverse
# # # d="mala"
# # # print(d[::-1])

# # # d="mala"
# # print(d[::-2])

# # s="programming in python"
# # print(s[:5])
# # print(s[-4:])
# # # print(s[1:20])
# # # print(s[::2])
# # # print(s[1::2])
# # # print(s[::-1])

# # for i in range(1,6):
# #     for j in range(5-i):
# #         print(" ",end=" ")
# #     for k in range(2*i-1):
# #         print("*",end=" ")
# #     print()

# # for i in range(5,0,-1):
# #     for j in range(5-i):
# #         print(" ",end=" ")
# #     for k in range(2*i-1):
# #         print("*",end=" ")
# #     print()

# # for i in range(0,5):
# #     for j in range(i):
# #         print(i,end=" ")
# #     print()

# # for i in range(5):
# #     for j in range(i+1):
# #         print(2*i,end=" ")
# #     print()

# # for i in range(1,6):
# #     for j in range(i):
# #         if i%2==0:
# #             print(2,end=" ")
# #         else:
# #             print(1,end=" ")
# #     print()

# # for i in range(6,0,-1):
# #     for j in range(1,i):
# #         print(j,end=" ")
# #     print()

# # for i in range(6,0,-1):
# #     for j in range(6-i):
# #         print(" ",end=" ")
# #     for j in range(1,i):
# #         print(j,end=" ")
# #     print()

# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()


# # for i in range(6,0,-1):
# #     for j in range(6-i):
# #         print(" ",end=" ")
# #     for j in range(i-1,0,-1):
# #         print(j,end=" ")
# #     print()

# # for i in range(6):
# #     for j in range(5,5-i,-1):
# #         print(j,end=" ")
# #     print()


# # for i in range(1,6):
# #     for j in range(5-i):
# #         print(" ",end=" ")
# #     for j in range(5,5-i,-1):
# #         print("*",end=" ")
# #     print()

# # for i in range(5,0,-1):
# #     for j in range(5-i):
# #         print(" ",end=" ")
# #     for j in range(5,5-i,-1):
# #         print("*",end=" ")
# #     print()

# # n=(input("enter the string"))
# # print(n[0],n[-1])

# # n=(input("enter the string"))
# # s=len(n)
# # print(n[s//2])

# # x=n[::-1]

# # if x==n:
# #     print("pall")
# # else:
# #     print("not")

# # print(n[1],n[-2])
# # c=0
# # for i in n:
# #     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
# #         c+=1
# # print(c)
# # v=""
# # for i in range(0,len(n),2):
# #     v+=n[i]
# # print(v[::-1])
# # c=0
# # for i in range(0,len(n)):
# #     if n[i]==" ":
# #         c+=1
# # print(c)
# # if n=="":
# #     print("empty")
# # else:
# #     print("not empty")





# # d=len[n]
# # print()
# # print(n[len(n)/2:len(n)])


# # s="hello"
# # print(s.upper())


# # s="hello"
# # print(s.lower())

# # s="Hello world"
# # print(s.capitalize())
# # print(s.title())
# # print(s.swapcase())
# # print(s.casefold())


#     # VALIDATION METHODS

# # s="1232"
# #1  print(s.isupper())
# #2 print(s.islower())
# #3 print(s.istitle())
# #4 print(s.isalpha())
# #5 print(s.isalnum())
# #6 # print(s.isspace())
# #7 print(s.isdigit())
# #8 print(s.isnumeric())
# #9 print(s.isdecimal())


# # search and find

# # s="pythyn"
# # print(s.find("y"))
# # print(s.index("y"))
# # print(s.rfind("y"))
# # print(s.rindex("y"))

# # Count
# # print(s.count("y"))

# # STARTSWITH()

# # s= "data science"
# # print(s.startswith("data"))
# # print(s.startswith("science"))
# # print(s.startswith("science",5))

# # ENDS WITH

# # print(s.endswith("science"))
# # print(s.endswith("data",0,4))

# # modification and replacing


# s="hello"
# new=s.replace("l","d")
# print(new)

# # strip()remove white space in tariling or leading

# # s="        hello     "
# # # print(s.strip())
# # print(s.lstrip())
# # print(s.rstrip())

# # s="data science"
# # print(s.split("a",1))

# # s="data,science,and,ai"
# # res=s.split(",",1)
# # print(res)
# # print(s.rsplit(",",1))

# # l=["hello","hi"]
# # print(" ".join(l))

# # fruits=["apple","orange","banana"]
# # print("-".join(fruits))
# # s="python"
# # print(s.ljust(20,"*")) 
# # print(s.rjust(20,"*"))
# # print(s.center(20,"*"))

# # zfill() zero padding

# # s="55"
# # # print(s.zfill(5))
# # print(s.zfill(10))

# # s="p"
# # print(dir(s))
# # s="hgh"
# # s="123"
# # print(s.isascii())

# # s="_python"
# # print(s.isidentifier())

# # s="ertfygud 1234567890"
# # print(s.isprintable())
# # # escape character-/n ,/t,/b

name= "ash"
age=10
height=1.9
print(f"my name is {name}i am {age} yrs old")