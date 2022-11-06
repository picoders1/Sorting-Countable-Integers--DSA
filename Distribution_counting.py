# distribution counting
import time
import random

arr = list(range(1, 1000001))  # list of integers from 1 to 100000 adjust these boundaries to fit your needs
# arrange elements in random range
random.shuffle(arr)
# first and last element before sorting
print("first and last element before sorting\n", arr[0], " ", arr[len(arr) - 1])

# print(arr) # <- List of unique random numbers
# arr = [1, 4, 3, 2, 6, 5, 7, 8, 9, 10]
n = len(arr)
# store upper and lower bounds and initial output array
low_B = min(arr)
upp_B = max(arr)
b = [0 for i in range(n)]
# initialize frequency
d = [0 for i in range(0, (upp_B - low_B + 1))]  # 0-n index
# compute frequency of each item
for i in range(0, n):
    j = arr[i] - low_B
    d[j] = d[j] + 1
# compute sum of accumulated frequencies
for i in range(1, (upp_B - low_B + 1)):
    d[i] = d[i] + d[i - 1]
# access item and insert into sorted vector based onn distribution value
st_time = time.time()
for i in range(n - 1, -1, -1):
    j = arr[i] - low_B
    d[j] = d[j] - 1
    b[d[j]] = arr[i]
et_time = time.time()
# time taken
print(et_time - st_time)
# first and last element before sorting
print("first and last element after sorting\n", b[0], " ", b[len(b) - 1])
# print(b)
