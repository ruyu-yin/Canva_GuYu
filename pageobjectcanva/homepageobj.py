from selenium.webdriver.common.by import By
from utils.browserpage import BasePage


class Homepage(BasePage):
    def startdesign(self):
        self.click(By.XPATH,"//*[@class='_38oWvQ'][contains(.,'开始设计')]")

    def login(self):
        self.click(By.XPATH,"//button[@class='_1QoxDw Qkd66A tYI0Vw o4TrkA NT2yCg Qkd66A tYI0Vw lsXp_w cwOZMg zQlusQ uRvRjQ']")

    def signup(self):
        self.click(By.XPATH,"//button[@class='_1QoxDw Qkd66A tYI0Vw o4TrkA zKTE_w Qkd66A tYI0Vw lsXp_w cwOZMg zQlusQ uRvRjQ']")

    def confirm_law(self):
        self.click(By.XPATH,"//div[@class='ZJon7Q _rklkw']")

