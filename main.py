from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    calculate_salary()
    print(f'Current date: {datetime.today().strftime("%d/%m/%Y")}\n')
    get_employees()
    print(f'at {datetime.today().strftime("%d/%m/%Y")}')