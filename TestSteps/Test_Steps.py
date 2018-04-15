from Pages.Login import Login
from Pages.BHomePage import BHomePage
from Pages.DepartmentPage import DepartmentPage
from time import sleep
from selenium.webdriver.support.select import Select


def test_login_steps(self):
        user_name = "company.admin"
        pass_word = "123"
        self.driver.get('https://bluesourcestaging.herokuapp.com/login')
        login = Login(driver=self.driver)
        home = BHomePage(driver=self.driver)
        login.sync()

        login.username_field.send_keys(user_name)
        login.password_field.send_keys(pass_word)
        login.login_button.click()
        home.sync()
        assert home.admin_button, "Home Page is not displayed"


def test_add_dept_steps(self):
    add_deparment = "Federal Investigation Department"

    # Click on admin and departments in BS Toolbar
    home = BHomePage(driver=self.driver)
    home.admin_button.click()
    home.dept_dropdown.click()

    # Add Department in Departments Page
    dept_page = DepartmentPage(driver=self.driver)
    dept_page.sync()

    assert dept_page.add_department, "Element: %s Not Displayed" % dept_page.add_department
    dept_page.add_department.click()
    dept_page.add_depart_name.send_keys(add_deparment)
    Select(dept_page.alternate_approve).select_by_visible_text('Company Admin')
    sleep(2)
    dept_page.create_department.click()
    dept_page.sync()

    assert dept_page.success_box, "The %s was not created" % dept_page('Federal Investigation Department')


