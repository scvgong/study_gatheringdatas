from selenium import webdriver
from selenium.webdriver.common.by import By

# - chrome browser 열기
browser = webdriver.Chrome()

browser.get("https://www.coupang.com/np/categories/510541")

selector_value = "div.name"
element_path = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)

for webelement in element_path:
    title = webelement.text
    print("{}".format(title))
    pass
pass


# [에이메카] 270LEDPM 광시야각 리얼 100 HDR * 전국 출장 A/S 지원 *
# [비트엠] Newsync B24Q IPS 프리싱크 HDR [무결점]
# 한성컴퓨터 1500R 커브드 게이밍 리얼 75 모니터, 68.58cm, TFG27F07V(일반)
# 큐닉스 그룹 68.5cm FHD 오피스 모니터, QX27SD REAL 75 HDR(무결점)
# LG 32MB25VQ 32LF550B 32LB627B 32LX530H 6916l-1974A 1975A 호환용 백라이트
# 비트엠 68cm Newsync H2775F 오피스 27인치모니터, H2775F(무결점)
# PQONE 카플레이 모니터 10.26인치 오토 안드로이드 애플 무선 블루투스 블랙박스 후방카메라, PQONE모니터+64GB SD카드
# 한성컴퓨터 60.4cm FHD 평면 240 게이밍 모니터, TFG24F24T(무결점)
# LG전자 룸앤TV, 68.6cm, 27LQ600SW
# 한성컴퓨터 68.6cm FHD 1500R 리얼 165 게이밍 모니터, TFG27F16V(일반)
# [쿨러마스터] GA241 VA FHD 100 게이밍 [무결점]
# 샤오미 미지아 모니터 LED 라이트 스크린바 2세대 1S MJGJD02YL, 스크린바 1 (1세대)
# 한성컴퓨터 73cm WFHD IPS 울트라와이드 모니터, TFG29F07WP(일반)
# 한성컴퓨터 60.4cm FHD 리얼 165 게이밍 모니터, ULTRON 2460G PLUS(일반)
# 한성컴퓨터 60.4cm FHD 리얼 165 게이밍 모니터, ULTRON 2460G PLUS(무결점)
# 어드밴스원 68.58cm 커브드 보더리스 게이밍모니터, M270CG75H
# 한성컴퓨터 68.6cm FHD 리얼 144 게이밍 모니터, ULTRON 2760G PLUS(무결점)
# 한성컴퓨터 68cm QHD 평면 144 게이밍 모니터, TFG27Q14F
# 한성컴퓨터 68.5cm FHD 프리싱크 리얼 75 모니터, ULTRON 2758 PLUS(일반)
# MSI 24인치 게이밍모니터 옵틱스 G243 게이밍 165 아이세이버 무결점 / sy, G243(무결점)
# 한성컴퓨터 68.6cm FHD 리얼 144 게이밍 모니터, ULTRON 2760G PLUS(일반)
# 한성컴퓨터 80.1cm FHD 리얼 165 게이밍 모니터, TFG32F16V(일반)
# [쿠팡수입] 제우스랩 39.6cm 1080P IPS 휴대용 모니터, P15A
# 인터픽셀 80.01cm QHD IPS 75Hz 평면 모니터 화이트 에디션, IPQ3220(일반)
# [신규론칭 리뉴얼 450정 증량]방풍통성산 최대량 6000mg 배합 450정 복부지방집중관리 / 다이어트 / 복부지방 /체내 불순물 제거, 로켓직구
# 한성컴퓨터 1500R 커브드 게이밍 리얼 100 모니터, 86.4cm, TFG34Q10W(일반)
# 한성컴퓨터 80.1cm QHD 모니터, ULTRON 3278 QHD(일반)
# 제우스랩 ZEUSLAP Z16P 휴대용 스크린 서브 보조 모니터 16인치 2.5K 블랙
# 한성컴퓨터 1200R 커브드 게이밍 리얼 144 모니터, 59.9cm, TFG24F14V(일반)
# MSI 61cm FHD IPS 170Hz 무결점 게이밍 모니터, G244F
# 한성컴퓨터 1500R 커브드 게이밍 리얼 75 모니터, 68.58cm, TFG27F07V(무결점)
# 픽셀아트 PIXELART PA2718W 화이트 180Hz FHD IPS 27형 모니터 일반
# 한성컴퓨터 60.4cm FHD 프리싱크 리얼75 모니터, ULTRON 2435V PLUS(일반)
# LG전자 60.4cm FHD 모니터, 24MQ400C
# 한성컴퓨터 81cm FHD 평면 144 게이밍 모니터, TFG32F14F(일반)
# 한성컴퓨터 86.4cm WQHD 1500R 커브드 리얼 144 울트라와이드 게이밍 모니터, TFG34Q14W 1500R(무결점)
# 어드밴스원 68.58cm FHD 커브드 보더리스 165HZ 게이밍 모니터, M270CG165(무결점)
# LG전자 68.6cm FHD 모니터, 27MQ400C
# 빅트랙 40.89cm FHD IPS 144Hz 휴대용 모니터, 161PM01
# 디엑스 61cm FHD 모니터 LG ips 패널 컴퓨터 사무용 DX241HDMI, DX241HDMI(무결점)
# 큐닉스 큐닉스그룹 60.4cm FHD 모니터, QX24SD REAL 75 HDR(일반)
# 한성컴퓨터 80.1cm FHD 1500R 리얼 240 게이밍 커브드 모니터, TFG32F24V(무결점)
# 카멜 80cm QHD 1500R 게이밍 커브드 모니터 CM3220GQC 165Hz
# 한성컴퓨터 80.1cm FHD 리얼 165 게이밍 모니터, TFG32F16V(무결점)
# 일본직배송 카배진 카베진 300정 3병 총 900정 세트
# LG전자 PC모니터, 60.4cm, 24BK550YW
# 한성컴퓨터 80.1cm WQHD 모니터, ULTRON 3278 QHD(무결점)
# 인터픽셀 60.5cm FHD 평면 75Hz IPS 피벗 게이밍 모니터, IP2420(무결점)
# MSI MP161 아이에르고 포터블 모니터 무결점 / IPS / FHD / 15.6인치
# 한성컴퓨터 80.01cm QHD 평면 모니터, TFG32Q07P(일반)
# 벤큐 69cm FHD 아이케어 모니터, GW2780
# LG전자 울트라와이드 모니터, 73cm, 29WP500
# Newsync B2415C 커브드 모니터, 선택없음, 1
# 일본 [다이이치산쿄] 트랑 화이트 C 클리어 120정, 1cm
# 일본 쇼콜라BB plus 250정 정품 직구, 1cm
# [고바야시] 나이시토루Z 315정, 일본, 1cm
# 일본 [다이쇼] 파부롱S 골드 W미립 24포, 1cm
# 오타이산 일본 소화제 48포 1개 정품 직구, 1cm
# (해외직구) 효과up! 다이어트~ 나이시토루Z [420정] 정품 직구, 일본, 1cm
# 변비엔 코락쿠 350정 정품 직구, 일본, 1cm