# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/11 上午12:55
# @Author    :   fml
# @File      :   customerManager_orderList.py  
# @Software  :   PyCharm
from selenium.common.exceptions import NoSuchElementException
from pages.customerManagerPage import CustomerManagerPageAction
from selenium.webdriver.common.by import By
import time


class CustomerManagerOrderList(CustomerManagerPageAction):
    #第一联系人姓名
    first_name = (
        By.CSS_SELECTOR,".hljd-table-tbody>tr:nth-child(2)>td span[class=\"style__gender-name--2muqY\"]:nth-child(1)")

    # 第二联系人姓名
    couple_name = (
        By.CSS_SELECTOR, ".hljd-table-tbody>tr:nth-child(2)>td span[class=\"style__gender-name--2muqY\"]:nth-child(2)")

    #第一个勾选框
    check_box_first = (By.CSS_SELECTOR,".hljd-table-tbody>tr:nth-child(2)>td input")

    #删除按钮
    delete_button = (By.CSS_SELECTOR,".tableStyle__danger--38tFg")

    #确认按钮
    accept_button = (By.CSS_SELECTOR,".hljd-btn-dangerous>span")

    #弹窗
    alert_popup_window = (By.CSS_SELECTOR,".hljd-modal-body")

class CustomerManagerOrderListAction(CustomerManagerOrderList):
    def getFirstName(self):
        """获取第一联系人姓名"""
        return self.find_element(self.first_name)

    def getCoupleName(self):
        """获取第一联系人姓名"""
        return self.find_element(self.couple_name)

    def tickoffCheckBox(self):
        """勾选第一条订单的选择框"""
        return self.find_element(self.check_box_first).click()

    def deleteOrderAction(self):
        """删除订单操作"""
        # return self.find_element(self.delete_button)
        try :
            return self.find_element(self.delete_button).click()
        except NoSuchElementException:
            print("删除按钮未显示")
    def alertAcceptAction(self):
        """弹窗点击确定，不是默认弹窗，所以无法获取"""
        # return self.alert_accept(self.alert_popup_window)
        return self.find_element(self.accept_button).click()

if __name__ == '__main__':
    CustomerManagerOrderListAction().gotoPage()
    CustomerManagerOrderListAction().gotoConfirm()
    CustomerManagerOrderListAction().gotoOrderTab()
    CustomerManagerOrderListAction().tickoffCheckBox()
    time.sleep(1)
    CustomerManagerOrderListAction().deleteOrderAction()
    #弹窗点击确定，删除成功
    CustomerManagerOrderListAction().alertAcceptAction()