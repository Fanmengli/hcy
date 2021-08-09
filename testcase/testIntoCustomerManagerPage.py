# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/9 下午8:35
# @Author    :   fml
# @File      :   testIntoCustomerManagerPage.py  
# @Software  :   PyCharm

from selenium import webdriver
from pages.homePage import HomePageAction
from pages.customerManagerPage import CustomerManagerPageAction

class TestIntoCustomerManagerPage:
    HomePageAction().gotoPage()
    CustomerManagerPageAction().gotoDeliverAlbum()
