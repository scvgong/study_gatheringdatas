# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from pymongo import MongoClient 
mongoClient = MongoClient("mongodb://192.168.10.242:27017") # 연결

# database 연결, local로 접속
database = mongoClient["gatheringdatas"]

# collection 작업
collection = database["court"]

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/)
browser.get("https://www.courtauction.go.kr/")

# iframe 으로 전환
browser.switch_to.frame('indexFrame')

from selenium.webdriver.common.by import By
# click menu : #menu > h1:nth-child(5) > a > img
browser.find_element(by=By.CSS_SELECTOR, value="#menu > h1:nth-child(5) > a > img").click()

from selenium.webdriver.support.ui import Select
# 법원/소재지 리스트 : #idJiwonNm > option
element_courts = browser.find_elements(by=By.CSS_SELECTOR, value="#idJiwonNm > option")
for index in range(len(element_courts)) :
        
    if index < 60:
        select_value = "#idJiwonNm"
        select_court = Select(browser.find_element(by=By.CSS_SELECTOR, value=select_value)) 
        select_court.select_by_index(index)
    else:
        break

    element_court = browser.find_element(by=By.CSS_SELECTOR, value="#idJiwonNm > option:nth-child({})".format(index+1))
    court = element_court.text

    # 검색 클릭 : #contents > form > div.tbl_btn > a:nth-child(1) > img
    url = "#contents > form > div.tbl_btn > a:nth-child(1) > img"
    browser.find_element(by=By.CSS_SELECTOR, value=url).click()
    time.sleep(1)

    # 상세검색 전체 #contents > div.table_contents > form:nth-child(1) > table > tbody
    selector_element = "#contents > div.table_contents > form:nth-child(1) > table > tbody > tr"
    element_infor = browser.find_elements(by=By.CSS_SELECTOR,value=selector_element)

    for x in range(1, len(element_infor)):
        # 사건번호 #contents > div.table_contents > form:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2)
        select_casenum = "#contents > div.table_contents > form:nth-child(1) > table > tbody > tr:nth-child({}) > td:nth-child(2)".format(x)
        element_casenum = browser.find_element(by=By.CSS_SELECTOR,value=select_casenum)
        casenum = element_casenum.text

        # 소재지 및 내역 #contents > div.table_contents > form:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(4)
        select_location = "#contents > div.table_contents > form:nth-child(1) > table > tbody > tr:nth-child({}) > td:nth-child(4)".format(x)
        element_location = browser.find_element(by=By.CSS_SELECTOR,value=select_location)
        location = element_location.text

        # print("{},{},{}".format(court,casenum,location))
        collection.insert_one({"court":court,"casenum":casenum,"location":location})
        pass

    # 이전 화면 : #contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img
    url = "#contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img"
    browser.find_element(by=By.CSS_SELECTOR, value=url).click()
    time.sleep(3)
    pass
pass

# 브라우저 종료
browser.quit()