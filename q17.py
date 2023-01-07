tup = ()
for item in range(5):
    input_ = input('Enter string: ')
    tup += (input_, )

shortest = min(tup, key=len)
print(f'Shortest string: {len(shortest)}')

