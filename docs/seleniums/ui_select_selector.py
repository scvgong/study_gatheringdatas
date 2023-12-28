# * 웹 크롤링 동작
from selenium import webdriver

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://getbootstrap.com/docs/5.3/examples/checkout/")

# - 정보 획득
from selenium.webdriver.common.by import By
# refer offica : https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select
from selenium.webdriver.support.ui import Select
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)

# 국가 selectbox 선택
selector_element = '#country'
element_country = browser.find_element(by=By.CSS_SELECTOR,value=selector_element)
Select(element_country).select_by_index(1)

# 주 selectbox 선택
selector_element = '#state'
element_state = browser.find_element(by=By.CSS_SELECTOR,value=selector_element)
Select(element_state).select_by_index(1)

pass

# 브라우저 종료
browser.quit()