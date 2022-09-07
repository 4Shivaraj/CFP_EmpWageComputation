import pytest
from emp_wage_compuations import Employee, Company
from emp_log import get_logger

lg = get_logger("(pytest_log)", file_name="emp_log.log")


@pytest.fixture
def emp_object():
    """
    :return: employee object
    """
    try:
        return Employee("shivaraj", 20, 20, 100, "web developer", 987345676)
    except Exception as e:
        lg.error(e)


@pytest.fixture
def company_object():
    """
    :return: company object
    """
    try:
        return Company("tata")
    except Exception as e:
        lg.error(e)


def test_calculate_emp_wage(emp_object, company_object):
    """
    testing calculating employee wage function
    :param emp_object: object of employee class
    :param company_object: object of company class
    :return: None
    """
    try:
        total_wage = emp_object.calculate_emp_wage()
        print(total_wage)
        assert isinstance(total_wage, int)
    except Exception as e:
        lg.error(e)


def test_add_employee(emp_object, company_object):
    # len(company_object.employee_dict) used __len__ method for protecting employee dictionary
    """
    testing add employee function
    :param emp_object: object of employee class
    :param company_object: object of company class
    :return: None
    """
    try:
        assert len(company_object) == 0
        company_object.add_employee(emp_object)
        assert len(company_object) == 1
        emp2 = Employee("mahesha", 20, 18, 100, "web developer", 986534567)
        company_object.add_employee(emp2)
        assert len(company_object) == 2
        print(len(company_object))
    except Exception as e:
        lg.error(e)


def test_get_employee(emp_object, company_object):
    """
    testing get employee function
    :param emp_object: object of employee class
    :param company_object: object of company class
    :return: None
    """
    try:
        company_object.add_employee(emp_object)
        actual = company_object.get_employee("shivaraj")
        assert isinstance(actual, Employee)
        assert actual.emp_name == "shivaraj"
        print(actual.emp_name)
    except Exception as e:
        lg.error(e)


def test_update_employee(emp_object, company_object):
    """
    testing update employee function
    :param emp_object: object of employee class
    :param company_object: object of company class
    :return: None
    """
    try:
        company_object.add_employee(emp_object)
        company_object.update_employee("shivaraj", 25, 28, 95, "python", 9854567876)
        assert emp_object.max_working_hours == 95
        print(emp_object.max_working_hours)
        assert emp_object.emp_wage_hour == 25
        print(emp_object.emp_wage_hour)
    except Exception as e:
        lg.error(e)


def test_delete_employee(emp_object, company_object):
    """
    testing delete employee function
    :param emp_object: object of employee class
    :param company_object: object of company class
    :return: None
    """
    try:
        company_object.add_employee(emp_object)
        assert len(company_object) == 1
        company_object.delete_employee("shivaraj")
        assert len(company_object) == 0
        print(len(company_object))
    except Exception as e:
        lg.error(e)

"""
============================= test session starts =============================
collecting ... collected 5 items

test_emp_wage_computations.py::test_calculate_emp_wage PASSED            [ 20%]2000

test_emp_wage_computations.py::test_add_employee PASSED                  [ 40%]2

test_emp_wage_computations.py::test_get_employee PASSED                  [ 60%]shivaraj

test_emp_wage_computations.py::test_update_employee PASSED               [ 80%]95
25

test_emp_wage_computations.py::test_delete_employee PASSED               [100%]0


============================== 5 passed in 0.02s ==============================
"""