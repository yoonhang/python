자동화 프로그램 은 1. 엑셀에서 주소를 읽어서 2. 토지이용계획확인서를 PDF 파일로 저장하는 프로그램입니다.
엑셀에서 주소를 읽어 오는 것,
selenium으로 웹페이지에 접속해서 주소를 입력하는 것까지 배운 내용대로 무난하게 잘 되었습니다만
PDF로 저장하기 위해 저장버튼을 누르면 팝업윈도우로 뜨게 되는 google "print-preview-app"을 다루지 못해 더 이상
진척이 없습니다. (130라인 #대상 이후)
google에서 이런 저런 키워드로 검색해 보았지만 아직 해법을 찾지 못했습니다.

기본편, 웹스크래핑, 업무자동화 강의를 다시 찾아 보았지만 프린터 다이알로그를 제어하는 방법은 없는 것 같아서
문의 드립니다.
프린터 다이알로그에서 [저장]을 선택하면 나오면 SaveAsFileName 다이알로그도 어떻게 다뤄야 할 지 궁금합니다.

바쁘시겠지만 지도 부탁드립니다. 감사합니다.


첨부파일을 올리는 기능이 없어서 작성한 코드를 아래에 첨부합니다.
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from tkinter import filedialog # filedialog


# options = webdriver.ChromeOptions()
# options.add_argument("User-Agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
browser = webdriver.Chrome(r"K:\data\Desktop\PythonWorkspace\chromedriver.exe")
# browser = webdriver.Chrome(r"K:\data\Desktop\PythonWorkspace\chromedriver.exe", options = options)

# 토지이음\토지이용계획열람 페이지
luris = "http://www.eum.go.kr/web/ar/lu/luLandDet.jsp#none" ## 신 서버
# luris = "http://www.luris.go.kr/web/actreg/arservice/ArLandUsePrintFrame.jsp" ## 구 서버

browser.get(luris)
# browser.minimize_window() # 브라우저 창 maximize ===> 실제 프로그램 실행 시 minimize 할 것 ###########
# browser.maximize_window()

# 토지이용계획열람 페이지의 handle
curr_handle = browser.current_window_handle


############ 엑셀에서 받아오는 값
s_sido = "경기도"
s_sigungu = "용인시 처인구"
s_eup = "이동읍"
s_li = "어비리"
s_san = "산"
s_bonbun = "2"
s_boobun = "2"
####################################


# 4.1 주소 선택 & 열람하기

#==========================================================

# 시도 선택
elem = Select(browser.find_element_by_xpath('//*[@id="selSido"]'))
elem.select_by_visible_text(s_sido)
browser.implicitly_wait(time_to_wait=5)

# 시군구 선택
elem = Select(browser.find_element_by_xpath('//*[@id="selSgg"]'))
elem.select_by_visible_text(s_sigungu)
browser.implicitly_wait(time_to_wait=5)

# 읍면동 선택
elem = Select(browser.find_element_by_xpath('//*[@id="selUmd"]'))
elem.select_by_visible_text(s_eup)
browser.implicitly_wait(time_to_wait=5)

# 리 선택
if s_li != "": # 리가 있으면 실행, 없으면 건너뛰기
elem = Select(browser.find_element_by_xpath('//*[@id="selRi"]'))
elem.select_by_visible_text(s_li)
browser.implicitly_wait(time_to_wait=5)

# 산 선택
elem = Select(browser.find_element_by_xpath('//*[@id="landGbn"]'))
elem.select_by_visible_text(s_san)
browser.implicitly_wait(time_to_wait=5)

# 본번 입력
elem = browser.find_element_by_xpath('//*[@id="bobn"]')
elem.send_keys(s_bonbun)
browser.implicitly_wait(time_to_wait=5)

# 부번 있으면 실행 없으면 건너뛰기
# 부번 입력
if s_boobun != "":
elem = browser.find_element_by_xpath('//*[@id="bubn"]')
elem.send_keys(s_boobun)
browser.implicitly_wait(time_to_wait=5)


# elem = browser.find_element_by_xpath('//*[@id="selSido"]/option[text()="경기도"]').click() # 시도 선택
# browser.implicitly_wait(time_to_wait=5)
# time.sleep(1)
# elem = browser.find_element_by_xpath('//*[@id="selSgg"]/option[text()="수원시 팔달구"]').click() # 시군구 선택
# time.sleep(1)
# elem = browser.find_element_by_xpath('//*[@id="selUmd"]/option[text()="인계동"]').click() # 읍면동 선택 ### '리'가 있다면 1초 후 리를 선택한다
# time.sleep(1)
# elem = browser.find_element_by_xpath('//*[@id="landGbn"]/option[text()="일반"]').click() # 산 선택
# time.sleep(1)
# elem = browser.find_element_by_xpath('//*[@id="bobn"]') # 본번 입력
# elem.send_keys("1043")
# elem = browser.find_element_by_xpath('//*[@id="bubn"]') # 부번 입력
# elem.send_keys("")

# '열람' 버튼 누르기
elem = browser.find_element_by_xpath('//*[@id="frm"]/fieldset/div[3]/p/span/a').click()

# 축척 선택
elem = browser.find_element_by_xpath('//*[@id="scale1"]')
if s_san == "일반":
elem.send_keys("1200") ### '일반' 지번 : 1/1200
else:
elem.send_keys("6000") ### '산' 지번 : 1/6000

# 축척 '변경' 버튼 누르기
elem = browser.find_element_by_xpath('//*[@id="appoint"]/div[4]/table/tbody/tr[2]/td/div[2]/span[2]/a').click()
browser.implicitly_wait(time_to_wait=5)

# '인쇄' 버튼 누르기
elem = browser.find_element_by_xpath('//*[@id="appoint"]/div[1]/span[3]/a').click()

# '인쇄하기' 버튼 누르기
print("1:", browser.title)
elem = browser.find_element_by_xpath('//*[@id="appoint"]/div[1]/span[3]/div/div/div/div[2]/div/p[2]/span/a').click()
browser.implicitly_wait(time_to_wait=5)

# 토지이용계획 - 이음 페이지로 이동
browser.switch_to.window(browser.window_handles[-1])
# driver.switch_to_window("토지이용계획 - 토지이음")
browser.implicitly_wait(time_to_wait=5)
print("title:", browser.title)



# 4.2 PDF 저장

#==========================================================

# frame 이동 : id = "sidebar"
# browser.switch_to_frame('sidebar')


# 대상
elem = Select(browser.find_element_by_xpath('/html/body/print-preview-app//print-preview-sidebar//div[2]/print-preview-destination-settings//print-preview-destination-select//print-preview-settings-section[1]/div/select'))
# /html/body/print-preview-app//print-preview-sidebar//div[2]/print-preview-destination-settings//print-preview-destination-select//print-preview-settings-section[1]/div/select/option[4]
elem.select_by_value("Save as PDF/local/")
browser.implicitly_wait(time_to_wait=5)

# 페이지
# elem = Select(browser.find_element_by_xpath('//*[@id="container"]/print-preview-pages-settings//print-preview-settings-section/div/select'))
# elem.select_by_value("0")
# browser.implicitly_wait(time_to_wait=5)

# # 레이아웃
# elem = Select(browser.find_element_by_xpath('//*[@id="container"]/print-preview-layout-settings//print-preview-settings-section/div/select'))
# elem.select_by_value("portrait")
# browser.implicitly_wait(time_to_wait=5)

# # 용지크기
# elem = Select(browser.find_element_by_xpath('//*[@id="moreSettings"]/print-preview-media-size-settings//print-preview-settings-section/div/print-preview-settings-select//select'))
# elem.select_by_value("A4")
# browser.implicitly_wait(time_to_wait=5)

# # 여백
# elem = Select(browser.find_element_by_xpath('//*[@id="moreSettings"]/print-preview-margins-settings//print-preview-settings-section/div/select'))
# elem.select_by_value("0")
# browser.implicitly_wait(time_to_wait=5)

# # 배율
# elem = Select(browser.find_element_by_xpath('//*[@id="moreSettings"]/print-preview-scaling-settings//print-preview-settings-section/div/select'))
# elem.select_by_value("0")
# browser.implicitly_wait(time_to_wait=5)

# # 머리글과 바닥글
# elem = browser.find_element_by_xpath('//*[@id="checkmark"]')
# if elem.is_selected() == False:
# elem.click()
# browser.implicitly_wait(time_to_wait=5)

# 저장
# elem = browser.find_element_by_xpath('//*[@id="sidebar"]//print-preview-button-strip//div/cr-button[1]')
# elem.click()
# browser.implicitly_wait(time_to_wait=5)



# K:\data\Desktop\PythonWorkspace\토지이용계획





# 4.3 열람 페이지로 돌아가기

#==========================================================

# 토지이용계획 - 이음 페이지 닫기
# browser.close()

# 토지이용계획열람 페이지로 돌아가기
# browser.switch_to.window(browser.window_handles[0])



# browser.quit()