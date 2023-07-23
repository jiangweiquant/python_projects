from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # options = webdriver.ChromeOptions()
    web = webdriver.Chrome()  # 创建浏览器对象
    web.get('https://lagou.com')  # 打开一个网址
    el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[2]/a')  # 通过xpath找到
    el.click()  # 点击事件
    time.sleep(2)  # 让浏览器缓一会，加载东西
    # 找到输入框，输入python -> 回车/搜索按钮
    web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys('python', Keys.ENTER)

    web.find_element(By.XPATH,
                     '/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/span/div/div[1]/a').click()
    time.sleep(10)
    # 进入到了新窗口，如何在新窗口进行数据提取[在selenium中，新窗口默认是不切换过来的]#现在python版本自动切换
    web.switch_to.window(web.window_handles[-1])
    # 在新窗口提取数据
    job_detail = web.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/dl[1]/dd[2]/div').text
    print(job_detail)
    # 关掉子窗口，变更窗口回到原窗口
    web.close()
    web.switch_to.window(web.window_handles[0])
    # 验证切回去了
    print(web.find_element(By.XPATH,
                           '/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/span/div/div[1]/a').text)


if __name__ == '__main__':
    main()