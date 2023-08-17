

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time, re, random, csv
from collections import namedtuple

def main(url_full):
        driver = webdriver.Chrome

driver.implicitly_wait(15)
driver.set_page_load_timeout(30)

# create HealthPlan namedtuple
HealthPlan = namedtuple("HealthPlan", ("State, County, FamType, Provider, PlanType,      Tier,") +
                            (" Premium, Deductible, OoPM, PrimaryCareVisitCoPay, ER, HospitalStay,") +
                            (" GenericRx, PreferredPrescription, RxOoPM, MedicalDeduct, BrandDrugDeduct"))

    # check whether the page has loaded and handle page load and time out errors
pageNotLoaded = bool(True)
while pageNotLoaded:
    try:
        driver.get(url_full)
        time.sleep(6 + abs(random.normalvariate(1.8, 3)))
    except TimeoutException:
        driver.quit()
        time.sleep(3 + abs(random.normalvariate(1.8, 3)))
        driver.get(url_full)
        time.sleep(6 + abs(random.normalvariate(1.8, 3)))
        # Handle page load error by testing presence of showAll,
        # an important feature of the page, which only appears if everything else loads

    try:
        driver.find_element_by_xpath('//*[@id="showAll"]').text
        # catch NoSuchElementException=>refresh page
    except NoSuchElementException:
        try:
        driver.refresh()

                # catch TimeoutException => quit and load the page
                # in a new instance of firefox,
                # I don't think the code ever gets here, because it freezes in the refresh
                # and will not throw the timeout exception like I would like
        except TimeoutException:
            driver.quit()
            time.sleep(3 + abs(random.normalvariate(1.8, 3)))
            driver.get(url_full)
            time.sleep(6 + abs(random.normalvariate(1.8, 3)))

    pageNotLoaded = False

    scrapePage()  # this is a dummy function, everything from here down works fine,