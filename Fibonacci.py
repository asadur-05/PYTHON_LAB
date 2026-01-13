# Fibonacci Series
first = 0 
second = 1
num = int(input("Enter the range for Fibonacci Series: "))
print("Fibonacci Series: ")
print(first)
print(second)
for i in range(2, num):
    next = first + second
    print(next )
    first = second
    second = next 
