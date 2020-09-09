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
password_input = driver.find_element_by_id("login-passwd")
password_input.send_keys("Zhixiang84")
driver.find_element_by_xpath('//*[@id="login-signin"]').send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element_by_link_text("Mail").click()
time.sleep(1)
driver.find_element_by_xpath(
    '//*[@id="mail-app-component"]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/ul/li[3]/a').click()
time.sleep(2)
incoming_email_address = driver.find_element_by_xpath("//span[@class='u_N C_Z1VRpVF']").text
print(incoming_email_address)
email_address = incoming_email_address.split('@')
email = email_address[1].replace(">", "")
print(f"Email domain: {email}")

if email == "amazon.com":
    print("Moving to the next email.")
    driver.find_element_by_xpath("//div[@class='ab_C k_w D_F H_7bcz en_0 P_2bJhi p_R m_Z14vXdP I_52qC gl_FM']//span[2]//button[1]//span[1]").click()
else:
    print("Closing the email.")
    driver.find_element_by_link_text("Delete").click()

# driver.find_element_by_xpath("//span[contains(text(),'Delete')]").click()


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
