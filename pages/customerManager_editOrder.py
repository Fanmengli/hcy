# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/10 下午11:48
# @Author    :   fml
# @File      :   customerManager_editOrder.py  
# @Software  :   PyCharm
import datetime
import random
import time

import win32com.client
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.customerManager_addOrder import CustomerManagerAddOrderAction
from pages.customerManagerPage import CustomerManagerPageAction

class CustomerManagerEditOrder(CustomerManagerAddOrderAction):
    def __init__(self):
        super().__init__()
    # 图片为空时选择图片
    select_photo = (By.CSS_SELECTOR,"input[class^=style__origanal_input]")
    #图片不为空时选择图片
    select_photo_not_empty = (By.CSS_SELECTOR,".style__origanal_input--Vvh5-")
    #批量操作按钮
    bulk_operation_button= (By.CSS_SELECTOR,".style__batch_wrap--3HUFb>.hljd-btn>span")
    #添加相册按钮
    add_photo_album_button = (By.CSS_SELECTOR,".style__add_album--3_7uv")
    #图文请帖tab
    image_invitation_card = (By.CSS_SELECTOR,".hljd-radio-group-outline>label:nth-child(2)")
    #视频请帖tab
    video_invitation_card = (By.CSS_SELECTOR,".hljd-radio-group-outline>label:nth-child(3)")
    #婚礼MVtab
    mv_card = (By.CSS_SELECTOR,".hljd-radio-group-outline>label:nth-child(4)")

    def selectPhoto(self):
        """图片为空时点击选择图片按钮"""
        return self.find_element(self.select_photo)

    def selectPhotoNotEmpty(self):
        """图片不为空时点击选择图片按钮"""
        return self.find_element(self.select_photo_not_empty)

    def bulkOperationButton(self):
        """点击批量操作按钮"""
        return self.find_element(self.bulk_operation_button)

class CustomerManagerEditOrderAction(CustomerManagerEditOrder):

    def selectPhotoClickAction(self,photoUrl):
        """图片为空时图片选择按钮不存在，则使用不为空时的按钮"""
        self.mouse_left_click(self.selectPhoto())
        # 对于 非 input 标签实现的上传功能, 我们可以用模拟键盘敲击的方式实现
        sh = win32com.client.Dispatch("WScript.shell")
        # 1、文件路径不得包含中文  2、输入法要保持英文输入状态
        sh.Sendkeys(photoUrl)

    def selectPhotoAction(self,photoUrl):
        """图片为空时图片选择按钮不存在，则使用不为空时的按钮"""
        self.selectPhoto().send_keys(photoUrl)
        # self.mouse_left_click(self.selectPhoto())
        # # 对于 非 input 标签实现的上传功能, 我们可以用模拟键盘敲击的方式实现
        # sh = win32com.client.Dispatch("WScript.shell")
        # # 1、文件路径不得包含中文  2、输入法要保持英文输入状态
        # sh.Sendkeys(photoUrl)
        # try:
        #     self.selectPhoto().send_keys(photoUrl)
        # except:
        #     self.selectPhotoNotEmpty().send_keys(photoUrl)

customerManagerEditOrderAction = CustomerManagerEditOrderAction()

if __name__ == '__main__':
    #进入影集交付列表
    customerManagerEditOrderAction.gotoDeliverAlbumAction()

    # first_name = "自动" + str(random.randint(100, 1000))
    # first_phone = "1578888{}".format(random.randint(1000, 9999))
    # current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # print("current_time:", current_time)
    # customerManagerEditOrderAction.add_order_action(first_name, first_phone, "沐沐", "17764505169")
    time.sleep(2)
    # #点击影集交付
    # customerManagerEditOrderAction.gotoDeliverAlbum()
    #进入第一个影集
    customerManagerEditOrderAction.gotoFirstOrderAction()
    # time.sleep(1)
    #点击上传图片
    customerManagerEditOrderAction.selectPhotoAction("D:\Desktop\\auto-photo\\1.jpg")

    # for i in range(1,10):
    #     time.sleep(0.5)
    #     customerManagerEditOrderAction.selectPhotoAction(f'D:\Desktop\\auto-photo\\{i}.jpg')
