# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/9 下午8:11
# @Author    :   fml
# @File      :   HomePage.py  
# @Software  :   PyCharm

import time
from selenium import webdriver
from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from utils.mySettings import customerManagerUrl


class HomePage(BasePage):
    customerManagerButton = (By.ID, u"serviceCardItem4")

    def __init__(self):
        super().__init__()

    def customerManagerButtonBox(self):
        return self.find_element(self.customerManagerButton)

class HomePageAction(HomePage):

    def gotoPage(self):
        time.sleep(1)
        self.customerManagerButtonBox().click()
        self.switch_to_page(customerManagerUrl)


if __name__ == '__main__':
    HomePageAction().gotoPage()