arr = []
n = int(input('Enter length of list: '))
for item in range(n):
    input_ = int(input('Enter a number: '))
    if 1 <= input_ <= 15:
        arr.append(input_)

for index, item in enumerate(arr):
    if item > 10:
        arr[index] = 100
    
print(arr)