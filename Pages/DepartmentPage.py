from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage


class DepartmentPage(BasePage):

    _page_head = (By.XPATH, '//*[@id="content"]/h1')
    _add_dept_btn = (By.XPATH, '//*[@id="content"]/a')
    _name_field = (By.ID, 'department_name')
    _alter_approv_field = (By.ID, 'department_alternate_approver_id')
    _create_dept_btn = (By.NAME, 'commit')
    _success_alert = (By.CLASS_NAME, 'alert alert-success alert-dismissable')

    @property
    def page_header(self):
        return self.find('_page_head')

    @property
    def add_department(self):
        return self.find('_add_dept_btn')

    @property
    def add_depart_name(self):
        return self.find('_name_field')

    @property
    def alternate_approve(self):
        return self.find('_alter_approv_field')

    @property
    def create_department(self):
        return self.find('_create_dept_btn')

    @property
    def success_box(self):
        return self.find('_success_alert')

