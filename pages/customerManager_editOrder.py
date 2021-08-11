# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/10 下午11:48
# @Author    :   fml
# @File      :   customerManager_editOrder.py  
# @Software  :   PyCharm
import datetime
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.customerManager_addOrder import CustomerManagerAddOrderAction

class CustomerManagerEditOrder(CustomerManagerAddOrderAction):
    def __init__(self):
        super().__init__()
    # 图片为空时选择图片
    select_photo = (By.CLASS_NAME,".style__origanal_input--Vvh5-")
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
# r"D:\Desktop\图片\auto-photo\1.jpg" "D:\Desktop\图片\精修图片\1 (1).jpg"

class CustomerManagerEditOrderAction(CustomerManagerEditOrder):

    def selectPhoto(self,photoUrl):
        """图片为空时点击选择图片按钮"""
        self.find_element(self.select_photo).send_keys(photoUrl)

    def selectPhotoNotEmpty(self):
        """图片不为空时点击选择图片按钮"""
        self.find_element(self.select_photo_not_empty)

    def bulkOperationButton(self):
        """点击批量操作按钮"""
        self.find_element(self.bulk_operation_button)

if __name__ == '__main__':
    first_name = "自动" + str(random.randint(100, 1000))
    first_phone = "1578888{}".format(random.randint(1000, 9999))
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    print("current_time:", current_time)
    CustomerManagerEditOrderAction().gotoPage()
    CustomerManagerEditOrderAction().gotoConfirm()
    CustomerManagerEditOrderAction().gotoDeliver()
    CustomerManagerEditOrderAction().gotoDeliverAlbum()
    time.sleep(2)
    CustomerManagerEditOrderAction().gotoFirstOrderAction()
    time.sleep(1)
    CustomerManagerEditOrderAction().selectPhoto(r"D:\Desktop\图片\auto-photo\1.jpg")

