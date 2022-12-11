'Automate the browser with Selenium'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time



chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options); 
driver = webdriver.Chrome('c:/Users/amirb/Desktop/amazon_selenium/chromedriver.exe')
driver.get('https://quist-client.web.app/#/')
driver.maximize_window()



# menu_btn = driver.find_element_by_id('nav-hamburger-menu')
# menu_btn.click()
# time.sleep(1)
# login_btn = driver.find_element_by_id('hmenu-customer-name')
# login_btn.click()
# time.sleep(4)

username_field = driver.find_element("flt-text-editing transparentTextEditing")
username_field.send_keys('shota')
username_field.send_keys(Keys.RETURN)
time.sleep(4)
# password_field = driver.find_element_by_id('ap_password')
# with open('password.txt', 'r') as x:
#     password = x.read()
# password_field.send_keys(password)
# password_field.send_keys(Keys.RETURN)
# print('You are logged in!')
# time.sleep(4)

# search_field = driver.find_element_by_id('twotabsearchtextbox')
# search_field.send_keys('Spiderman Statue')
# search_loop = driver.find_element_by_class_name('nav-right')
# search_loop.click()
# print('The search was made succesfully!')