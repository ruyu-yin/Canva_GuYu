from selenium.webdriver.common.by import By
import pytest
from utils.browserpage import BasePage


class CheckCatalogCreate(BasePage):
    """everything is ok, machine status,count, every tab is ok"""
    def get_cataloglife(self):
        catalogstatus_ = []
        actualvalue = BasePage().driver.page_source
        cataloglife = {"CreateCatalogFailed","Now provisioning...","Now copying the master image...","Now creating Citrix server VMs...","Now deleting Citrix server VMs...","New catalog is ready","Catalog creation is taking longer than expected. Please wait"}
        for createstep in cataloglife:
            try:
                assert createstep in actualvalue
                if createstep in actualvalue:
                    cataogstatus_= catalogstatus_.append(createstep)
                    print(catalogstatus_)
                break
            except KeyError as e:
                return cataloglife


    def get_catalogstatus(self,catalogname=None):
        cmdcatalogready = "New catalog is ready!"
        iconwarning = self.find(By.XPATH,"//div[class='status-icon xdicon-warning']")
        icontick = self.find(By.XPATH,"//div[class='status-icon xdicon-warning']")
        cataloglist = self.driver.page_source
        assert catalogname in cataloglist
        if iconwarning in cataloglist:
            print("catalog is created successfully")
        elif icontick in cataloglist:
            print ("catalog is active and users is added successfully")
        else:
            print("catalog create failed, error message is in the logxxxx")
            self.getlogall()
    def newcatalog_addsubscribers(self):
        self.click(By.ID,"daasDashboardAddSubscribers")
        self.click(By.ID,"daasCatalogSubscribersManage")
        # self.click(By.XPATH, "//a[@class='ng-star-inserted tab-active'][contains(.,'Subscribers')]")

    def get_machine_count(self,machinecount):
        if machinecount != 10 :
            pass

        elif machinecount == 10 :
            pass

        elif machinecount <= 10:
            pass
        elif machinecount >= 10:
            pass
        elif machinecount >= 3:
            pass

        else:
            pass
    def get_machine_power(self):
        pass

    def get_machine_registration(self):
        pass
