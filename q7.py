n = int(input('Enter length of lists: '))
a, b, c = [], [], []
for index in range(n):
    a.append(int(input('Enter number for first list: ')))
    b.append(int(input('Enter number for second list: ')))
    print()
    c.append(a[index] + b[index])

print(a, b, c, sep='\n')