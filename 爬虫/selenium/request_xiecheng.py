import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
下载浏览器驱动程序路径
https://chromedriver.storage.googleapis.com/index.html
查看驱动器与浏览器版本的映射关系
http://blog.csdn.net/huilan_same/article/details/51896672
#最新
https://sites.google.com/chromium.org/driver/?pli=1
'''


def page_select_function():
    # driver_path = r'C:\Users\X3\Desktop\chromedriver_win32\chromedriver.exe'
    options = webdriver.ChromeOptions()
    bro = webdriver.Chrome(options=options)
    bro.get('https://www.ctrip.com/') #访问携程网站
    time.sleep(1)
    # # 窗口最大化
    # bro.maximize_window()
    # 从首页选择进入机票页面定位标签
    # flight_btn = bro.find_element(By.XPATH, "//button[@aria-label='机票 按回车键打开菜单']")
    flight_btn = WebDriverWait(bro, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='机票 按回车键打开菜单']"))
    )
    # print(flight_btn.is_enabled())
    flight_btn.click()
    # 单程
    button = WebDriverWait(bro, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME,"active"))
    )
    # button = bro.find_element(By.CLASS_NAME,"active")
    print(button.is_enabled())
    button.click()
    # 找到日期选择框元素
    date_input = bro.find_element(By.CLASS_NAME,"date-components")
    date_input.click()
    time.sleep(1)
    # 选择出发城市
    # 找到地点输入框元素
    location_input = bro.find_element(By.CLASS_NAME,"form-input-v3")
    location_input.clear()
    location_input.send_keys("北京")
    time.sleep(1)
    print('____________________')
    #选择到达城市
    destination_input = bro.find_element(By.CSS_SELECTOR,'input[name="owACity"]')
    destination_input.clear()
    destination_input.send_keys("重庆")
    time.sleep(1)
    # 开始搜索
    input_tag_search = bro.find_element(By.CLASS_NAME,'search-btn')
    input_tag_search.click()
    time.sleep(3)

    # 只选择直飞
    button = bro.find_element(By.XPATH, '//span[contains(text(), "直飞")]')
    button.click()
    time.sleep(2)
    for i in range(1):
        bro.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    return bro
def data_acquistion(bro):
    source = bro.page_source
    bs = BeautifulSoup(source, 'html.parser')
    divs = bs.find_all('div', class_='flight-item domestic')##
    return divs
def data_treating(divs):
    for div in divs:
        try:
            airlineName = div.find('div', class_='airline-name').get_text()
            flightNumber = div.find_all('span', class_='plane-No')[0].get_text()
            # craftTypeName = div.find('span', class_='direction_black_border low_text').string
            departureTime = div.find('div', class_='depart-box').find('div', class_='time').string
            arrivalTime = div.find('div', class_='arrive-box').find('div', class_='time').get_text()
            lowestPrice = div.find('span', class_='price').get_text()
            print(airlineName, '\t', flightNumber, '\t', departureTime, '\t', arrivalTime, '\t', lowestPrice)
        except:
            print('无该信息')
def main():
    driver = page_select_function()
    divs = data_acquistion(driver)
    data_treating(divs)
    driver.quit()

if __name__ == '__main__':
    main()