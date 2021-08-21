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

class CustomerManagerAddOrder(CustomerManagerPageAction):

    def __init__(self):
        super().__init__()
    # 添加影集按钮
    add_order = (By.CSS_SELECTOR,"div[class^=style__pay_left]>.hljd-btn-primary:nth-child(2)")
    # """first_name"""
    first_name = (By.CSS_SELECTOR,"[id=\"name\"]")
    # """first_phone"""
    first_phone = (By.CSS_SELECTOR,"[id=\"phone\"]")
    # """couple_name"""
    couple_name = (By.CSS_SELECTOR,"[id=\"coupleName\"]")
    # """couple_phone"""
    couple_phone = (By.CSS_SELECTOR,"[id=\"couplePhone\"]")
    # """拍摄时间"""
    shoot_time = (By.CSS_SELECTOR,"#serviceDate")
    # """today_time"""
    today_time = (By.XPATH,"//div[@class=\"hljd-picker-footer\"]")
    # """点击确定，添加成功"""
    sure_btn = (By.CSS_SELECTOR,".hljd-modal-footer .hljd-btn-primary")

    def addOrderButton(self):
        """添加影集按钮"""
        return self.find_element(self.add_order)

    def firstNameInput(self):
        """第一联系人姓名"""
        return self.find_element(self.first_name)

    def firstPhoneInput(self):
        """第一联系人手机号"""
        return self.find_element(self.first_phone)

    def coupleNameInput(self):
        """第二联系人姓名"""
        return self.find_element(self.couple_name)

    def couplePhoneInput(self):
        """第二联系人手机号"""
        return self.find_element(self.couple_phone)

    def shootTimeDiv(self):
        """拍摄时间"""
        return self.find_element(self.shoot_time)

    def todayTimeDiv(self):
        """拍摄时间弹框中的今天按钮"""
        return self.find_element(self.today_time)

    def sureButton(self):
        """添加影集弹框中的确认弹框"""
        return self.find_element(self.sure_btn)

class CustomerManagerAddOrderAction(CustomerManagerAddOrder):

    def add_order_action(self,first_name,first_phone,couple_name,couple_phone):
        """
        点击添加按钮---输入第一联系人姓名手机号，输入第二联系人姓名手机号，输入拍摄时间，点击确认，创建成功
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
        time.sleep(0.5)
        self.mouse_left_click(self.todayTimeDiv())
        # self.todayTimeDiv().click()
        time.sleep(0.5)
        self.sureButton().click()

#在类中实例化动作类
#Python的import默认是单例模式；测试用例中可能有多个地方引用到它，在这里实例化并导入后，就可以保证这个实例是单一的
customerManagerAddOrderObj = CustomerManagerAddOrderAction()

if __name__ == '__main__':
    first_name = "自动"+str(random.randint(100,1000))
    first_phone = "1578888{}".format(random.randint(1000,9999))
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    print("current_time:",current_time)
    customerManagerAddOrderObj.gotoDeliverAlbumAction()
    customerManagerAddOrderObj.add_order_action(first_name,first_phone,"沐沐","17764505169")
