# * 웹 크롤링 동작
from selenium import webdriver

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://cafe.naver.com/peopledisc")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
# browser.find_element(by=By.CSS_SELECTOR,value="#menuLink84").click()
element_click = browser.find_element(by=By.CSS_SELECTOR,value="#menuLink84")
element_click.click()

# iframe 으로 전환
browser.switch_to.frame('cafe_main')

# main-area > div:nth-child(4) > table > tbody > tr
cafe_list = browser.find_elements(by=By.CSS_SELECTOR,value="#main-area > div:nth-child(4) > table > tbody > tr")
pass

# 브라우저 종료
browser.quit()