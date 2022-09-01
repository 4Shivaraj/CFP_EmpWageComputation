import random
from emp_log import get_logger

lg = get_logger("(CrudOperations)", file_name="emp_log.log")


class Employee:
    def __init__(self, emp_name, emp_wage_hour, max_working_days, max_working_hours, department, phone_number):
        self.emp_name = emp_name
        self.emp_wage_hour = emp_wage_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.department = department
        self.phone_number = phone_number

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
                working_hour_dict = {1: 8, 2: 4, 0: 0}
                working_hour = working_hour_dict.get(emp_check)
                daily_wage = working_hour * self.emp_wage_hour
                lg.debug(" daily wage of an employee {}".format(daily_wage) if daily_wage != 0 else
                         "employee is absent")
                emp_wage_per_month += daily_wage
                emp_working_hours += working_hour
                emp_working_days += 1
            lg.info("Name of the employee: {}".format(self.emp_name))
            lg.info("Days the employees have worked: {} ".format(emp_working_days))
            lg.debug("Employee wage for month: {}".format(emp_wage_per_month))
            lg.debug("Hours the employees have worked: {} ".format(emp_working_hours))
            return

        except Exception as e:
            lg.error(e)

    def details(self):
        return f'employee name : {self.emp_name}, employee wage per hour: {self.emp_wage_hour},' \
               f'maximum working days: {self.max_working_days}, maximum working hours: {self.max_working_hours}', \
               f'department name: {self.department},phone number: {self.phone_number} '


class Company:
    def __init__(self, comp_name):
        self.comp_name = comp_name
        self.employee_dict = {}

    def add_employee(self, emp_obj):
        """
        :param emp_obj: is the object of employee class
        :return: None
        """
        try:
            self.employee_dict.update({emp_obj.emp_name: emp_obj})
        except Exception as e:
            lg.error(e)

    def update_employee(self, key, wage_per_hour, max_working_days,
                        max_working_hours, department, phone_number):
        """
        :param key: user string input
        :param wage_per_hour: user integer input
        :param max_working_days: user integer input
        :param max_working_hours: user integer input
        :param department: user string input
        :param phone_number: user integer input
        :return: None
        """
        try:
            employee = self.get_employee(key)
            if not employee:
                lg.debug("Employee is not available")
                return

            employee.wage_per_hour = wage_per_hour
            employee.max_working_days = max_working_days
            employee.max_working_hours = max_working_hours
            employee.department = department
            employee.phone_number = phone_number
            lg.debug("Updated successfully")
        except Exception as e:
            lg.error(e)

    def get_employee(self, emp_name):
        """
        :param emp_name: user string input
        :return: None
        """
        try:
            return self.employee_dict.get(emp_name)
        except Exception as e:
            lg.error(e)

    def display_employee(self):
        """
        this function display the details of employee
        :return: None
        """
        try:
            for key, value in self.employee_dict.items():
                lg.info(key)
                lg.info(value.details())
                print(key, value.details())
        except Exception as e:
            lg.error(e)

    def delete_employee(self, key):
        """
        this function display the details of employee
        :param key: user string input
        :return: None
        """
        try:
            contact = self.get_employee(key)
            if not contact:
                lg.debug("Employee is not available")
                return
            self.employee_dict.pop(key)
            lg.debug("Employee deleted successfully")
        except Exception as e:
            lg.error(e)


if __name__ == '__main__':
    company_name = input("Enter the company name:\n")
    company = Company(company_name)


    def add_():
        try:
            emp_name = input("enter your name:\n")
            wage_per_hour = int(input("enter the wage per hour:\n"))
            max_working_days = int(input("enter the maximum working days:\n"))
            max_working_hours = int(input("enter the maximum working hours:\n"))
            department = input("enter the department name:\n")
            phone_number = int(input("enter the phone number:\n"))
            emp_obj = Employee(emp_name, wage_per_hour, max_working_days, max_working_hours,
                               department, phone_number)
            company.add_employee(emp_obj)
        except Exception as e:
            lg.error(e)


    def display_():
        try:
            company.display_employee()
        except Exception as e:
            lg.error(e)


    def update_():
        try:
            key = input("Enter the name of employee to check exits or not:\n")
            if company.get_employee(key):
                wage_per_hour = int(input("enter the wage per hour:\n"))
                max_working_days = int(input("enter the maximum working days\n"))
                max_working_hours = int(input("enter the maximum working hours\n"))
                department = input("enter the department name\n")
                phone_number = int(input("enter the phone number\n"))
                emp = Employee(emp_name=key, emp_wage_hour=wage_per_hour, max_working_days=max_working_days,
                               max_working_hours=max_working_hours, department=department, phone_number=phone_number)
                company.add_employee(emp)

        except Exception as e:
            lg.error(e)


    def delete_():
        try:
            key = input("Enter the name of employee to check exits or not:\n")
            company.delete_employee(key)
        except Exception as e:
            print(e)

    def default():
        print("Invalid! Enter the correct choice")


    choice_dict = {1: add_, 2: display_, 3: update_, 4: delete_}

    while True:
        print("Enter the choice : \n1)Add contact \n2)Display contact\n3)update contact\n4)delete "
              "contact")
        choice = int(input())
        if choice in choice_dict.keys():
            choice_dict.get(choice)()
        else:
            default()
