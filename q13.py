tup = eval(input('Enter a tuple: '))
n = int(input('Enter item from tuple to be removed: '))
index = tup.index(n)
result = tup[:index] + tup[index+1:]
print(result)