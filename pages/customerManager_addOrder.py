# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/10 上午1:11
# @Author    :   fml
# @File      :   customerManager_addOrder.py  
# @Software  :   PyCharm

from selenium import webdriver
from pages.customerManagerPage import CustomerManagerPageAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.homePage import HomePageAction
import random
import datetime
import time

class customerManagerAddOrder(CustomerManagerPageAction):
    def __init__(self):
        super().__init__()

    add_order = (By.CSS_SELECTOR,".style__pay_left--uYB41>.hljd-btn-primary:nth-child(2)")
    #first_name
    first_name = (By.CSS_SELECTOR,"[id=\"name\"]")
    #first_phone
    first_phone = (By.CSS_SELECTOR,"[id=\"phone\"]")
    #couple_name
    couple_name = (By.CSS_SELECTOR,"[id=\"coupleName\"]")
    #couple_phone
    couple_phone = (By.CSS_SELECTOR,"[id=\"couplePhone\"]")
    #拍摄时间
    shoot_time = (By.CSS_SELECTOR,"#serviceDate")
    # today_time
    today_time = (By.XPATH,"//div[@class=\"hljd-picker-footer\"]")

    sure_btn = (By.CSS_SELECTOR,".hljd-modal-footer .hljd-btn-primary")

    def addOrderButton(self):
        return self.find_element(self.add_order)

    def firstNameInput(self):
        return self.find_element(self.first_name)

    def firstPhoneInput(self):
        return self.find_element(self.first_phone)

    def coupleNameInput(self):
        return self.find_element(self.couple_name)

    def couplePhoneInput(self):
        return self.find_element(self.couple_phone)

    def shootTimeDiv(self):
        return self.find_element(self.shoot_time)

    def todayTimeDiv(self):
        return self.find_element(self.today_time)

    def sureButton(self):
        return self.find_element(self.sure_btn)

class customerManagerAddOrderAction(customerManagerAddOrder):
    def add_order_action(self,first_name,first_phone,couple_name,couple_phone,shoot_time):
        """

        :param first_name:
        :param first_phone:
        :param couple_name:
        :param couple_phone:
        :param shoot_time:
        :return:
        """
        self.addOrderButton().click()
        time.sleep(1)
        self.firstNameInput().send_keys(first_name)
        self.firstPhoneInput().send_keys(first_phone)
        self.coupleNameInput().send_keys(couple_name)
        self.couplePhoneInput().send_keys(couple_phone)
        time.sleep(0.5)
        # self.mouse_left_click(self.shootTimeDiv())
        # self.shootTimeDiv().send_keys(shoot_time)
        self.shootTimeDiv().click()
        self.mouse_left_click(self.todayTimeDiv())
        # self.todayTimeDiv().click()
        time.sleep(0.5)
        self.sureButton().click()


if __name__ == '__main__':
    first_name = "ceshi"+str(random.randint(100,1000))
    first_phone = "1578888{}".format(random.randint(1000,9999))
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    print("current_time:",current_time)
    HomePageAction().gotoPage()
    CustomerManagerPageAction().gotoDeliverAlbum()
    customerManagerAddOrderAction().add_order_action(first_name,first_phone,"沐沐","17764505169",current_time)
