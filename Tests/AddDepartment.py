from Helpers.BaseTest import BaseTest
from Pages.BHomePage import BHomePage
from Pages.DepartmentPage import DepartmentPage
from time import sleep
from TestSteps.Test_Steps import test_login_steps
from selenium.webdriver.support.select import Select


class AddDepartment(BaseTest):

    def test_add_dept(self):
        add_deparment = "Federal Investigation Department"
        # Login to Bluesource
        test_login_steps(self)

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
        # sleep(2)
        #
        # html_list = self.driver.find_element_by_class_name('block')
        # items = html_list.find_elements_by_class_name('list-group')
        # for item in items:
        #     text = item.text
        #     if text == 'Federal Investigation Department':
        # print(text)
        #
        # sleep(5)