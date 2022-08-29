import random
from emp_log import get_logger

lg = get_logger("(emp_attendance)", file_name="emp_log.log")


class Employee:

    def __init__(self, emp_present):
        self.emp_present = emp_present

    def calculate_emp_wage(self):
        """
        this function will check the attendance of an employee.
        :return: None.
        """
        try:
            emp_check = random.randint(0, 1)
            if emp_check == self.emp_present:
                lg.info(emp_check)
                lg.debug("Employee is present")
            else:
                lg.debug("Employee is absent")
            return
        except Exception as e:
            lg.error(e)


if __name__ == '__main__':
    emp_wage_check = Employee(1)
    emp_wage_check.calculate_emp_wage()
