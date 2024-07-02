# GatheringData

## WebScrapings
* Web상에 존재하는 Contents를 수집하는 작업
* HTML 페이지를 가져와서 파싱하고 필요한 데이터만 확보

### 과정
* 불러옴 -> 선택사용 -> (저장)
* 대상 고려 순서 : id -> class -> Tag Name -> combine Tag and Something

## Selenuium
* 웹 브라우저를 자동화하기 위한 도구, 스크래핑하는데 적합
```
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://selenium.dev")
driver.quit()
```
