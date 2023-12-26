# * 웹 크롤링 동작
from selenium import webdriver
import time

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/mJOVXR5/comments")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
        
# 한페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR,value="body")
previous_scrollHeight = 0

from pymongo import MongoClient 
mongoClient = MongoClient("mongodb://192.168.10.242:27017") # 연결

# database 연결, local로 접속
database = mongoClient["gatheringdatas"]

# collection 작업
collection = database["watcha_comments"]

# 스크롤 작업
while True:
   
    element_body.send_keys(Keys.END)
    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")

    if previous_scrollHeight >= current_scrollHeight:
        break
    else:
        previous_scrollHeight == current_scrollHeight 
        time.sleep(3)

    # 댓글 전체에 대한 내용정보
    selector_value = "div.css-13j4ly.egj9y8a4"
    element_movie_comment = browser.find_elements(by=By.CSS_SELECTOR,value=selector_value)

    for element_item in element_movie_comment:
        try:
            # 작성자 이름
            selector_name = "div.css-drz8qh.egj9y8a2 > a > div.css-eldyae.e10cf2lr1"
            element_name = element_item.find_element(by=By.CSS_SELECTOR,value=selector_name)
            name = element_name.text

            # 작성자 별점
            selector_grade = "div.css-jqudug.egj9y8a3 > div.css-31ods0.egj9y8a0 > span"
            element_grade = element_item.find_element(by=By.CSS_SELECTOR,value=selector_grade)
            grade = element_grade.text

            # 작성자 댓글
            selector_comment = "div.css-2occzs.egj9y8a1 > a > div > span"
            element_comment = element_item.find_element(by=By.CSS_SELECTOR,value=selector_comment)
            comment = element_comment.text
            pass
        except:
            pass
        finally:
            pass
        # print("작성자 : {}, 별점 : {}, 댓글 : {}".format(name,grade,comment))
        collection.insert_one({"user_name":name, "user_grade":grade, "user_comment":comment})
        pass
       
    
    pass      



# 브라우저 종료
browser.quit()

