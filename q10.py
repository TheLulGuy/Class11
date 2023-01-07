words = []
n = int(input('Enter length of list: '))
for item in range(n):
    words.append(input('Enter a word: '))

result = sorted(words, key=lambda x:len(x))
print(f'Largest: {result[-1]}')