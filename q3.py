n = int(input('Enter length of list: '))
arr = []
for item in range(n):
    arr.append(int(input('Enter a number: ')))

print('Sum: ', sum(arr))
print('Average: ', sum(arr)/n)
