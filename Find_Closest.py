import numpy as np

numbers = [10, 220, 600, 300, 400]
target = 26

arr = np.array(numbers)
closest = arr[np.abs(arr - target).argmin()]

print("Closest number is:", closest)
