# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/10 上午1:10
# @Author    :   fml
# @File      :   testCustomerManagerAddOrder.py  
# @Software  :   PyCharm
from datetime import datetime
from random import random


from selenium import webdriver
from pages.customerManager_addOrder import customerManagerAddOrderAction
from pages.customerManagerPage import CustomerManagerPageAction
from pages.homePage import HomePageAction

class TestCustomerManagerAddOrder(customerManagerAddOrderAction):
    first_name = "ceshi" + str(random.randint(100, 1000))
    first_phone = "1578888{}".format(random.randint(1000, 9999))
    current_time = datetime.datetime.now().strftime('%Y-%m-%dd')
    print("current_time:", current_time)
    HomePageAction().gotoPage()
    CustomerManagerPageAction().gotoDeliverAlbum()
    customerManagerAddOrderAction().add_order_action(first_name, first_phone, "沐沐", "17764505169", current_time)