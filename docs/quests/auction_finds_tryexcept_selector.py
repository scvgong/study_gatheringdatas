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
# 상품 전체
selector_value = "div > div.info"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)

for element_item in element_bundle:
    
    try:
        # 상품 제목
        selector_title = "div.info > em > a"
        element_title = element_item.find_element(by=By.CSS_SELECTOR, value=selector_title)
        title = element_title.text

        # 판매 원가
        selector_old_price = "span > strike > span"
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value=selector_old_price)
        old_price = element_old_price.text

        # 변경 가격
        selector_new_price = "li.d_price > span.sale > span"
        element_new_price = element_item.find_element(by=By.CSS_SELECTOR, value=selector_new_price)
        new_price = element_new_price.text

        # 배송 방법(3가지)
        selector_delivery = "div.icon > div"
        element_delivery = element_item.find_element(by=By.CSS_SELECTOR, value=selector_delivery)
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