# # n=input("enter a string")
# # print(n[0],n[-1])

# # s="abcdef"
# # print(s[::2])


# # s="shhhhhh"
# # reverse=""
# # for char in s:
# #     reverse=char+reverse
# # print(reverse)

# # s="abdefa"
# # d=len(s)
# # print(s[d//2])

# # s="typeing"
# # d=s[0]
# # f=s[-1]
# # c=f+s[1:-1]+d
# # print(c)

# # n=input("enter a sentence")
# # f=n.split(" ")
# # print(f)
# # for word in f:
# #     print(word[0].upper()+word[1::],end=" ")

# # vowels
# n=input("enter a string")
# count=0
# for char in n :
#     if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#         count+=1
# print(count)


# n=input("enter a sentence")
# f=n.split(" ")
# print("-".join(f))

# n=input("eneter a string")
# v=""
# for char in n:
#     if char=="!" or char=="?":
#         continue
#     else:
#         v+=char
# print(v)

# n=input("enter a string")
# for char in n:
#     if char.islower():
#         break
# print("is upper")

# n=input("enter a string")
# count=0
# for char in n:
#     b=n.count(char)
#     if char==" ":
#         continue
#     if b>1:
#         print("second occ : ",char,b)



# n=input("enter the string")
# for i in range (len(n)):
#     if n[i]=="e":
#         print(" e found at",i)

# s=input("enterstring")
# sub=input("sub")
# n=s.split(" ")
# for words in n:
#     if words==sub:
#         print("found at")
#     else:
#         print("not")

# t=(10,20,30,40)
# print(t[0])
# print(t[-1])
# print(t[1:4])

# t=(10,20,30,40,50)
# l=list(t)
# print(l)
# l.append(60)
# print(l)
# t=tuple(l)
# print(t)

# t=(10,20,30,40,50)
# j=max(t)
# print(j)
# f=min(t)
# print(f)

# t=(10,20,30,40,50,20,20)
# y=int(input("enter a element"))
# count=0
# d=t.count(y)
# print(d)

# t=(10,20,30)
# (a,b,c)=t
# print(a)

# t1=(1,2,3)
# t2=(4,5,6)
# t1,t2=t2,t1 
# print(t2)

# t=(1,2,3,[4,5])
# l=list(t)
# print(l[3])
# l[3][0]=6
# l[3][1]=7
# print(l)

# t=(42,56,47,32,58,12,95,75,2)
# l=list(t)
# l.sort()
# print(l)


# t1=(1,2,3)
# t2=(4,5,6)
# res=[]
# for i in range(3):
#     res.append(t1[i]+t2[i])
# print(res)
# t=tuple(res)
# print(t)

# t=(1,2,2,3,4,4,5)
# d=set(t)
# print(d)
# t=tuple(d)
# print(t)

# t=[]
# k=int(input("enter a number"))
# for i in range(k):
#     g=int(input("enter a number"))
#     t.append(g)
# print(t)
# b=[]
# for j in t:
#     if j%2==0:
#         b.append(j)
# print(b)

# e=[]
# stu=(
# ("alice",18,78),
# ("ali",18,88),
# ("angel",18,79))
# for i in range(len(stu)):
#    e.append( stu[i][2])
# p=e.index(max(e))
# print(stu[p])

# r={"apple","banana","cherry"}
# print(r)

# r={"apple","banana","cherry"}
# r.append("orange")
# print(r)

# r={"apple","banana","cherry"}
# r.remove("banana")
# print(r)
# r={"apple","banana","cherry"}
# r.discard("banana")
# print(r)


# r={"apple","banana","cherry"}
# print("apple" in r)


# r={"apple","banana","cherry"}
# d=len(r)
# print(d)

# a={1,2,3}
# b={3,4,5,6}
# print(a.union(b))

# a={1,2,3}
# b={3,4,5,6}
# print(a.intersection(b))   

# a={1,2,3}
# b={3,4,5,6}
# print(a.difference(b))   
# print(b.difference(a))

# a={1,2,3}
# b={3,4,5,6}
# print(a.symmetric_difference(b))

# a=[1,2,3,3,4,4,4,5]
# p=set(a)
# print(p)

# s1={10,20,30}
# s2={20,40,50}
# s1,s2=s2,s1
# print(s1)

# s1={10,20,30,40,50}
# s2={20,40,50}
# print(s2.issubset(s1))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))


# values=[1,2,3]
# keys=['ten','twenty','thirty']
# d=dict.fromkeys(values,keys)
# print(d)

# employees=['kelly','emma']
# default={'designation':'designation','salary':8000}
# d=dict.fromkeys(employees,default)
# print(d)

# stu={"ammu":(20,"a","sda"),
#       "ammz":(25,"b","das"),
#       "ali":(5,"a","sddd")   
#    }
# print(stu)

# Dict1 = {'name' : "Ammu",
# 	'age' : 20,
# 	'mark' : 86}
# Dict2 = {'Place' : 'Kochi',
# 'Course' : 'Python',
# 'Grade' : "A"}
# Dict1.update(Dict2)
# print(Dict1)

# d1 = {"name" : "Ammu",
# 	"age" : 20,
# 	"mark" : 86}
# d2={}
# print(d1)
# for i,j in d1.items():
#     d2.setdefault(j,i)
# print(d2)

# x={i:i*i for i in range(1,11) }
# print(x)

# x={i:i*i for i in range(1,21) if i %2==0 }
# print(x)

# x={i:i**3 for i in range(1,21) }
# print(x)

l=["hello", "my", "name", "is", "ash"]
h={i:len(i) for i in l}
print(h)











