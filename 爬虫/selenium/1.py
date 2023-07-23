from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # options = webdriver.ChromeOptions()
    web = webdriver.Chrome()#创建浏览器对象
    web.get('https://lagou.com') #打开一个网址
    # print(web.title)
    #  窗口最大化
    # web.maximize_window()
    #找到某个元素，点击他
    # web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')该方法弃用
    el = web.find_element(By.XPATH,'//*[@id="changeCityBox"]/ul/li[2]/a') #通过xpath找到
    el.click()#点击事件
    time.sleep(2)#让浏览器缓一会，加载东西
    #找到输入框，输入python -> 回车/搜索按钮
    web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python',Keys.ENTER)
    #查找存放数据的位置，进行数据提取
    div_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
    for div in div_list:
        job_name = div.find_element(By.XPATH, './/div/div[1]/a').text
        job_price = div.find_element(By.XPATH, './/div/div[2]/span').text
        company = div.find_element(By.XPATH, './/div[@class ="company__2EsC8"]/div[1]/a').text
        print(job_price, job_name,company)

if __name__ == '__main__':
    main()







