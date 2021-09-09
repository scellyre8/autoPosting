from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# li를 감싼 div 검색
tmNews = driver.find_element_by_id('today_main_news')

hdFlickItem = tmNews.find_element_by_class_name('hdline_flick_item')

# 썸네일 기사 
hdAtag = hdFlickItem.find_element_by_tag_name('a')
# 링크
hdHref = hdAtag.get_attribute('href')
hdImgTag = hdAtag.find_element_by_tag_name('img')

# 이미지
hdImaSrc = hdImgTag.get_attribute('src')
# 제목
hdTitle = hdImgTag.get_attribute('alt')
#hdTitle = hdAtag.get_attribute('alt')
print('썸네일 링크 : ', hdHref) 
print('썸네일 이미지 src : ', hdImaSrc)
print('썸네일 제목 : ', hdTitle)

result = []

# div 내에서 li 리스트 검색
tmNewsLis = tmNews.find_elements_by_tag_name('li')

# li는 여러개이므로 for문으로 루프
for li in tmNewsLis :
    aTag = li.find_element_by_tag_name('a')
    href = aTag.get_attribute('href')

    print('기사 제목 :', aTag.text)
    print('링크 : ', href)
    result.append(aTag.text)
    result.append(href)
    
result = [result[i:i+2] for i in range(0, len(result), 2)]

print('===================')
print(result)

driver.get('https://hellodoor.tistory.com/manage/post')
time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])
try:
    WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert = driver.switch_to.alert

    print(alert)
    alert.dismiss()
    
except:
    print('~')

title = driver.find_element_by_class_name('textarea_tit')
print(title)
print('1')
title.send_keys('asdfasdf')
title.send_keys(Keys.ENTER)
print(2)
contentBody = driver.find_element_by_id('tinymce')
contentBody.send_keys(hdTitle)


# print(tmNewsHead.text)
# driver.quit()
