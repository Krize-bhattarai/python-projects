import calendar

year = int(input('Enter year: '))
month = int(input('Enter month: '))

cal = calendar.monthcalendar(year, month)

print('Mon Tue Wed Thu Fri Sat Sun')

for week in cal:
    for day in week:
        if day == 0:
            print('    ', end = '')
        else:
            print(f'{day:4}', end='')
    print()   # new line after each week
