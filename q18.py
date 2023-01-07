def input_records():
    return (input('Enter name of student: '), int(input('Enter marks: ')), int(input('Enter marks: ')), int(input('Enter marks: ')))

def information(tup, n):
    print(f'Student {n}: ')
    tup = tup[1:]
    print(f'Max score: {max(tup)}')
    print(f'Min score: {max(tup)}')
    print(f'Sum: {sum(tup)}')
    print(f'Average: {sum(tup)/3}')
    print()

a = (input_records(),input_records(),input_records(),input_records(),input_records())
print()
for index, item in enumerate(a):
    information(item, index+1)