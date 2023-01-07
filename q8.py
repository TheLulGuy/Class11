def rotation(arr):
    last = arr[-1]
    del arr[-1]
    arr.insert(0, last)
    print(arr)

a = eval(input('Enter list: '))
rotation(a)