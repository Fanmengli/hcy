# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/9 下午8:24
# @Author    :   fml
# @File      :   firstPage.py  
# @Software  :   PyCharm
import time

from selenium import webdriver
from pages.homePage import HomePageAction
from selenium.webdriver.common.by import By

class CustomerManagerPage(HomePageAction):
    def __init__(self):
        super().__init__()

    confirmButton = (By.CLASS_NAME,"hljd-btn")
    #交付按钮
    deliverButton = (By.XPATH,"//ul[@role=\"menu\"]/li[7]")
    #影集交付按钮
    deliverAlbumButton = (By.CSS_SELECTOR,"a[href=\"#/deliver/album\"]")
    #产品交付按钮
    deliverProductButton = (By.CSS_SELECTOR,"a[href=\"#/deliver/product\"]")

    def confirmBox(self):
        return self.get_element(self.confirmButton)

    def deliverButtonBox(self):
        return self.find_element(self.deliverButton)

    def deliverAlbumButtonBox(self):
        return self.find_element(self.deliverAlbumButton)

class CustomerManagerPageAction(CustomerManagerPage):

    def gotoDeliverAlbum(self):
        #确认--点击交付--点击影集交付
        self.confirmBox().click()
        self.deliverButtonBox().click()
        time.sleep(1)
        self.deliverAlbumButtonBox().click()

if __name__ == '__main__':
    HomePageAction().gotoPage()
    CustomerManagerPageAction().gotoDeliverAlbum()



