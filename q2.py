arr = eval(input('Enter an entire list: '))
n = int(input('Enter number to be searched: '))

for item in arr:
    if item == n:
        print(f'Number found at index {arr.index(item)}')
        break
else:
    print('Number not found')
