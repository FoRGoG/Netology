from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
import emoji
import os
if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.now())
    print(emoji.emojize('Life is :thumbs_up:'))
    print(os.getcwdb())