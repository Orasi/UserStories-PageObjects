from Helpers.BaseTest import BaseTest
from Pages.EmployeePage import EmployeePage
from time import sleep
from TestSteps.Test_Steps import test_login_steps, test_add_dept_steps
from selenium.webdriver.support.select import Select
from Pages.BHomePage import BHomePage


class AddEmployee(BaseTest):

    def test_add_emplopyee(self):

        # User variable
        username = 'Afweroki.Isaias'
        first_name = 'Isaias'
        last_name = 'Afweroki'
        department = 'Federal Investigation Department'

        # Login to BlueSource
        test_login_steps(self)

        # Add department the new employee will be created in
        test_add_dept_steps(self)

        # Click on employee button in nav bar
        home = BHomePage(driver=self.driver)
        home.employ_button.click()
        employee_page = EmployeePage(driver=self.driver)
        employee_page.sync()

        # Create the new Employee in (selected department) Note: Must run Add Department Step
        employee_page.add_employ_button.click()
        sleep(2)
        employee_page.employee_username.send_keys(username)
        employee_page.employee_FirstN.send_keys(first_name)
        employee_page.employee_LastN.send_keys(last_name)
        Select(employee_page.employee_department).select_by_visible_text(department)
        employee_page.create_employee.click
        employee_page.sync()
        assert employee_page.success_created, "The Employee %s was not sucessfully created" % username

