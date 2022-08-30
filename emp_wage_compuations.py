import random
from emp_log import get_logger

lg = get_logger("(WageForMultipleCompany)", file_name="emp_log.log")


class Company:
    def __init__(self, company_name, emp_data):
        self.company_name = company_name
        self.emp_data = emp_data

    def company_dict(self):
        company_wage_data = {}
        company_wage_data.update({self.company_name: self.emp_data})
        return company_wage_data


class Employee:
    def __init__(self, emp_name, salary_details_dict, company_name,
                 emp_wage_hour, max_working_days, max_working_hours):
        self.emp_name = emp_name
        self.salary_details_dict = salary_details_dict
        self.company_name = company_name
        self.emp_wage_hour = emp_wage_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours

    def salary_dict(self, emp_name, emp_wage):
        self.salary_details_dict.update({emp_name: emp_wage})
        return self.salary_details_dict

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
            salary_data = self.salary_dict(self.emp_name, emp_wage_per_month)
            lg.info("salary_data: {}".format(salary_data))
            lg.info("Name of the company: {}".format(self.company_name))
            lg.info("Days the employees have worked: {} ".format(emp_working_days))
            lg.debug("Employee wage for month: {}".format(emp_wage_per_month))
            lg.debug("Hours the employees have worked: {} ".format(emp_working_hours))
            return salary_data

        except Exception as e:
            lg.error(e)


if __name__ == '__main__':
    flipkart_emp1_wage = Employee("Shivaraj", {}, "FlipKart", 30, 20, 100).calculate_emp_wage()
    flipkart_emp2_wage = Employee("Cheluvesh", {}, "FlipKart", 20, 25, 105).calculate_emp_wage()
    amazon_emp1_wage = Employee("gayathri", {}, "Amazon", 28, 18, 95).calculate_emp_wage()
    amazon_emp2_wage = Employee("raksha", {}, "Amazon", 35, 15, 90).calculate_emp_wage()
    flipkart_emp1_wage.update(flipkart_emp2_wage)
    amazon_emp1_wage.update(amazon_emp2_wage)
    flipkart = Company("FlipKart", flipkart_emp1_wage).company_dict()
    amazon = Company("amazon", amazon_emp1_wage).company_dict()
    lg.debug(flipkart)
    lg.debug(amazon)
