from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, time
from time import sleep
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait

#Create Webdriver
driver = webdriver.Chrome()
driver.get("https://bluesourcestaging.herokuapp.com/login")

#Login to bluesource
user_name_field = driver.find_element_by_id("employee_username").send_keys("company.admin")
pass_word_field = driver.find_element_by_id("employee_password").send_keys("123")
login_btn = driver.find_element_by_name("commit").submit()
if driver.find_element_by_id("search-bar").is_displayed():
    print("Pass: Login Successful")
else:
    print("Fail: Login not Sucessful")

#create new department in admin departments homepage
admin_btn = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]").click()
dropdown = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]/ul/li/a[1]").click()
dept_button = driver.find_element_by_xpath('//*[@id="content"]/a').click()

dept_name_field = driver.find_element_by_id("department_name").send_keys("Orasi2019")
control_select = driver.find_element_by_id("department_alternate_approver_id")
Select(control_select).select_by_visible_text("Company Admin")
submit_dept_button = driver.find_element_by_name("commit").click()

if driver.find_element_by_xpath('//*[@id="content"]/div[1]').is_displayed():
    print("Pass: Departments Section Found")
else:
    print("Fail: Departments Section Not Found")


#Add employee to newly created department
employee_btn = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[7]/a").click()
if driver.find_element_by_xpath('//*[@id="resources-per-page"]/label').is_displayed():
    print("Pass: Employee homepage is displayed")
else:
    print("Fail: Employee homepage not displayed")

emp_add_btn = driver.find_element_by_xpath('//*[@id="all-content"]/div[2]/div/div[2]/button').click()
sleep(2)
emp_add_user = driver.find_element_by_name("employee[username]").send_keys('carla.wilson18')
emp_add_first = driver.find_element_by_id("employee_first_name").send_keys("Carla")
emp_add_last = driver.find_element_by_id("employee_last_name").send_keys("Wilson")
emp_drp_down = driver.find_element_by_id("employee_department_id")
Select(emp_drp_down).select_by_visible_text("Orasi2019")
emp_btn_create = driver.find_element_by_name("commit").click()
if driver.find_element_by_xpath('//*[@id="all-content"]/div[1]').is_displayed():
    print("Pass: Employee Successfully Creaed in Department")
else:
    print("Fail: Employee Was Not Successfully Created in department")
sleep(3)

#Update employee to newly created department
upd_emp = driver.find_element_by_css_selector('input#search-bar.form-control').send_keys("Aaron Rogers")
sleep(1)
upd_emp_click = driver.find_element_by_css_selector('a[href="employees/72"].ng-binding').click()
sleep(2)
upd_emp_edit = driver.find_element_by_css_selector('#accordion > div > div:nth-child(5) > button').click()
sleep(2)
upd_emp_dept = driver.find_element_by_id("employee_department_id")
Select(upd_emp_dept).select_by_visible_text("Orasi2019")
upd_emp_create = driver.find_element_by_name("commit").click()
if driver.find_element_by_xpath('//*[@id="content"]/div[1]').is_displayed():
    print("Pass: Employee Successfully Creaed in Department")
else:
    print("Fail: Employee Was Not Successfully Created in department")

#Delete an existing department from Bluesource
del_dept = driver.find_element_by_css_selector('body > header > div > nav > ul > li:nth-child(1) > a').click()
del_dept_dropdown = driver.find_element_by_css_selector('a[href="/admin/departments"]').click()

# del_dept_btn = driver.find_element_by_css_selector("#content > div > ul:nth-child(59) > li").click()
links = driver.find_elements_by_css_selector("h2 > a")

links = driver.find_elements_by_css_selector("#content > div > ul:nth-child(58) > li > div > a:nth-child(2)")
# for link in links:
#     if link.find_element_by_tag_name("Orasi2019") == True:
# assert isinstance(link, object)
dept_trash = driver.find_element_by_css_selector('#content > div > ul:nth-child(58) > li > div > a:nth-child(2) > span').click()
alert = driver.switch_to_alert()
alert.accept()
print('Deletion successful')
