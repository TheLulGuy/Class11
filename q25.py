coordinates = {}
quadrants = []
for n in range(1, 5):
    print(f'Enter coordinate number {n}')
    x = int(input('Enter x coordinate: '))
    y = int(input('Enter y coordinate: '))
    coordinates[n] = {'x':x, 'y':y}
    if x > 0:
        if y > 0:
            quadrants.append(1)
        if y < 0:
            quadrants.append(4)
    elif x < 0:
        if y > 0:
            quadrants.append(2)
        elif y < 0:
            quadrants.append(3)



for index, item in enumerate(quadrants):
    print(f'Coordinate {index+1} is in Quadrant no. {item}')