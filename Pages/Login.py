from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.NavigationBar import NavigationBar

class Login(BasePage):
    _username_field = (By.ID, 'employee_username')
    _pass_field = (By.ID, 'employee_password')
    _login_btn = (By.NAME, 'commit')
    _admin_btn = (By.CSS_SELECTOR, NavigationBar.admin_button)

    @property
    def username_field(self):
        return self.find('_username_field')

    @property
    def password_field(self):
        return self.find('_pass_field')

    @property
    def login_button(self):
        return self.find('_login_btn')

    @property
    def admin_button(self):
        return self.find('_admin_btn')

