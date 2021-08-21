# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/9 下午8:01
# @Author    :   fml
# @File      :   basePage.py  
# @Software  :   PyCharm

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utils.mySettings import timeout,polTime

from utils.myDriver import Driver


class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()

    def get_element(self,locator):
        """
        根据表达式匹配单个元素，显示等待逻辑
        :param locator:
        :return:
        """
        WebDriverWait(
            #传入浏览器对象
            driver=self.driver,
            #传入超时时间
            timeout = timeout,
            #传入轮询时间
            poll_frequency=polTime).until(
            EC.visibility_of_element_located(locator)
        )
        #解包
        return self.driver.find_element(*locator)

    def find_element(self,locator):
        return self.driver.find_element(*locator)

    def switch_to_page(self,url):
        allHandle = self.driver.window_handles
        for handle in allHandle:
            self.driver.switch_to.window(handle)
            if self.driver.current_url == url:
                break

    def input_text(self,locator,text):
        return self.find_element(locator).send_keys(text)

    # def click(self,*locator):
    #     return self.find_element(*locator).click()

    def get_title(self):
        return self.driver.title

    def mouse_left_click(self,locator):
        return ActionChains(self.driver).click(locator).perform()

    def alert_accept(self,locator):
        """弹窗点击确认"""
        self.find_element(locator).click()
        self.driver.switch_to.alert.accept()

    # @classmethod
    def quitDriver(self):
        print('-----teardown-----')
        return self._driver.quit()

    def mouse_left_click(self,locator):
        ActionChains(self.driver).click(locator).perform()





