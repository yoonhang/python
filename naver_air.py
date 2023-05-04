from selenium import webdriver
import time
import requests

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser=webdriver.Chrome("D:\chromedriver.exe")
browser.maximize_window()
url="https://beta-flight.naver.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res=requests.get(url,headers=headers)
browser.get(url)

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

#이번달 27일, 28일 선택

browser.find_elements_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button").click()
time.sleep(1)
browser.find_elements_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button").click()

네이버 항공권부터 막히는데 해결하신 분 있나요?ㅜㅜ