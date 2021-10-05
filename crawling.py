from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import tistoryReq

import chromedriver_autoinstaller
import time
import subprocess

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9999 --user-data-dir="C:\chrometmp"')
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1.:9999")
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

naverNewsUrl = 'https://news.naver.com/'
tistory = 'https://hellodoor.tistory.com/manage'

driver.get(naverNewsUrl)

tmNews = driver.find_element_by_id('today_main_news')
hdFlickItem = tmNews.find_element_by_class_name('hdline_flick_item')

# 썸네일 기사 
hdAtag = hdFlickItem.find_element_by_tag_name('a')

# 링크
hdHref = hdAtag.get_attribute('href')

# 이미지
hdImgTag = hdAtag.find_element_by_tag_name('img')
hdImgSrc = hdImgTag.get_attribute('src')

driver.get(hdHref)
time.sleep(1)

# 제목
driver.switch_to.window(driver.window_handles[-1])
thumTitHead = driver.find_element_by_class_name('tts_head')
hdTitle = thumTitHead.text

main = driver.find_element_by_id('articleBodyContents') # main content
articleContent = main.text

driver.back()
driver.switch_to.window(driver.window_handles[-1])

result = []
result.append(hdTitle)
result.append(hdHref)
result.append(hdImgSrc)
result.append(articleContent)

# li를 감싼 div 검색
tmNews = driver.find_element_by_id('today_main_news')
# div 내에서 li 리스트 검색
tmNewsLis = tmNews.find_elements_by_tag_name('li')

# li는 여러개이므로 for문으로 루프
#for li in range(1):
for li in range(len(tmNewsLis)) :
    tmNews = driver.find_element_by_id('today_main_news')
    tmNewsLis = tmNews.find_elements_by_tag_name('li')

    aTag = tmNewsLis[li].find_element_by_tag_name('a')
    href = aTag.get_attribute('href')

    print('기사 제목 :', aTag.text)
    print('링크 : ', href)
    result.append(aTag.text)
    result.append(href)

    driver.get(href)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    main = driver.find_element_by_id('articleBodyContents') # main content
    articleContent = main.text
    
    try:
        imgTag = main.find_element_by_tag_name('img')
        imgSrc = imgTag.get_attribute('src')
    except:
        imgSrc = ''
    print('이미지 :', imgSrc)
    result.append(imgSrc)
    articleContent = articleContent.replace('\n', "<br>")
    result.append(articleContent)
    
    driver.back()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    
result = [result[i:i+4] for i in range(0, len(result), 4)]
print(result)

driver.quit()

# 티스토리 api request 
tistoryReq.autoWrite(result)