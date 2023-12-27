# * 웹 크롤링 동작
from selenium import webdriver
import time

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 입력
browser.get("https://www.11st.co.kr/products/114830343?trTypeCd=22&trCtgrNo=895019")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)


# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 리뷰 클릭
element_click = browser.find_element(by=By.CSS_SELECTOR,value="#prdReview")
element_click.click()

#iframe으로 전환
browser.switch_to.frame('ifrmReview')

# #review-list-page-area 리뷰 리스트
selector_value = "#review-list-page-area > ul > li"
review_list = browser.find_elements(by=By.CSS_SELECTOR,value=selector_value)

# DB 업로드
from pymongo import MongoClient 
mongoClient = MongoClient("mongodb://192.168.10.242:27017") # 연결

# database 연결, local로 접속
database = mongoClient["gatheringdatas"]

# collection 작업
collection = database["11st_comments"]


# 특정 조건 불러오기
for element_item in review_list:
    
    try:
        # 작성자 dt.name
        selector_name = "li > dl > dt.name"
        element_name = element_item.find_element(by=By.CSS_SELECTOR,value=selector_name)
        name = element_name.text

        # 선택옵션 div.option
        selector_option = "div.option > dd"
        element_option = element_item.find_element(by=By.CSS_SELECTOR,value=selector_option)
        option = element_option.text

        # 별점 p.grade
        selector_grade = "p.grade > span > em"
        element_grade = element_item.find_element(by=By.CSS_SELECTOR,value=selector_grade)
        grade = element_grade.text

        # 내용정보 #review-list-page-area > ul:nth-child(1) > li:nth-child(1) > div > div / 내용더보기 "p.cont_btn.review-expand > button.c_product_btn.c_product_btn_more6.review-expand-open-text"
        selector_comment = "div > div.cont_text_wrap > p" 
        element_comment = element_item.find_element(by=By.CSS_SELECTOR,value=selector_comment)
        # browser.find_element(by=By.CSS_SELECTOR,value="p.cont_btn.review-expand > button.c_product_btn.c_product_btn_more6.review-expand-open-text").click()
        comment = element_comment.text


        pass
    except:
        pass
    finally:
        pass
    
    time.sleep(3)
    # print("{},{},{},{}".format(name,option,grade,comment))        
    collection.insert_one({"user_name":name, "user_option":option,"user_grade":grade,"user_comment":comment})
    pass

# 브라우저 종료
browser.quit()