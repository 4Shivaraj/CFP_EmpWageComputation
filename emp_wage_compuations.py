import random
from emp_log import get_logger

lg = get_logger("(CrudOperations_MultipleCompany)", file_name="emp_log.log")


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

            employee.emp_wage_hour = wage_per_hour
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
    company_dict = {}


    def add_company_func():
        """
        Helper function to add a company
        :return: company dictionary
        """
        try:
            company_name = input("Enter the company name:\n")
            lg.info(company_name)
            company_object = Company(company_name)
            company_dict.update({company_object.comp_name: company_object})
            lg.debug("add_company {}".format(company_dict))
            return company_dict
        except Exception as e:
            lg.error(e)


    def display_company_func():
        """
        Helper function to display the company
        """
        try:
            for index, company_name in enumerate(company_dict.keys()):
                print(index, company_name)
        except Exception as e:
            lg.error(e)


    def add_employee_func():
        """
        Helper function to add the employee
        :return:
        """
        try:
            company_name = input("Enter the company name:\n")
            company_exist = company_dict.get(company_name)
            if company_exist is None:
                company_exist = Company(company_name)
                company_dict.update({company_exist.comp_name: company_exist})
            emp_name = input("enter your name:\n")
            wage_per_hour = int(input("enter the wage per hour:\n"))
            max_working_days = int(input("enter the maximum working days:\n"))
            max_working_hours = int(input("enter the maximum working hours:\n"))
            department = input("enter the department name:\n")
            phone_number = int(input("enter the phone number:\n"))
            emp_object = Employee(emp_name, wage_per_hour, max_working_days, max_working_hours, department,
                                  phone_number)
            company_exist.add_employee(emp_object)
            lg.debug(company_exist)
        except Exception as e:
            lg.error(e)


    def get_employee_func():
        """
        Helper function to get an employee
        :return: None
        """
        try:
            company_name = input("Enter the company name:\n")
            company_exist = company_dict.get(company_name)
            if company_exist is None:
                lg.debug("Company doesn't exist")
                return
            emp_name = input("enter employee name:\n")
            company_exist.get_employee(emp_name)
            lg.debug(company_exist)
        except Exception as e:
            lg.error(e)


    def update_employee_func():
        """
        Helper function to update an employee
        :return: None
        """
        try:
            company_name = input("Enter the company name:\n")
            company_object = company_dict.get(company_name)
            if company_object is None:
                lg.info("Company not found")
                return
            name = input("enter the employee name:\n")
            employee_object = company_object.get_employee(name)
            if employee_object is None:
                lg.debug("Employee not found")
                return
            wage_per_hour = int(input("enter the wage per hour:\n"))
            max_working_days = int(input("enter the maximum working days:\n"))
            max_working_hours = int(input("enter the maximum working hours:\n"))
            department = input("enter the department name:\n")
            phone_number = int(input("enter the phone number:\n"))
            company_object.update_employee(name, wage_per_hour, max_working_days, max_working_hours, department,
                                           phone_number)
            lg.info(company_object)

        except Exception as e:
            lg.error(e)


    def delete_employee_func():
        """
        Helper function to delete an employee
        :return: None
        """
        try:
            company_name = input("Enter the company name:\n")
            company_exist = company_dict.get(company_name)
            if company_exist is None:
                lg.debug("Company doesn't exist")
                return
            emp_name = input("enter employee name:\n")
            company_exist.delete_employee(emp_name)
            lg.info(company_exist)
        except Exception as e:
            lg.error(e)


    def display_employee_func():
        """
        Helper function to display employee
        :return: None
        """
        try:
            company_name = input("Enter the company name:\n")
            company_object = company_dict.get(company_name)
            if company_object is None:
                print("Company doesn't exist")
                return
            company_object.display_employee()
        except Exception as e:
            lg.error(e)


    def default():
        print("Invalid! Enter the correct choice")


    choice_dict = {1: add_company_func, 2: display_company_func, 3: add_employee_func, 4: get_employee_func,
                   5: delete_employee_func,
                   6: display_employee_func, 7: update_employee_func}

    while True:
        print("Enter the choice : \n1.add_company\n2.Display Company\n3.Add Employee \n4.Get Employee\n5.Delete "
              "Employee\n6.display_employees\n7.update_employees\n0.Exit")
        choice = int(input())
        if choice in choice_dict.keys():
            choice_dict.get(choice)()
        else:
            default()












"""
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
1
Enter the company name:
tata
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
(CrudOperations_MultipleCompany) - 2022-09-02 17:13:49,645 - INFO - tata
(CrudOperations_MultipleCompany) - 2022-09-02 17:13:49,645 - DEBUG - add_company {'tata': <__main__.Company object at 0x00000276ACE60E50>}
2
0 tata
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
3
Enter the company name:
tata
enter your name:
shivaraj
enter the wage per hour:
20
enter the maximum working days:
20
enter the maximum working hours:
100
enter the department name:
web
enter the phone number:
8765423456
(CrudOperations_MultipleCompany) - 2022-09-02 17:14:15,055 - DEBUG - <__main__.Company object at 0x00000276ACE60E50>
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
3
Enter the company name:
flipkart
enter your name:
mahesh
enter the wage per hour:
23
enter the maximum working days:
25
enter the maximum working hours:
105
enter the department name:
design
enter the phone number:
98765323456
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
(CrudOperations_MultipleCompany) - 2022-09-02 17:14:49,201 - DEBUG - <__main__.Company object at 0x00000276ACE60940>
4
Enter the company name:
flipkart
enter employee name:
mahesh
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
(CrudOperations_MultipleCompany) - 2022-09-02 17:15:01,159 - DEBUG - <__main__.Company object at 0x00000276ACE60940>
6
Enter the company name:
tata
shivaraj ('employee name : shivaraj, employee wage per hour: 20,maximum working days: 20, maximum working hours: 100', 'department name: web,phone number: 8765423456 ')
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
(CrudOperations_MultipleCompany) - 2022-09-02 17:15:11,187 - INFO - shivaraj
(CrudOperations_MultipleCompany) - 2022-09-02 17:15:11,187 - INFO - ('employee name : shivaraj, employee wage per hour: 20,maximum working days: 20, maximum working hours: 100', 'department name: web,phone number: 8765423456 ')
7
Enter the company name:
tata
enter the employee name:
shivaraj
enter the wage per hour:
26
enter the maximum working days:
15
enter the maximum working hours:
190
enter the department name:
web developer
enter the phone number:
9876456787
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
(CrudOperations_MultipleCompany) - 2022-09-02 17:15:46,453 - DEBUG - Updated successfully
(CrudOperations_MultipleCompany) - 2022-09-02 17:15:46,453 - INFO - <__main__.Company object at 0x00000276ACE60E50>
6
Enter the company name:
tata
shivaraj ('employee name : shivaraj, employee wage per hour: 26,maximum working days: 15, maximum working hours: 190', 'department name: web developer,phone number: 9876456787 ')
Enter the choice : 
1.add_company
2.Display Company
3.Add Employee 
4.Get Employee
5.Delete Employee
6.display_employees
7.update_employees
0.Exit
(CrudOperations_MultipleCompany) - 2022-09-02 17:15:52,768 - INFO - shivaraj
(CrudOperations_MultipleCompany) - 2022-09-02 17:15:52,768 - INFO - ('employee name : shivaraj, employee wage per hour: 26,maximum working days: 15, maximum working hours: 190', 'department name: web developer,phone number: 9876456787 ')

"""
