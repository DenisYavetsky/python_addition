import datetime
import requests
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':

    print(f"Время запуска: {datetime.datetime.now()}")
    calculate_salary()
    get_employees()
    print(f"Время завершения: {datetime.datetime.now()}")
