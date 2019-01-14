import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
chrome_options = Options()
driver = webdriver.Chrome(executable_path="/Users/ashokmishra/PycharmProjects/chromedriver", options=chrome_options)
# open instagram login page
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(5)
# enter username
driver.find_element_by_name("username").send_keys("your instagram username")
# enter password
driver.find_element_by_name("password").send_keys("your password")
# login button
driver.find_element_by_css_selector(".L3NKy").click()
# time.sleep(5)
# # send verification code button
# driver.find_element_by_xpath("//*[@id='react-root']/section/div/div/div[3]/form/span/button").click()
# time.sleep(5)
# # enter otp
# otp = driver.find_element_by_xpath("//*[@id='security_code']")
# txt = input("enter code")
# otp.send_keys(txt)
# time.sleep(5)
# # click on submit button
# driver.find_element_by_xpath("//*[@id='react-root']/section/div/div/div[2]/form/span/button").click()
time.sleep(5)
# click on not now
driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]").click()
time.sleep(5)
# click on profile
driver.find_element_by_css_selector("a.gmFkV").click()
time.sleep(5)
# get followers
dialog = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
# get number of followers
all_followers = int(driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text)
print(all_followers)
# get the following number
all_following = int(driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text)
print(all_following)
time.sleep(5)
# click on followers
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(15)
# main div class of followers list
main_class = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/ul")


for items in main_class:
    items.find_element_by_class_name("FPmhX")
    names = items.text
    print(names)
# close the followers window
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div[2]/button/span").click()

time.sleep(5)
# click on following
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
# time.sleep(5)
# following_class = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/ul/div")
#
# for i in following_class:
#     i.find_elements_by_class_name("_0imsa")
#     following_names = i
#     print(following_names)
time.sleep(5)
n = str(driver.find_element_by_class_name("FPmhX").text)
print(n)
li = []
li.append(n)
print(li)










