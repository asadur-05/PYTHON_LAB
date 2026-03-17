
a =["Avengers", "Iron Man", "Captain America", "Thor", "Hulk"]
print(a)
#2)Access element in list in python
print(a[0])
print(a[1])
#3)Modify list in python.
a[0] = "Iron Man"
a[1] = "Black Widow"
print(a)
#4)Add remove elements in list in python.
b=[10,25,45,17]
b.append(20)
b.append(30)
print(b)
b.remove(25)
print(b)

#5)Copy list using slicing
c = b[:]
print("Copied List:", c)

#6)Copy list using constructor
d = list(b)
print("Copied List using constructor:", d)
