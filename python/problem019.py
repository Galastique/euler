import datetime

#Variable
sundays = 0

#For every year
for year in range(1901,2001):

    #For every month
    for month in range(1,13):

        #Get weekday of first day of the month
        day = datetime.date(year, month, 1)
        weekday = day.weekday()

        #If day 1 = sunday count it
        if weekday == 6:
            sundays += 1

#Displays answers
print(sundays) #Expected 171