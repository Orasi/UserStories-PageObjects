from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage


class EmployeePage(BasePage):

    _add_btn = (By.XPATH, '//*[@id="all-content"]/div[2]/div/div[2]/button')
    _employ_userN = (By.ID, 'employee_username')
    _employ_Fname = (By.ID, 'employee_first_name')
    _employ_Lname = (By.ID, 'employee_last_name')
    _employ_dept = (By.ID, 'employee_department_id')
    _create_employ = (By.NAME, 'submit')
    _success_alert = (By.CLASS_NAME, 'alert alert-success alert-dismissable')


    @property
    def add_employ_button(self):
        return self.find('_add_btn')

    @property
    def employee_username(self):
        return self.find('_employ_userN')

    @property
    def employee_FirstN(self):
        return self.find('_employ_Fname')

    @property
    def employee_LastN(self):
        return self.find('_employ_Lname')

    @property
    def employee_department(self):
        return self.find('_employ_dept')

    @property
    def create_employee(self):
        return self.find('_create_employ')

    @property
    def success_created(self):
        return self.find('_success_alert')


