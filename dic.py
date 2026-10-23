# a= {"name":"ammu",
#    "age": 20,
#    "course":"python"}
# # print(a)
# a["age"]=25
# print(a)
# for i in a:
#     print(i)
#     print(a[i])

# a= {"name":"ammu",
#    "age": 20,
#    "course":"python"}
# print(a)
# a["mark"]=85
# print(a)
# print(a.items())
# print(a.keys())
# print(a.values())

# for i in a.items():
#     print(i)
# for i in a.keys():
#     print(i)
# for i in a.values():
#     print(i)

# for key,value in a.items():
#     print(key,value)

# print(a["age"])
# print(a.get("age"))

# clear()
# a={"name":"ammu",
#    "age":20}
# # print(a)
# # a.clear()
# # print(a)

# x=a.copy()
# print(x)

# a= {"name":"ammu",
#    "age": 20,
#    "course":"python"}
# x=a.pop("course")         removes an key value pair
# print(x)
# print(a)

# a= {"name":"ammu",
#    "age": 20,
#    "course":"python"}
# x=a.popitem()             remove the last key value pair
# print(x)
# print(a)

# a={
#     "anu":[20,"A"],
#     "binu":[22,"B"],
#     "alice":[21,"A+"]
# }
# a.update({"Anu":[21,"A+"],"ali":[25,"B+"]})
# print(a)

# x=['a','b','c']
# z=dict.fromkeys(x,"m")
# print(z)

# x=['a','b','c']
# y=(1,2,3)
# z=dict.fromkeys(x,y)
# print(z)

a= {"name":"ammu",
   "age": 20,
   "course":"python"}
print(a)
x=a.setdefault("age",25)
print(x)
print(a)

x=a.setdefault("grade","d")
print(x)
print(a)