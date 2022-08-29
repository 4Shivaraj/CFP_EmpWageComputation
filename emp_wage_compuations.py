import random
from emp_log import get_logger

lg = get_logger("(class_method)", file_name="emp_log.log")


class Employee:
    def __init__(self, emp_wage_hour, max_working_days, max_working_hours):
        self.emp_wage_hour = emp_wage_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours

    def calculate_emp_wage(self):
        """
        in this function added checking maximum working days and hours of an employee.
        :return: None.
        """

        try:
            emp_wage_per_month = 0
            emp_working_days = 0
            emp_working_hours = 0
            while emp_working_days < self.max_working_days and emp_working_hours < self.max_working_hours:
                emp_check = random.randint(0, 2)
                lg.info(emp_check)
                emp_dict = {1: 8, 2: 4, 0: 0}
                working_hour = emp_dict.get(emp_check)
                daily_wage = working_hour * self.emp_wage_hour
                lg.debug(" daily wage of an employee {}".format(daily_wage) if daily_wage != 0 else
                         "employee is absent")
                emp_wage_per_month += daily_wage
                emp_working_hours += working_hour
                emp_working_days += 1
            lg.info("Days the employees have worked: {} ".format(emp_working_days))
            lg.debug("Employee wage for month: {}".format(emp_wage_per_month))
            lg.debug("Hours the employees have worked: {} ".format(emp_working_hours))
            return

        except Exception as e:
            lg.error(e)


if __name__ == '__main__':
    emp_wage_hour = 20
    max_working_days = 20
    max_working_hours = 100

    emp_wage_check = Employee(emp_wage_hour, max_working_days, max_working_hours)
    emp_wage_check.calculate_emp_wage()
