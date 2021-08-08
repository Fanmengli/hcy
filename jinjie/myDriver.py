# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/8 下午2:48
# @Author    :   fml
# @File      :   myDriver.py  
# @Software  :   PyCharm

from selenium import webdriver
from jinjie.mySettings import loginUrl,account,password

class Driver:

    #初始化一个空的driver   （_driver，可被其他类继承的，语法上没有特殊含义）
    _driver = None

    @classmethod
    def get_driver(cls,browserName="Chrome"):
        if cls._driver == None:
            if browserName == "Chrome":
                cls._driver = webdriver.Chrome()
            elif browserName == "ie":
                cls._driver = webdriver.Ie()
            elif browserName == "firefox":
                cls._driver == webdriver.Firefox()
            else:
                raise ("找不到浏览器，请检查传参")
            #第一次，设置最大化和隐式等待
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(3)
            #login在这里执行，保证登录在其他操作之前
            cls.login()
        return cls._driver

    #登录就一次就可以
    @classmethod
    def login(cls):
        """
        登录就一次就好，所以放在Driver中
        cls._driver = webdriver.Chrome()在上一个方法中，所以在这个方法中调用时，pycharm不会联想，可以将这句话复制过来即可联想，之后删掉
        :return:
        """
        # cls._driver = webdriver.Chrome()
        cls._driver.get(loginUrl)
        cls._driver.find_element_by_css_selector(".index-module__account--238f5 input").send_keys(account)
        cls._driver.find_element_by_css_selector(".index-module__password--1fHpE input").send_keys(password)
        cls._driver.find_element_by_class_name("index-module__login-btn--1En8M").click()

if __name__ == '__main__':
    Driver.get_driver()