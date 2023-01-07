# Dummy values
# d1 = {'a': 1, 'b':2, 'c':1}
# d2 = {'b':7, 'a':0}
d1, d2 = eval(input('Enter value for d1: ')), eval(input('Enter value for d1: '))
 
print('Overlapping keys: ')
for item in d1.keys():
    if item in d2.keys():
        print(item)
