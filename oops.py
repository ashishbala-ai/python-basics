# # // OBJECT
# # // COLLECTION of data and its funcationalities
# # // similar to real world project

# # // CLASS
# # // BLUE print of an OBJECT
# # // using class we can create many object

# # // create a class
# #     // class Student:
# #     //     pass
# #     // s1=Student()
# #     // s2=Student()
# # class Student:
# #         name="ammu"
# #         age=129
# # s1=Student()
# # s2=Student()
# # print(s1.name)
# # print(s1.age)


# # class Student:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# # s1=Student("Alice",21)
# # s2=Student("Anu",22)
# # print(s1.name)
# # print(s1.age)
# # print(s2.name)
# # print(s2.age)

# # class Employee():
# #     def __init__(self,name,age,salary):
# #         self.name=name
# #         self.age=age
# #         self.salary=salary
# #     def display(self):
# #         print("name",self.name)
# #         print("age",self.age)
# #         print("salary",self.salary)
# # e1=Employee("ammu",21,20000)
# # e2=Employee("anu",22,21000)
# # e3=Employee("ali",23,23000)
# # e1.display()
# # e2.display()
# # e3.display()

# # class car():
# #     def __init__(self,brand,model):
# #         self.brand=brand
# #         self.model=model
# #     def display(self):
# #         print("model",self.model)
# #         print("brand",self.brand)
# # c1=car("maruthi",2014)
# # c2=car("maruthi",2024)
# # c1.display()
# # c2.display()

# # class num():
# #     def __init__(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def display(self):
# #         print("sum",self.a+self.b)
# # c1=num(4,6)
# # c1.display()

# class num():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print("sum",self.a+self.b)
#     def sub(self):
#         print("sub",self.a-self.b)
#     def mul(self):
#         print("product",self.a*self.b)
#     def div(self):
#         print("sum",self.a/self.b)
# c1=num(6,6)
# c1.add()
# c1.sub()
# c1.mul()
# c1.div()

# INHERITANCE

# inheritance means deriving a new class from an existing class
# a class inherits the property is know as child class
# the clss whos proprty is inherited is called the parent class

# class Animal():
#     def eat(self):
#         print("animal is eating")
# class dog(Animal):
#     def bark(self):
#         print("dog is barking")
# dog1=dog()
# dog1.eat()
# dog1.bark()

# class student():
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# class mark(student):
#     def __init__(self, name, roll,maths,science):
#         super().__init__(name, roll)
#         self.maths=maths
#         self.science=science
#     def display(self):
#         print("name",self.name)
#         print("roll",self.roll)
#         print("maths",self.maths)
#         print("science",self.science)
# c1=mark("ash",21,85,90)
# c1.display()

# Single inheritance

# parent class is inherited by a single child class tehn the relation is single inheritance

# Multi level inheritance

# the concept of inheriting the member from multiple class into a single classs is multi level inheritance
#  the cild class can be a paraent class to the another child class and process go on
# it is also called multiple level inheritance

# Multiple level inheritance

# if a single child class inherits two or more claasses then the relation between the child class 
# and the multiple parent class is know as multiple inheritance
# all the members of the class that are being inherited are acessible by the child 
# the parent class that the child class inherits are declared in an oder using parathesis

# class childclass(parent class1 ,parent class2)

# # heirarchical inheritance
# a single parent will have multiple childclassbwhich are at the same level and the memebrs of the pareent class are acessible to all the childclass
# child one member is not acessible foe child2

# hybrid inheritance

# if a class has diffrent types of inheritance implemented in it ,thenn this inheritance is know as the hybrid
# as the name itself therewill be two or more inheritance implemented


# class Grand():
#     def gdisplay(self):
#         print("i am the grand parent")
# class Parent(Grand):
#     def pdisplay(self):
#         print(" i am the parent")
# class Child(Parent):
#     def cdisplay(self):
#         print("i am child")
# c=Child()
# c.gdisplay()
# c.pdisplay()
# c.cdisplay()

# class Grand():
#     def gdisplay(self):
#         print("i am the grand parent")
# class Parent(Grand):
#     def pdisplay(self):
#         print(" i am the parent")
# class Child(Parent,Grand):
#     def cdisplay(self):
#         print("i am child")
# c=Child()
# c.gdisplay()
# c.pdisplay()
# c.cdisplay()

# class A:
#     def show (self):
#         print("class a")
# class B(A):
#     def show (self):
#         print("class b")
# class C(A):
#     def show (self):
#         print("class c")
# class D(B,C):
#     pass
# print(D.__mro__)
# obj=D()
# obj.show()
# print(obj.show())

# class parent():
#     def show(self):
#         print("parent class")
# class child1(parent):
#     def dis(self):
#         print("first child")
# class child2(parent):
#     def dis(self):
#         print("second child")
# c1=child1()
# c2=child2()
# c1.show()
# c2.show()


# class hi():
#     def bank(self):
#         print("SBI")
# class hello(hi):
#     def account(self):
#         print("savings account")
# class di(hello):
#     def customer(self):
#         print("viswa")
# c1=di()
# c2=hello()
# c3=hi()
# c3.bank()
# c2.account()
# c1.customer()

# class vehicle():
#     def info(self):
#         print("i am a vechile")
# class car(vehicle):
#     def carinfo(self):
#         print("i am a car")
# class eletric(car):
#     def battery(self):
#         print("i run on eletricity")
# c1=eletric()
# c1.info()
# c1.carinfo()
# c1.battery()

# class person():
#     def store(self):
#         print("ash")
# class student(person):
#     def roll(self):
#         print("21")
# class mark(student):
#     def ma(self):
        
#         print("78")
#         print("87")
#         print("89")
# c1=mark()


# from abc import ABC, abstractmethod
# class shape (ABC):
#     @abstractmethod
#     def area (self):
#         pass
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area (self):
#         return 3.14*self.radius**2
# class rectangele(shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
# c1=circle(5)
# print("Aea ",c1.area())
# c2=rectangele(4,5)
# print(c2.area())
from abc import ABC, abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class upi(payment):
#     def pay (self):
#         print("paid by upi")
# class cash(payment):
#     def pay(self):
#         print("paid by cash")
# class cod(payment):
#     def pay(self):
#         print("paid by cod")   
# c1=upi()
# c2=cash()
# c3=cod()
# c1.pay()
# c2.pay()
# c2.pay()

# Encapsulation
# class person:
#     def __init__ (self,name,age):
#         self.name=name
#         self._age=age
# p1=person("alice",43)
# print("name",p1.name)
# print("age",p1._age)          acesss protected variable
# class person:
#     def __init__ (self,name,age):
#         self.name=name
#         self.__age=age
# p1=person("alice",43)
# print("name   :  ",p1.name)
# print("age",p1.__age)           this will raise an attributeerror


# POLYMORPHISM
# class animal():
#     def make(self):
#         pass
# class dog(animal):
#     def make(self):
#         print("wofff")
# class cat(animal):
#     def make(self):
#         print("mewow")
# a1=dog()
# a2=cat()
# a1.make()
# a2.make()

# # COMPILE TIME POLYMORPHISM
# class clac:
#     def add(self,a,b):
#         return a + b
#     def add(self,a,b,c):
#         return a + b + c
# c=clac()
# print(c.add(2,3))#this will call the second add ethid which has three aeugments and will raise a type error
# print(c.add(2,3,4))#the will call the second add method

# OPERTOR OVERLOADING
# class Number:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self,other):
#         return Number(self.value + other.value)
# n1=Number(5)
# n2=Number(10)
# res=n1+n2
# print(res.value)

# class bank_account():
#     def __init__ (self,bal):
#         self.__bal=bal
#         print("avialabe balance is",self.__bal)
#     def depo(self,dep):   
#         self.__bal+=dep     
#         print("the deposit amount is",dep, "the cuurent balaance is ",self.__bal)
#     def withdraw(self,withd):
#         if withd>self.__bal:
#             print("high withdrwal")
#         else:
#          self.__bal-=withd  
#          print("the deposit amount is",withd, "the cuurent balaance is ",self.__bal)   
# n1=bank_account(5000)
# n1.depo(1000)
# n1.withdraw(6000)


# class car():
#     def key(self):
#         print("car")
# class lap():
#     def key(self):
#         print("lap")
# a1=car()
# a2=lap()
# a1.key()
# # a2.key()

# class student():
#     def info(self):
#         print("im student")
# class teacher():
#     def info (self):
#         print("i am a teacher")
# class principal():
#     def info(self):
#         print("i am prici")
# def dis(objects):
#     for obj in objects:
#         obj.info()
# people=[student(),teacher(),principal()]    #craete a lisst of object
# dis(people)

class employee():
    def salary(self):
        print("salary")
        
class manager(employee):
    def salary(self):
        print("salary is 500000")

class devloper(employee):
    def salary(self):
        print("salary is 600000")
m=manager()
n=devloper()
m.salary()
n.salary()