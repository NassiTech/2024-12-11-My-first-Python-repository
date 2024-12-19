#################################################################
# 2024-12-18 exercise 2
#
# see https://www.w3schools.com/python/python_datetime.asp
#################################################################

# We only need the datetime class and the timedelta class from the
# datetime module since we don't need access to other
# parts of the datetime module like datetime.date or
# datetime.time. Like this we don't need to qualify the
# datetime class with the module name, e.g. for the statement
# 'today = datetime.now()'

# import datetime
from datetime import datetime, timedelta


def tage_bis_jahresende(keydate):
    # The class datetime.strftime()
    # ("string format time")
    # converts a datetime object into a string
    # %Y = Year, full version (see URL above)
    year = int(keydate.strftime("%Y"))
    end_of_year = datetime(year, 12, 31)
    return end_of_year - keydate


def tage_bis_datum(keydate):
    today = datetime.now()
    return today - keydate


def wochentag_berechnen(keydate):
    # The class datetime.strftime()
    # ("string format time")
    # converts a datetime object into a string
    # %A = Weekday, full version
    return keydate.strftime("%A")


def zeit_in_zukunft(amount, unit):
    if unit == "hours":
        future = datetime.now() + timedelta(hours=amount)
    elif unit == "days":
        future = datetime.now() + timedelta(days=amount)
    elif unit == "minutes":
        future = datetime.now() + timedelta(minutes=amount)
    else:
        return ""

    return future.strftime("%d.%m.%Y %H:%M:%S")


##### 1st part ##################################################
print("\n")
print("1. Actual date and time")
today = datetime.now()
print(today.strftime("Date: %d.%m.%Y Time: %H:%M:%S"))
print("\n")

##### 2nd part ##################################################
print(f"2. Days left until end of year {today.strftime('%Y')} (excl. today)")
difference = tage_bis_jahresende(today)
print(f"Remainig days: {difference.days}")
print("\n")

##### 3rd part ##################################################
# print("3. User defined date")
# while True:
#  user_date_str = input("Enter a date (DD.MM.YYYY): ")

# try:
# datetime.strptime() converts a string to a datetime
# object ("string parse time")
# user_date = datetime.strptime(user_date_str, "%d.%m.%Y")
# except Exception as e:
#  print("\n")
#  print(f"Don't understand '{user_date_str}' - please try again!")
#  print("\n")
# else:
#   break

# remaining = tage_bis_datum(user_date)
# print(
# f"Remainig time until {today.strftime('%d.%m.%Y')} (excl.) ==> {remaining.days} days"
# )
# print("\n")

##### 4th part ##################################################
# print the day of the week for the date that
# the user entered in part 3
# print(f"4. Calculate day of week (for {user_date.strftime('%d.%m.%Y')})")
# week_day = wochentag_berechnen(user_date)
# print(f"Week day: {week_day}")
# print("\n")

##### 5th part ##################################################
# print("5. Calculate time shift")
# user_input = input("Enter time span (example: '5 hours'): ")
# split_input = user_input.split()
# ze_in_zu = zeit_in_zukunft(int(split_input[0]), split_input[1])
##if ze_in_zu != "":
# print(f"Future date/time: {ze_in_zu}")
# else:
#  print("Wrong unit! Allowed is only 'hours, minutes, days'")
# print("\n")


# ###############     new version -> start from zero from 3. User defined date   ##############################


# days_to_keydate is a function that calculates the number of days (between two days) ex: from today to an user entered date Link :
# the input parameter (selected_day).
# The function gives a return parameter Difference today - selected_day
# the user is asked to enter a date through input()
def days_to_keydate():
    today = datetime.now()

    user_date_str = input("enter a date format DD.MM.YYYY:")
    user_date = datetime.strptime(user_date_str, "%d.%m.%Y")
    difference = user_date - today
    return difference


days_to_keyday = days_to_keydate().days
print(f"{days_to_keyday}: ")
# the number of days without extra hours could be obtained in 3 different ways
# .days in the function definition that we want to run
# .days could be in the argument difference in line  118
# line 123 in the print after the argument days_to_keyday


################## new version of 4.-> start from zero Calculate day of week   ##############################
# day_of_the_week() is a function that compares the user entered date with calendar function
# the input parameter entered-day is transformed from a string to a datetime format with strptime
# the asked day is transformed from the datetime format again to string format strftime -> %A weekday
# the return value is a week day as a string type data
# day of the week link : https://stackoverflow.com/questions/36341484/get-day-name-from-weekday-int
# https://stackoverflow.com/questions/8380389/get-day-name-from-datetime
# https://stackoverflow.com/questions/8380389/get-day-name-from-datetime
# https://stackoverflow.com/questions/74853453/days-till-year-end
def day_of_the_week():
    today = datetime.now()
    user_date_str = input("enter a date format DD.MM.YYYY:")
    user_date = datetime.strptime(user_date_str, "%d.%m.%Y")
    week_day_str = user_date.strftime("%A")

    return week_day_str


user_date_str = day_of_the_week()
print(f"today is: {user_date_str} :")
