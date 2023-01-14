import random

def encase_print(*kwargs) -> None:
    print('-----------------------------')
    for item in kwargs:
        print(item)
    print('-----------------------------')

arr = 0
while True:
    print('''
1 - Create list
2 - Append a random 4 digit integer into the list
3 - Extend the list
4 - Insert an element into the list
5 - Remove an element from the list
6 - Print largest and smallest element in list
7 - Find second largest and smallest element in list
8 - Sort list in ascending or descending order
9 - Reverse the elements of a list
clear/c - Clear the list
exit/e - Exit
''')
    choice = input()
    if choice == '1':
        arr = []
    elif choice == '2':
        arr.append(random.randint(1000, 9999))
    elif choice == '3':
        extra = list(input('Enter what to extend: '))
        arr.extend(extra)
    elif choice == '4':
        item = int(input('Enter item to be removed: '))
        index = int(input('Enter index to be inserted in: '))
        arr.insert(index, item)
    elif choice == '5':
        item = int(input('Enter item to be removed: '))
        print('''
Choose:
    1) last element
    2) element at particular position
    3) the first occurrence of the element
''')
        c = input()[0]
        if c == '1':
            arr.pop()
        elif c == '2':
            index = int(input('Enter index: '))
            arr.pop(index)
        elif c == '3':
            arr.remove(item)
        else:
            print('Enter proper choice: ')
            continue
    elif choice == '6':
        encase_print(f'Biggest number: {max(arr)}', f'Smallest number: {min(arr)}')            
    elif choice == '7':
        dup = arr.copy()
        dup.sort()
        encase_print(f'Second largest: {dup[1]}', f'Second smallest: {dup[-2]}')
    elif choice == '8':
        dup = arr.copy()
        choice = input('(a)scending or (d)escending order? ')[0].lower()
        if choice == 'a':
            dup.sort()
            encase_print(dup)
        elif choice == 'd':
            dup.reverse()
            encase_print(dup)
        else:
            print('Enter proper choice: ')
            continue
    elif choice == '9':
        dup = arr.copy()
        dup.reverse()
        encase_print(dup)
    elif choice in ('c', 'clear'):
        arr.clear()
    elif choice in ('e', 'exit'):
        exit(0)
    else:
        encase_print('Enter proper choice')
