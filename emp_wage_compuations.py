import random
from emp_log import get_logger

lg = get_logger("(MultipleCompany)", file_name="emp_log.log")


class Employee:
    def __init__(self, company_name, emp_wage_hour, max_working_days, max_working_hours):
        self.company_name = company_name
        self.emp_wage_hour = emp_wage_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours

    def calculate_emp_wage(self):
        """
        This function used for checking employee wages for multiple company.
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
            lg.info("Name of the company: {}".format(self.company_name))
            lg.info("Days the employees have worked: {} ".format(emp_working_days))
            lg.debug("Employee wage for month: {}".format(emp_wage_per_month))
            lg.debug("Hours the employees have worked: {} ".format(emp_working_hours))
            return

        except Exception as e:
            lg.error(e)


if __name__ == '__main__':

    emp1_wage = Employee("FlipKart", 20, 20, 100)
    emp1_wage.calculate_emp_wage()
    emp2_wage = Employee("Amazon", 30, 19, 110)
    emp2_wage.calculate_emp_wage()

