# * 웹 크롤링 동작
from selenium import webdriver

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

## 하나의 elements 가져오기
# selector_value = "#ty_thmb_view > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit"
# element_path = browser.find_element(by=By.CSS_SELECTOR, value = selector_value)
# # browser.find_element(by=By.CSS_SELECTOR, value = selector_value)
# # get text in tag
# element_path.text
# '반려견패드(중)40*50cm*100매'
pass

## 여러개 elements 정보 가져오기
selector_value = "span.mnemitem_goods_tit"
element_path = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)
type(element_path)
# <class 'list'>
type(element_path[0])
# <class 'selenium.webdriver.remote.webelement.WebElement'>
element_path[0].text
#'시리우스 펫퓸 반려견 러블리플라워 샴푸 500ML'
element_path[1].text
#'시리우스 펫퓸 반려견 드라이풋샴푸 270ML'
for webelement in element_path:
    title = webelement.text
    print("{}".format(title))
    pass
pass


# 브라우저 종료
browser.quit()

