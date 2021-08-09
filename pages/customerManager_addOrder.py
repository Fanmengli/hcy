# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/10 上午1:11
# @Author    :   fml
# @File      :   customerManager_addOrder.py  
# @Software  :   PyCharm

from selenium import webdriver
from pages.customerManagerPage import CustomerManagerPageAction
from selenium.webdriver.common.by import By
import time

class customerManagerAddOrder(CustomerManagerPageAction):
    def __init__(self):
        super().__init__()

    add_order = (By.CSS_SELECTOR,".style__pay_left--uYB41>.hljd-btn-primary:nth-child(2)")
    #first_name
    first_name = (By.CSS_SELECTOR,"input[id=\"name\"]")
    #first_phone
    first_phone = (By.CSS_SELECTOR,"[id=\"phone\"]")

    def addOrderButton(self):
        return self.find_element(self.add_order)

    def firstNameInput(self):
        return self.find_element(self.first_name)

    def firstPhoneInput(self):
        return self.find_element(self.first_phone)

class customerManagerAddOrderAction(customerManagerAddOrder):
    def add_order(self,first_name,first_phone):
        self.addOrderButton().click()
        time.sleep(1)
        self.firstNameInput().send_keys(first_name)
        self.firstPhoneInput().send_keys(first_phone)
