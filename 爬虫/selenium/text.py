from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def main():
    #遇到iframe如何处理
    web = webdriver.Chrome()#创建浏览器对象
    web.get('') #打开一个网址
    iframe = web.find_element()#定位找到iframe
    web.switch_to.frame(iframe)#切换到iframe
    tx = web.find_element().text #在iframe里面进行数据提取
    #切换回原页面
    web.switch_to.default_content()



if __name__ == '__main__':
    main()