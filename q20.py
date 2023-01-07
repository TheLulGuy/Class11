months = {
    'January':31,    
    'February':28,
    'March':31,
    'April':30,
    'May':31,
    'June':30,
    'July':31,
    'August':31,
    'September':30,
    'October':31,
    'November':30,
    'December':31,
}

def pretty_print(opening, message):
    print(opening)
    print(message)
    print()

pretty_print('Alphabetical order: ', sorted(months.items(), key=lambda x:x [0]))
pretty_print('No. of days: ', sorted(months.items(), key=lambda x: x[1]))
pretty_print('Months with 31 days: ', {item: months[item] for item in months.keys() if months[item] == 31})