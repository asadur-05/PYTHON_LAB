# Swap two numbers
def swap(a,b):
    temp = a
    a = b
    b= temp
    print("Swaped Value: ", a , b)

X = int(input("Enter 1st Value:"))
Y = int(input("Enter 2nd Value:"))
swap(X,Y)
