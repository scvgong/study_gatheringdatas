# * 웹 크롤링 동작
from selenium import webdriver
import time

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 입력
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=12#pageNum%%13"
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By

element_item = browser.find_elements(by=By.CSS_SELECTOR,value="li > div.box_pd.ranking_pd")

def items(browser):
    
    #상품 명칭
    selector_title = "div.c_product_info_title.appleshop_type.c_product_info_title_coupon > h1"
    element_title = browser.find_element(by=By.CSS_SELECTOR,value=selector_title)
    title = element_title.text

    #imagelink
    selector_image = "div.img_full.img_full_height"
    element_image = browser.find_element(by=By.CSS_SELECTOR,value=selector_image)
    image = element_image.text

    #원가
    selector_old_price = "div.b_product_info_price.b_product_info_price_style3 > div > div > dl > div:nth-child(1) > dd"
    element_old_price = browser.find_element(by=By.CSS_SELECTOR,value=selector_old_price)
    old_price = element_old_price.text

    #판매가
    selector_price = "div:nth-child(2) > dd.price > strong"
    element_price = browser.find_element(by=By.CSS_SELECTOR,value=selector_price)
    price = element_price.text

    #상품정보
    selector_infor = "#tabpanelDetail4 > div > table:nth-child(10)"
    element_infor = browser.find_element(by=By.CSS_SELECTOR,value=selector_infor)
    infor = element_infor.text

    list_browser = [title,image,old_price,price,infor]

    return list_browser


# item_list = ["a.prd_4725982710","a.prd_5070943536","a.prd_4142962611","a.prd_4907624417"]


# 상품으로 들어가기
element_item_one = browser.find_element(by=By.CSS_SELECTOR,value="a.prd_4725982710")   
element_item_one.click()
time.sleep(2)  # 화면 완성 term
list_item = items(browser)

print("{}".format(list_item))

browser.back() # 제품 리스트로 이동
time.sleep(2)  # 화면 완성 term

element_item_two = browser.find_element(by=By.CSS_SELECTOR,value="a.prd_5070943536")   
element_item_two.click()
time.sleep(2)  # 화면 완성 term
list_item = items(browser)

print("{}".format(list_item))

browser.back() # 제품 리스트로 이동
time.sleep(2)  # 화면 완성 term

element_item_third = browser.find_element(by=By.CSS_SELECTOR,value="a.prd_6280495982")   
element_item_third.click()
time.sleep(2)  # 화면 완성 term
list_item = items(browser)

print("{}".format(list_item))

browser.back() # 제품 리스트로 이동
time.sleep(2)  # 화면 완성 term

element_item_four = browser.find_element(by=By.CSS_SELECTOR,value="a.prd_4907624417")   
element_item_four.click()
time.sleep(2)  # 화면 완성 term
list_item = items(browser)

print("{}".format(list_item))

browser.back() # 제품 리스트로 이동
time.sleep(2)  # 화면 완성 term

pass


# 브라우저 종료
browser.quit()