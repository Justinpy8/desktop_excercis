import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.yahoo.com/")
time.sleep(2)
driver.find_element_by_link_text("Sign in").click()
username_input = driver.find_element_by_name("username")
username_input.clear()
username_input.send_keys("sleepingbeaz@yahoo.com")
username_input.send_keys(Keys.RETURN)
time.sleep(1)
pw = driver.find_element_by_id("login-passwd")
pw.send_keys("Zhixiang84")
driver.find_element_by_xpath('//*[@id="login-signin"]').click()


# time.sleep(2)
# pw_input.send_keys(Keys.RETURN)




# GMAIL Login:

# driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# time.sleep(2)
# # driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a").click()
# username_input = driver.find_element_by_xpath('//*[@id="identifierId"]')
# username_input.send_keys("justin.ma8419@gmail.com")
# driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
# time.sleep(3)
# password_input = driver.find_element_by_name('password')
# password_input.send_keys('20190103')
# driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()




