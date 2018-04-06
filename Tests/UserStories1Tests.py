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

if driver.find_element_by_class_name('Departments').is_displayed():
     print("Pass: Departments Section Found")
else:
     print("Fail: Departments Section Not Found")




