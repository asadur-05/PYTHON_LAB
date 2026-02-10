a = [1,10,2]
b = a #creating a reference variable 
c=a.copy() #creating a new list.
b.append(3)
c.append(4)
print("Original List =>",a)
print("Copy using '=' =>",b)
print("Using Copy method =>",c)

import copy
a = [[1,2],[3,4]]
b = copy.deepcopy(a) #creating a new list.
b[0].append(10)
print(a)
print(b)

i ="I am bust right now"
print(i)
split_i = i.split()
reversed_i = split_i[:: -1]
reverse_join = " ".join(reversed_i)
print(reverse_join)

#one line
print(" ".join(i.split()[::-1]))

a =[2,5,4,10,1,5,3]
print(a[5:1:-1])

b = ([2,3],[4,5,10])
b[0].append(5)
print(b)
b[0][0] +=1
print(b)
b[0]=   [7,8]
print(b) #return error because we are trying to change the reference of tuple element which is not allowed
