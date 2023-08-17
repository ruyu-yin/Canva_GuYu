from selenium.webdriver.common.by import By

from utils.browserpage import BasePage


class Navigationpage(BasePage):
    def go_to_homepage(self):
        self.click(By.LINK_TEXT,"首页")