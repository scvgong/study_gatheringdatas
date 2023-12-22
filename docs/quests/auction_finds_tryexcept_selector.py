# * 웹 크롤링 동작
from selenium import webdriver

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033 입력
browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")

# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
# 상품 제목
selector_value = "div > div.info"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)

for element_item in element_bundle:
    # 상품 제목
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value="div.info > em > a")
    title = element_title.text
    try:
        # 판매 원가
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="span > strike > span")
        old_price = element_old_price.text

        # 변경 가격
        element_new_price = element_item.find_element(by=By.CSS_SELECTOR, value="li.d_price > span.sale > span")
        new_price = element_new_price.text

        # 배송 방법(3가지)
        element_delivery = element_item.find_element(by=By.CSS_SELECTOR, value="div.icon > div")
        delivery = element_delivery.text.split()

        pass
    except:
        old_price = ""
        new_price = ""
        delivery = ""
        pass
    finally:
        pass
    print("상품 제목 : {}, 판매원가 : {}, 변경가격 : {}, 배송 : {}".format(title,old_price,new_price,delivery))
    pass