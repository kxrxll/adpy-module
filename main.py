from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import names

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f'Actual date: {datetime.now().strftime("%A, %d. %B %Y %I:%M%p")}')
    for i in range(int(input('How many people you want to check? Type here: '))):
        print(names.get_full_name())
