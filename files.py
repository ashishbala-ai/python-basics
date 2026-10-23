# open (filename ,mode)
# mode what the modes do
# "r"  opening the file (default)
# "w"  open for writing(first truncatr the file)
# "x"  open for exclusive creation (fall if file already exixt)
# "a"  open for writig (appends to file if it exists)
# "b   binary mode"
# "t"  text mode
# "+"  open for updating (read and write)


#  f=open("ds.txt","x")
# f=open("ds.txt","w")
# # f.write("hi ash")
# f.write("hiiiiii ash")
# f.close()

# file reading

# f=open("ds.txt","r")
# print(f.read())
# f.close


# file appending

# f=open("ds.txt","a")
# f.write("\n data science \n python \n data analtics")
# f.close()

# file read line by line readlines

# f=open("ds.txt","r")
# print(f.readlines())
#  f.close()

# tell() cureent position of cursor

# f=open("ds.txt","r")
# print(f.read(5))
# print(f.tell())

# f=open("ds.txt","w")
# f.write("ashish")
# print(f.tell())
# f.close()

# seek() moves the cursr position

# f=open("ds.txt","r")
# f.seek(3)
# print(f.read())

# f=open("ash.txt","w")
# # f.write("ash\nashish\ndata")
# # f=open("ash.txt","r")
# # print(f.readlines())

# f=open("ash.txt","a")
# for i in range(1,101):
#     f.write(str(i))
#     f.write("\n")
# f.close()

# f=open("ash.txt","r")
# print(f.read())


# import os
# os.remove("eg.txt")         #file remove
# os.remove("example.txt")       # folder removal

# import shutil
# shutil.rmtree("eg.txt")     #willl delete a folder

# with open("ash.txt","w") as f:
#     f.write("python")

with open("ash.txt","w") as f:
    f.write("ashish\n21\ndata science")
with open ("ash.txt","r") as f:
   print( f.read())