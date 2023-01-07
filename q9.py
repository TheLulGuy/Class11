even, odd = [], []
n = int(input('Enter length of list: '))
for item in range(n):
    input_ = int(input('Enter a number: '))
    if input_ % 2 == 0:
        even.append(input_)
    else:
        odd.append(input_)

print(f'Even: {even}')
print(f'Odd: {odd}')