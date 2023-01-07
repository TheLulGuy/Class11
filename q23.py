from time import sleep 
# Menu driven program
'''
1) Add new team details
Accept team name, No. matches won, and No. of matches
lost. Store this information in a dictionary where team name
is the key and its corresponding value is a list of the form
[wins, losses].

2) Print winning Percentage of a given team
Ask the user to enter a team name, compute and print out the
team's winning percentage. Print appropriate message if the
given team’s name does not exist in the dictionary.

3) Display list of number of matches won by all teams
Using the dictionary, create a list whose entries are the
number of wins of each team. Display the list. Print
appropriate message if the dictionary is empty.

4) Display list of teams with zero losses
Using the dictionary, create a list of all those team names
that have only winning record i.e. the team has zero losses.
Display the list. Print appropriate message if the
dictionary/list is empty.

5) Exit
'''
def wait():
    sleep(1)
def cool_exit():
    print('Exiting..')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('Done!')
    exit(0)

teams = {}
while True:
    print('''
--------------------------------------------------------
Choose appropriate option: 

1) Add new team details
2) Print winning Percentage of a given team
3) Display list of number of matches won by all teams
4) Display list of teams with zero losses
5) Exit
--------------------------------------------------------
''')
    choice = int(input())
    match choice:
        case 1:
            name = input('Enter name of team: ')
            if name in teams.keys():
                print('Name is already there.')
                wait()
                continue
            wins = int(input('Enter number of wins: '))
            loses = int(input('Enter number of loses: '))
            teams[name] = [wins, loses]
        case 2:
            name = input('Enter name of team to be checked: ')
            if name not in teams.keys():
                print('Name is not there.')
                wait()
                continue
            data = teams[name]
            print(f'Percentage: {data[0]/sum(data) * 100}')
            wait()
        case 3:
            for key, item in teams.items():
                print(f'{key} : {item[0]}')
            wait()
        case 4:
            a = []
            for key, item in teams.items():
                if item[1] == 0:
                    a.append(key)
            if a == []:
                print('No teams with 0 losses: ')
                wait()
            else:
                print('Teams with 0 losses:', a)
                wait()
        case 5:
            cool_exit()
        case 666 | 69 | 420:
            print('WRONG')
            exit(0)
        case _:
            print('Enter a proper value: ')
