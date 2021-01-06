'''Write a Python program to calculate the number of days between two dates.
 Sample dates : (20200702), (20200711)'''

from datetime import date

first_date=date(2020, 7, 2)
last_date=date(2020, 7 , 11)
no_of_days=last_date-first_date
print(f" {no_of_days} difference between two dates")