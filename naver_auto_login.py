import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("gyusik2780")
browser.find_element_by_id("pw").send_keys("rbtlr!@#$$")

browser.find_element_by_id("log.login").click()

time.sleep(3)

browser.find_element_by_id("id").clear()

print(browser.page_source)

browser.close()
browser.quie()


