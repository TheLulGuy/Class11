sentence = input('Enter a sentence: ').split()
dictionary = {item: sentence.count(item) for item in sentence}
print(dictionary)