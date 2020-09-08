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

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)
result_msg_list = result_msg.split()
print(result_msg_list)

print("Refining the number of results:")
result_msg_num = int(result_msg_list[1].replace(",", ""))
# result_numbers = int(result_msg_num.replace(",", ""))
print(result_msg_num)

print("Refining the result time:")
result_msg_time = float(result_msg_list[3].replace("(", ""))
# result_time = float(result_msg_time.replace("(", ""))
print(result_msg_time)

assert result_msg_num > 20000000, "Results are less than 20 millions."
print("Verifying result number is passed.")

assert result_msg_time < 1, "The search took more than 1 second."
print("Verifying search performance passed.")

# if result_msg_num > 2000000:
#     print("It returned more than 2 million results")
# else:
#     print("It returned less than 2 million results")
#
# if result_msg_time < 2:
#     print("It took less than 2 seconds to complete the search.")
# else:
#     print("It took more than 2 seconds to complete the search.")
print("Test is completed, closing the browser...........")
driver.close()
