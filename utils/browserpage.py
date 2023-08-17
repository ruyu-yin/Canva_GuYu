
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import os.path
import logging
from logging import Logger



class BasePage():
    def __init__(self):
        self.chromeoptions = Options()
        self.chromeoptions.add_argument("start-maximized")
        self.chromeoptions.debugger_address = "127.0.0.1:8201"
        self.driver = webdriver.Chrome(options=self.chromeoptions)

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def  getlogall(self):
        catalogcreationlog = Logger().error("create catalog failed")
        imagebuildlog = Logger().error("Build image failed")
        imageimportlog = Logger().error("Import image failed")
        connectioncreatelog= Logger().error("Creating peer Vnet failed")
        catalogcreationlogactive=Logger().info("catalog create successfully")

    def quit_browser(self):
         self.driver.quit()

    def forward(self):               # 浏览器前进操作
        self.driver.forward()
        logging.info("Click forward on current page.")

    def back(self):                        # 浏览器后退操作
        self.driver.back()
        logging.info("Click back on current page.")

    def find(self, by, locator):               # 定位元素方法
        return self.driver.find_element(by, locator)

    def click(self, by,locator):  # 点击元素
        el = self.find(by,locator)
        try:
            el.click()
            print("no error")
            #logging.info("The element \'%s\' was clicked." % el.text)
        except NameError as e:
            print("error")
            #logging.error("Failed to click the element with %s" % e)

    def send_keys(self, by,locator, text):
        el = self.find(by,locator)
        el.clear()
        try:
            el.send_keys(text)
            logging.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logging.error("Failed to select in input box with %s" % e)
            self.get_windows_img()

    def wait(self, seconds,by,locator):         # 显示等待
        try:
            wait_ = WebDriverWait(self.driver, seconds,0.5)
            element_ = wait_.until(
                EC.presence_of_element_located((by, locator)),message="TimeOut")
            #wait_.until(lambda driver: driver.find_element(*loc))
            #logging.info("wait for %d seconds." % seconds)
        except NameError as e:
            print("error")
            #logging.error("Failed to load the element with %s" % e)

    def get_windows_image(self):                # 保存图片 #把file_path保存到我们项目根目录的一个文件夹.\Screenshots下
        file_path = os.path.dirname(os.path.abspath("..") + "/screenshots/")
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.get_windows_image()
            logging.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logging.error("Failed to take screenshot! %s" % e)
            self.get_windows_image()

    def clear(self, by,locator):           # 清除文本框
        el = self.find(by,locator)
        try:
            el.clear()
            logging.info("Clear text in input box before typing.")
        except NameError as e:
            logging.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    def move_element(self, by,locator, sloc):   # 鼠标事件（左键点击）
        mouse = self.find(by,locator)
        try:
            ActionChains(self.driver).move_to_element(mouse).perform()
            self.click(sloc)
            pass
        except Exception as e:
            logging.error("Failed to click move_element with %s" % e)
            self.get_windows_img()



    @staticmethod
    def sleep(seconds):          # 强制等待
        time.sleep(seconds)
        logging.info("Sleep for %d seconds" % seconds)



