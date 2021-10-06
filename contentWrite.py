from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pyautogui
import pyperclip

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

def editPosting(data):

    tistory = f'https://hellodoor.tistory.com/manage/newpost/{data[0]}?type=post&returnURL=https%3A%2F%2Fhellodoor.tistory.com%2Fmanage%2Fposts'
    driver.get(tistory)
    time.sleep(2)

    mceu_20 = driver.find_element_by_id('mceu_20-open')
    mceu_20.click()
    time.sleep(0.5)

    mceu_38 = driver.find_element_by_id('mceu_34')
    mceu_38.click()

    js_tmp = """
        javascript:(function() {
            function l(u, i){
                var d = document;
                if(!d.getElementById(i)) {
                    var s = d.createElement('script');
                    s.src = u;
                    s.id = i;
                    d.body.appendChild(s);
                }
            }
            l('//code.jquery.com/jquery-3.2.1.min.js', 'jquery')
        })();
    """
    driver.execute_script(js_tmp)

    position = pyautogui.position()

    print(pyautogui.size())
    print(position.x)
    print(position.y)

    pyautogui.moveTo(-1495, 331)
    pyautogui.click()

    print(data[1])

    pyperclip.copy(data[1])
    pyautogui.hotkey('ctrl', 'v')
    
    # pyautogui.write(data[1])

    btn_default = driver.find_element_by_class_name('btn-default')
    btn_default.click()

    foot = driver.find_element_by_class_name('layer_foot')
    btns = foot.find_elements_by_tag_name('button')
    for btn in btns:
        btn_type = btn.get_attribute('type')

        if btn_type == 'submit':
            btn.click()
            print(btn_type)
    
    driver.quit()