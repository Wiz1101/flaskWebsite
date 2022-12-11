from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
 
#--| Setup
options = Options()
options.add_argument("-incognito")
options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(executable_path=r'C:\cmder\bin\chromedriver.exe', options=options)
#--| Parse or automation
browser.get('https://quist-client.web.app/#/')
browser.maximize_window()


search_bar = browser.find_element('flt-text-editing transparentTextEditing')
search_bar.send_keys('Shota')
search_bar.submit() 
time.sleep(4)

# accept_button = browser.find_elements_by_css_selector('#L2AGLb')[0]
# accept_button.click()
# time.sleep(2)
# search_bar = browser.find_elements_by_css_selector('div.a4bIc > input')[0]
# search_bar.send_keys('2022')
# search_bar.submit() 