# enter actual date and time
# ise datetime module
import datetime


def tage_bis_jahresende(keydate):
    end = datetime.datetime(2024, 12, 31)
    return end - keydate


def tage_bis_datum(keydate):
    today = datetime.datetime.now()
    return today - keydate


# def actual_date_time():
# x = actual_date_time_str = "19.12.2024"

##### 1st part ################################


print("1.actual date and time: ")
today = datetime.datetime.now()
print(today.strftime("%d.%m.%Y %H:%M:%S"))


##### 2nd part ################################

print("2.days left until end of year")


difference = tage_bis_jahresende(today)
print(f"remainnig days {difference}")

##### 3rd part ################################

print("3.user defined date")

user_date = input("enter a date DD.MM.YYYY: ")

difference = tage_bis_datum(user_date)

print(difference)

# actual_date_time()

# calculate how many days are left until end of the year
date_str = "2024.12.18"
date_str = "19.12.2024"

start = datetime.datetime(2024, 12, 18)
end = datetime.datetime(2024, 12, 31)
difference = end - start
print(difference)
