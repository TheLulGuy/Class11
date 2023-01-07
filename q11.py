n = int(input('Enter n: '))
lst = []
for item in range(n):
    lst.append(input('Enter word: ').lower())
no_vowels = []
for item in lst:
    if any(char in 'aeiou' for char in item):
        continue
    else:
        no_vowels.append(item)

print(f'Original: {lst}')
print(f'No vowels: {no_vowels}')
