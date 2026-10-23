# # conditional statements
# age =20
# if age>=18:
#     print ("eligible")
# age =17
# if age>=18:
#     print("ekigible ")
# else:
#     print("not eligible")
mark=40
# if mark>=50:
#     print("pass")
# else:
#     print("fail")
# num=7
# if num%2==0:
#    print("even")
# else:
#     print("odd")
# num=int(input("enetr a number"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")
# num=int(input("enter a number"))
# if num>0:
#     print ("positive")
# else:
#     print("negative")
# 


# nested if

# num=int(input("enter a number"))
# if num>=50:
#     if num>=90:
#         print ("A")
#     elif num>=80:
#         print ("B")
#     elif num>=70:
#         print ("c")
#     elif num>=50:
#         print ("d")
# else:
#      print("fail")

# num=int(input("enter a number"))
# if num>0:
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("negative")


# # exp=int(input("enter the service"))
# # sal=int(input("enter the salary"))

# # if exp>=5:
# #     b=sal*0.05
# #     print("bonus",b)
# #     print("salary",sal+b)

# # b=int(input("enter the number of class held"))
# # a=int(input("enter the cls attended"))
# # att=((a/b)*100)
# # print("percentage of class attended",att)
# # if att>=75:
# #     print(" allowed to sit in exm")
# # else:
# #     print("not allowed to sit in exm")

# # a=int(input("enter age"))
# # b=input("enter sex")
# # c=input("enter martial status")
# # if b=="female":
# #     print("she work in the urban area")

# # if b=="male":
# #     if a>20 and a<40:
# #         print("he may work in anywhere")
# #     elif a>40 and a<60:
# #         print("work in urban")
# #     else:
# #         print("error")


# a=int(input("enter the age1"))
# b=int(input("enter the age2"))
# c=int(input("enter the age3"))
# if a>b and a>c:
#     print("a is greater")
#     if b>c:
#         print("c is smallest")
#     else:
#         print("b is smallest")
# elif b>c:
#     print("b is greater")
#     if a>c:
#         print("c is smallest")
#     else:
#         print("a is smallest")
# else:
#     print("c is greater")
#     if a>b:
#         print("b is samllest")
#     else:
#         print("a is smallest")

# a=int(input("enter the number"))
# if a%2==0 and a%5==0:
#     print(a,"is divisible")
# elif a%2==0:
#     print("divisible by 2")
# elif a%5==0:
#     print("divisible by 5")
# else:
#     print(a,"is not divisible")

# n=int(input("enter a number"))
# d1=n%10 
# d2=(n//10)%10
# d3=(n//100)%10
# d4=n//1000
# reverse=d1*1000+d2*100+d3*10+d4
# print("reverse",reverse)

# n=int(input("enetr a number"))
# m=int(input("enetr a number"))
# print("before swap a",n,"b",m)
# n,m=m,n
# print("after swap a",n,"b",m)

# n=int(input("enter a acc balance"))
# m=int(input("enter a whitrwal amnt"))
# if m<=n:
#     if m%100==0:
#         print("sucessfull")
#     else:
#         print("enter amount in multiples of 100")
# else:
#     print("insufficent balance")

# n=int(input("enter the salary"))
# m=int(input("enter the credit score"))
# k=int(input("enter the loan amnt"))
# if n>=30000:
#     if m>=700:  
#         if k<=20*n:
#             print("loan approved")
#         else:
#             print("loan amnt to0 high")
#     else:
#         print("improve credit score")
# else:
#     print("low income")

# n = input("Enter Food Type  : ")
# if n == "veg" :
#     print("Paneer :500, veg biriyani : 500")
#     d = input("Enter Food  : ")
#     q = int(input("Enter Quantity : "))
#     if d == "paneer,veg" :
#         b = 1000*q
#     else :
#         b = 500*q
#     if b>=1000 :
#         print("Bill = ",b, "Discount ",(b/100)*10)
#     else:
#         print("Bill = ",b, "No discount")

# else :
#      print("Chicken , Fish")
#      d = input("Enter Food  : ")
    #  q = input("Enter Quantity : ")

# WHILE LOOP

# i=0
# while i<5:
#     print("hello")
#     i+=1

# n=int(input("enetr the number"))
# i=0
# while i<=n:
#     print("num",i+1)
#     i+=1
i=1
# while i<10:
#     print("num",i+1)
#     i+=1
# else:
#     print("loop end")

# PASS STATEMENT


# i=0
# while i<5:
#     print("hello")
#     if i == 3:
#          break
#     i+=1
i=0
# while i<10:
#     print("num",i)
#     if i == 5:
#          break
#     i+=1
i=1
# while i<=20:
#     if i%2==0:
#         print("num",i)
#     i+=1
# i=2
# while i<=20:
#     print(i)
#     i+=2
# i=5
# while i<=100:
#     print(i)
#     i+=5
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     print(i)
#     i+=2
# i=1
# while i<=10:
#     if i==5:
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=0
# while i<10:
#     if i==3:
#         pass
#     print(i)
#     i+=1
# i=1
# v=0
# while i<=10:
#     v=v+i
#     i+=1
# print(v)
# i=1
# v=1
# while i<=10:
#     v=v*i
#     i+=1
# print(v)
# i=1
# while i<20:
#     if i==10:
#       break
#     print(i)
#     i+=1






# i=1
# while i<=20:
#   if i%2==0:
#     i+=1
#     continue
#   print(i)
#   i+=1

# i=1
# while i<100:
#   n=int(input("enter a number" ))
#   if n<0:
#     break
#   i+=1


# i=10
# while i<100:
#   print(i)
#   i-=1 
#   if i==0:
#     break   


# i=1
# while i<=20:
#   if i%2==0:
#     print(i)
#   i+=1

# i=0
# while i<=20:
#   if i%2!=0:
#     print(i)
#   i+=1

# n=int(input("enter a NUMBER"))
# while i<=10:
#     k=0
#     k=n*i
#     print(n,"*",i,"=",k)
#     i+=1


  
# n=int(input("enter a number"))
# if n>1:

#     i=2
#     while i<=n:
#         if n%i==0:
#             print ("not prime")
#             break
#         i+=1
#     else:
#         print ("prime")
# else:
#     print("Not a prime")

# n=int(input("enter a number"))
# temp=n
# reverse=0
# while n>0:
#     dig=n%10
#     reverse=reverse*10+dig
#     n=n//10
# if temp==reverse:
#     print("palindrome")
# else:
#     print("not pallindrome")




