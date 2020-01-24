import config
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

url = "https://ping.apex.sh/login"

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get(url)

driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/button[1]").click()

username = driver.find_element_by_id('login_field')
username.send_keys(config.github_account)

password = driver.find_element_by_id('password')
password.send_keys(config.github_password)

driver.find_element_by_name('commit').click()

time.sleep(10)

driver.get("https://ping.apex.sh/ibm_cognitive_class/")

time.sleep(10)

driver.find_element_by_xpath("//text()[. = 'Add Check']/parent::*").click()

driver.find_element_by_css_selector('input[name="name"]').send_keys(config.stack_name)

for exisiting_element in driver.find_elements_by_xpath('//span[@class="_subtext_7vxv1_15"]'):
    if exisiting_element.text == config.stack_url:
        sys.exit('URL already exists, please change it in configuration \n')

driver.find_element_by_css_selector('input[name="url"]').send_keys(config.stack_url)

driver.find_element_by_xpath('//button[. ="Save"]').click()
