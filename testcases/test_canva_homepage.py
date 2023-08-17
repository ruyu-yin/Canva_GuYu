from pageobjectcanva.designlibrary import YourDesign
from pageobjectcanva.homepageobj import Homepage
from pageobjectcanva.navigationobj import Navigationpage


def test_open_homepage(login):
   pass

def test_startdesign():
   Homepage().startdesign()

def test_login():
   # Homepage().login()
   Homepage().confirm_law()


def test_signup():
   Homepage().signup()
   Homepage().confirm_law()

def test_goback_homepage():
   Homepage().startdesign()
   Navigationpage().go_to_homepage()