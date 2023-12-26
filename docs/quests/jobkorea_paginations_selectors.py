from selenium import webdriver
import time 
# - chrome browser 열기


# from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# - 주소 https://www.coupang.com/np/campaigns/348?page=1 입력

chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

browser = webdriver.Chrome(options=chrome_options)

for page_number in range(1,10):
    url = "https://www.coupang.com/np/campaigns/348?page={}".format(page_number)
    browser.get(url)
    time.sleep(3)
    pass