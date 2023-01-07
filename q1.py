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
    match choice:
        case '1':
            arr = []
        case '2':
            arr.append(random.randint(1000, 9999))
        case '3':
            extra = eval(input('Enter what to extend: '))
            arr.extend(extra)
        case '4':
            item = int(input('Enter item to be removed: '))
            index = int(input('Enter index to be inserted in: '))
            arr.insert(index, item)
        case '5':
            item = int(input('Enter item to be removed: '))
            print('''
Choose:
    1) last element
    2) element at particular position
    3) the first occurrence of the element
''')
            c = input()[0]
            match c:
                case 1:
                    arr.pop()
                case 2:
                    index = int(input('Enter index: '))
                    arr.pop(index)
                case 3:
                    arr.remove(item)
                case _:
                    print('Enter proper choice: ')
                    continue
        case '6':
            encase_print(f'Biggest number: {max(arr)}', f'Smallest number: {min(arr)}')            
        case '7':
            dup = arr.copy()
            dup.sort()
            encase_print(f'Second largest: {dup[1]}', f'Second smallest: {dup[-2]}')
        case '8':
            dup = arr.copy()
            choice = input('(a)scending or (d)escending order? ')[0].lower()
            match choice:
                case 'a':
                    dup.sort()
                    encase_print(dup)
                case 'd':
                    dup.reverse()
                    encase_print(dup)
                case _:
                    print('Enter proper choice: ')
                    continue
        case '9':
            dup = arr.copy()
            dup.reverse()
            encase_print(dup)
        case 'c' | 'clear':
            arr.clear()
        case 'e' | 'exit':
            exit(0)
        case _:
            encase_print('Enter proper choice')