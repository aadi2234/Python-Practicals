#12.	Write a Python program to check if the input year is a leap year of not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

year = int(input("Enter a year: "))
is_leap_year(year)
    