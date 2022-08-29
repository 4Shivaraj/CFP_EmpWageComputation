import random
from emp_log import get_logger

lg = get_logger("(part_time_wage)", file_name="emp_log.log")


class Employee:

    def calculate_emp_wage(self):
        """
        in this function added checking part-time wage of an employee.
        :return: None.
        """
        try:
            emp_wage_hour = 20
            emp_check = random.randint(0, 2)
            lg.info(emp_check)
            emp_dict = {1: 8, 2: 4, 0: 0}
            working_hour = emp_dict.get(emp_check)
            daily_wage = working_hour * emp_wage_hour
            lg.debug(" daily wage of an employee {}".format(daily_wage) if daily_wage != 0 else
                     "employee is absent")

        except Exception as e:
            lg.error(e)


if __name__ == '__main__':
    emp_wage_check = Employee()
    emp_wage_check.calculate_emp_wage()
