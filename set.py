# o={1,2,3,4,5,6}
# print(o)
# print(type(o))

# o={1,2,2,2,2,2,3,3,3,4,5}
# print(o)                         returns only unique values no dulicates

# a={'a',0,1,True,False,'hi'}
# print(a)                         NO ODER

# d={1,2,3,4,5,6}
# d.add(7)
# print(d)
# d.remove(2)
# print(d)

# s1={1,2,3,4,5}
# s2={3,4,5,6,7}
# d=s1.union(s2)
# print(d)
# print(s1|s2)

# x=s1.intersection(s2)
# print(x)
# x=s1.difference(s2)
# print(x)
# print(s2-s1)

# x=s1.symmetric_difference(s2)
# print(x)
# x=s1^s2
# print(x)

# x=s1.intersection_update(s2)
# print(s1)

# x=s1.difference_update(s2)
# print(s1)

# x=s1.symmetric_difference_update(s2)
# print(s1)

# num={1,2,3,4,5,6,7,8,9}
# odd={1,3,5,7,9}
# even={2,4,6,8}
# print(num.issuperset(odd))
# print(num.issuperset(even))
# print(num.issubset(odd))
# print(odd.issubset(num))
# print(even.isdisjoint(odd))

# odd={1,3,5,7,9}
# # odd.discard(9)
# # print(odd)

# # odd.remove(7)
# # print(odd)

# print(odd.discard(10))

# pop
# 
# odd={1,3,5,7,9}
# x=odd.pop()
# print(x)
# print(odd)

# copy

a={1,2,3}
b={3,5,6}
a.update(b)
print(a)