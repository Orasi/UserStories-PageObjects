from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage


class BHomePage(BasePage):

    _admin_btn = (By.XPATH, '/html/body/header/div/nav/ul/li[1]/a')
    _project_btn = (By.XPATH, '/html/body/header/div/nav/ul/li[6]/a')
    _direct_btn = (By.XPATH, '/html/body/header/div/nav/ul/li[5]/a')
    _employ_btn = (By.XPATH, '/html/body/header/div/nav/ul/li[7]/a')
    _logout_btn = (By.XPATH, '/html/body/header/div/nav/ul/li[8]/a')
    _dept_drop = (By.XPATH, '/html/body/header/div/nav/ul/li[1]/ul/li/a[1]')

    @property
    def admin_button(self):
        return self.find('_admin_btn')

    @property
    def direct_button(self):
        return self.find('_direct_btn')

    @property
    def project_button(self):
        return self.find('_project_btn')

    @property
    def employ_button(self):
        return self.find('_employ_btn')

    @property
    def logout_button(self):
        return self.find('_logout_btn')

    @property
    def dept_dropdown(self):
        return self.find('_dept_drop')

