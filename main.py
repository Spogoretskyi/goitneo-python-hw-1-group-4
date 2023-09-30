from datetime import datetime

test_users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Alex Key", "birthday": datetime(1978, 2, 21)}, 
    {"name": "Hanna Jansen", "birthday": datetime(1983, 1, 1)}] 

def get_day(date):
    return date.strftime("%A")

def get_birthdays_per_week(users):
    days = {}
    current_date = datetime.today().date()

    for user in users:
        birthday = user["birthday"].date() 
        print(birthday)
        birthday_this_year = birthday.replace(year = datetime.year)
        print(birthday_this_year)
        day = get_day(user["birthday"])
        print(day)
        days[day] = user["name"]


print(get_birthdays_per_week(test_users))
    

