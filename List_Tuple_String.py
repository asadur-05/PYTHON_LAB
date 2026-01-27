tup = (3,4,5)
print("Original Tuple: ", tup)
#1) Tuple Value Change using typecasting
li = list(tup)
li[0] = "Lets Learn "
li[1] = "PYTHON"
li[2] = "Coding"
print(li)
tup = tuple(li)
print("Again converted in tuple",tup)
print(type(tup))

#2) Tuple Value Changing using Concatination
li = (12,) + tup[1:]
print(li)

li = [2,4,3,10,25,45,17,20,30,80]
print(li[0:])
print(li[1:9:2])
print(li[-3])
print("Reverse Printing",li[::-1])


str = "Md. Asadur Rahaman"
str2 = "Hello," + " " + str
print(str2)
str[0] = "S" #return error string is immutable
print(str)

str = "racecar"
str2 = "Asadur"
print(str == str[::-1])
print(str2 == str2[::-1])
