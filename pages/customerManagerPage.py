# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/9 下午8:24
# @Author    :   fml
# @File      :   firstPage.py  
# @Software  :   PyCharm

import time
from pages.homePage import HomePageAction
from selenium.webdriver.common.by import By


class CustomerManagerPage(HomePageAction):
    def __init__(self):
        super().__init__()

    """确认按钮"""
    knowButton = (By.CSS_SELECTOR, "button[type=\"button\"]>span")
    """订单按钮"""
    orderTab = (By.XPATH, "//ul[@role=\"menu\"]/li[4]")
    """交付按钮"""
    deliverButton = (By.XPATH, "//ul[@role=\"menu\"]/li[7]")
    """影集交付按钮"""
    deliverAlbumButton = (By.CSS_SELECTOR, "a[href=\"#/deliver/album\"]")
    """产品交付按钮"""
    deliverProductButton = (By.CSS_SELECTOR, "a[href=\"#/deliver/product\"]")
    """订单标题"""
    order_title = (By.CSS_SELECTOR, ".style__list_content--mat4N>li:nth-child(1) h4")
    """订单拍摄日期"""
    order_shoot_time = (By.CSS_SELECTOR, ".style__list_content--mat4N>li:nth-child(1) p:first-child")
    """第一个订单"""
    first_order = (By.CSS_SELECTOR, "ul[class^=style__list_content]>li:nth-child(1)")

    def knowBox(self):
        """进入crm系统后的确认弹框"""
        return self.get_element(self.knowButton, 10)

    def orderTabBox(self):
        """订单按钮"""
        return self.find_element(self.orderTab)

    def deliverButtonBox(self):
        """交付按钮"""
        return self.find_element(self.deliverButton)

    def deliverAlbumButtonBox(self):
        """影集交付按钮"""
        return self.find_element(self.deliverAlbumButton)

    def deliverProductButtonBox(self):
        """产品交付按钮"""
        return self.find_element(self.deliverProductButton)

    def getOrderTitle(self):
        """得到订单标题"""
        return self.find_element(self.order_title)

    def getOrderShootTime(self):
        """得到订单拍摄日期"""
        return self.find_element(self.order_shoot_time)

    def getFirstOrder(self):
        """得到第一个订单"""
        return self.find_element(self.first_order)


class CustomerManagerPageAction(CustomerManagerPage):

    def gotoConfirm(self):
        """确认"""
        self.knowBox().click()

    def gotoOrderTab(self):
        """点击订单tab"""
        self.orderTabBox().click()

    def gotoDeliver(self):
        """点击交付tab"""
        self.deliverButtonBox().click()

    def gotoDeliverAlbum(self):
        """点击影集交付"""
        time.sleep(1)
        self.deliverAlbumButtonBox().click()

    def gotoDeliverAlbumAction(self):
        """进入影集交付页面"""
        self.gotoPage()
        self.gotoConfirm()
        self.gotoDeliver()
        self.gotoDeliverAlbum()

    def getOrderTitleAction(self):
        # contentText = self.getOrderTitle().get_attribute("textContent")
        try:
            contentText = self.getOrderTitle().get_attribute("textContent")
            print(contentText)
            if "&" in contentText:
                firstNameText = contentText.split("&")[1].strip()
                coupleNameText = contentText.split("&")[0].strip()
                return firstNameText, coupleNameText
            else:
                firstNameText = contentText
                return firstNameText
        except IndexError:
            print("没有第一联系人姓名")

    def getOrderShootTimeAction(self):
        # shootTimeText = self.getOrderShootTime().text
        shootTimeText = self.getOrderShootTime().get_attribute("textContent")
        return shootTimeText.split("：")[1]

    def gotoFirstOrderAction(self):
        return self.getFirstOrder().click()


if __name__ == '__main__':
    CustomerManagerPageAction().gotoDeliverAlbumAction()
    time.sleep(1)
    print("标题：", CustomerManagerPageAction().getOrderTitleAction())
    print("时间：", CustomerManagerPageAction().getOrderShootTimeAction())
    CustomerManagerPageAction().gotoFirstOrderAction()
