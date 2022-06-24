# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/9 下午8:01
# @Author    :   fml
# @File      :   basePage.py  
# @Software  :   PyCharm

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from utils.mySettings import polTime, host
from utils.myDriver import Driver


class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()

    def get_element(self, locator, timeout):
        """
        根据表达式匹配单个元素，显示等待逻辑
        :param locator:
        :return:
        """
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=timeout,
            # 传入轮询时间
            poll_frequency=polTime).until(
            EC.visibility_of_element_located(locator)
        )
        # 解包
        return self.driver.find_element(*locator)

    def is_element_exist(self, locator):
        flag = True
        ele = self.driver.find_elements(*locator)
        if len(ele) == 1:
            return flag
        else:
            flag = False
            return flag

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def switch_to_page(self, url):
        url = f'{host}url'
        allHandle = self.driver.window_handles
        for handle in allHandle:
            self.driver.switch_to.window(handle)
            if self.driver.current_url == url:
                break

    def input_text(self, locator, text):
        return self.find_element(locator).send_keys(text)

    def get_title(self):
        return self.driver.title

    def mouse_left_click(self, locator):
        return ActionChains(self.driver).click(locator).perform()

    def alert_accept(self, locator):
        """弹窗点击确认"""
        self.find_element(locator).click()
        self.driver.switch_to.alert.accept()

    def quitDriver(self):
        print('-----teardown-----')
        self.driver.quit()

    def mouse_left_click(self, locator):
        """左击"""
        ActionChains(self.driver).click(locator).perform()

    def forward(self):
        """前进"""
        self.driver.forward()

    def back(self):
        """后退"""
        self.driver.back()

    def move_to_element(self, locator):
        """悬停到某个元素"""
        ActionChains(self.driver).move_to_element(self.driver.find_element(locator)).perform()

    def context_click(self, locator):
        """右击"""
        ActionChains(self.driver).context_click(self.driver.find_element(locator)).perform()

    def context_click(self, locator):
        """右击"""
        ActionChains(self.driver).double_click(self.driver.find_element(locator)).perform()

    def drag_and_drop(self, locator1, locator2):
        """右击"""
        loc1 = self.driver.find_element(locator1)
        loc2 = self.driver.find_element(locator2)
        ActionChains(self.driver).drag_and_drop(loc1, loc2).perform()
