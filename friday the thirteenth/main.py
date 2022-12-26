"""
ID: james.f3
LANG: PYTHON3
TASK: friday
"""



fin, fout = open('friday.in', 'r'), open('friday.out', 'w')


years = int(fin.readline())
month_starting_day = 1
amounts = [0, 0, 0, 0, 0, 0, 0]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


for i in range(1900, 1900 + years):
    if str(i).endswith('00'):
        if i % 400 == 0:
            for month in range(0, 12):
                day = (month_starting_day + 12) % 7
                amounts[day] += 1
                month_starting_day = month_starting_day + leap[month] % 7

        else:
            for month in range(0, 12):
                day = (month_starting_day + 12) % 7
                amounts[day] += 1
                month_starting_day = month_starting_day + days_in_month[month] % 7

    else:
        if i % 4 == 0:
            for month in range(0, 12):
                day = (month_starting_day + 12) % 7
                amounts[day] += 1
                month_starting_day = month_starting_day + leap[month] % 7

        else:
            for month in range(0, 12):
                day = (month_starting_day + 12) % 7
                amounts[day] += 1
                month_starting_day = month_starting_day + days_in_month[month] % 7

fout.write(f'{amounts[6]} {amounts[0]} {amounts[1]} {amounts[2]} {amounts[3]} {amounts[4]} {amounts[5]}\n')

