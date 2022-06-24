# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/9 下午8:11
# @Author    :   fml
# @File      :   HomePage.py  
# @Software  :   PyCharm

import time
from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from utils.mySettings import customerManagerUrl


class HomePage(BasePage):

    def __init__(self):
        super().__init__()

    """确认按钮"""
    confirmButton = (By.CSS_SELECTOR, "div[class=\"hljd-modal-body\"]>img:first-child")
    """进入客户管理系统"""
    enterCustomerManagerButton = (
        By.CSS_SELECTOR, "div[class=\"MoreComponent_style_container__PXeut\"]>div:nth-child(2)")

    def confirmBox(self):
        """进入crm系统后的确认弹框"""
        return self.get_element(self.confirmButton, 10)

    def enterCustomerManagementBox(self):
        """进入客户管理系统页面"""
        return self.find_element(self.enterCustomerManagerButton)


class HomePageAction(HomePage):

    def gotoPage(self):
        self.confirmBox().click()
        time.sleep(1)
        self.enterCustomerManagementBox().click()
        self.switch_to_page(customerManagerUrl)

if __name__ == '__main__':
    HomePageAction().gotoPage()
