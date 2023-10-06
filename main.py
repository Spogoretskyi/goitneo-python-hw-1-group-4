from collections import defaultdict
from datetime import datetime

test_users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Alex Key", "birthday": datetime(1978, 2, 21)},
    {"name": "John Jay", "birthday": datetime(1972, 10, 15)},
    {"name": "Felix Marc", "birthday": datetime(1974, 10, 18)},
    {"name": "Huan Madeiro", "birthday": datetime(1983, 10, 16)},
    {"name": "Alex Kahn", "birthday": datetime(1966, 10, 17)},
    {"name": "July Prescot", "birthday": datetime(1988, 10, 18)},
    {"name": "Alan Trudo", "birthday": datetime(1987, 10, 8)},
    {"name": "Jane Bik", "birthday": datetime(1990, 10, 9)},
    {"name": "James Lime", "birthday": datetime(1991, 10, 10)},
    {"name": "Kate Blanc", "birthday": datetime(1989, 11, 1)},  
    {"name": "Hanna Jansen", "birthday": datetime(1983, 1, 1)}] 

def get_day(date):
    return date.strftime("%A")

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    current_year = datetime.today().year
    current_date = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year = current_year)

        if birthday_this_year < current_date:
            birthday_this_year.replace(year = current_year + 1)

        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7 and delta_days > 0:
            day = get_day(user["birthday"])

            if day in ("Saturday", "Sunday"):
                day = "Monday"
            
            birthdays_per_week[day].append(name)

    return birthdays_per_week


print(get_birthdays_per_week(test_users))
    

