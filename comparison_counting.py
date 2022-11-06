# comparison counting
import time
import random

arr = list(range(1, 10001))  # list of integers from 1 to 100000 adjust these boundaries to fit your needs
random.shuffle(arr)
# first and last element before sorting
print("first and last element before sorting\n", arr[0], " ", arr[len(arr) - 1])

# print(arr) # <- List of unique random numbers
# arr = [1, 4, 3, 2, 6, 5, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7]
n = len(arr)
b = [0 for i in range(n)]
c = [0 for i in range(n)]
st_time = time.time()
for i in range(0, n - 1):  # (element 1 till (n) th)
    for j in range((i + 1), n):  # (element 2 till n th)
        if arr[i] < arr[j]:
            c[j] = c[j] + 1
        else:
            c[i] = c[i] + 1
et_time = time.time()
# time taken
print(et_time - st_time, " seconds")

# print((et_time-st_time)/1000000 , " seconds")

for i in range(n):
    b[c[i]] = arr[i]
# first and last element after sorting
print("first and last element after sorting\n", b[0], " ", b[len(b) - 1])
# print(b)
