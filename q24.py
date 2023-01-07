database = {}
while True:
    key = input('Enter product name: ')
    if key == 'quit':
        print('Exited.\n')
        break
    price = int(input('Enter price of product: '))
    database[key] = price
    print('Added!\n')

print('Initiated database.......')
while True:
    name = input('Enter product name: ')
    if name in database:
        print(database[name])
    elif name == 'quit':
        print('Exited.')
        exit(0)
    else:
        print('Product does not exist')
