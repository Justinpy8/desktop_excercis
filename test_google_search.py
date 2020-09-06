import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.google.com/')
print("opening the web site")
time.sleep(1)

search_box = driver.find_element_by_name("q")
search_box.clear()
search_box.send_keys("selenium python")
time.sleep(2)

search_box.send_keys(Keys.RETURN)
time.sleep(1)

result_msg_list = list()
result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)

result_msg_list.append(result_msg)

print('*****result are being saved into a list*****')
print(result_msg_list)

result_num.split() = result_msg_list
print(result_num)
