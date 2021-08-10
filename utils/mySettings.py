# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/8 下午2:45
# @Author    :   fml
# @File      :   mySettings.py  
# @Software  :   PyCharm

from selenium import webdriver

webdriverDir = "D:\jmeter视频教程\selenium\chromedriver.exe"

loginUrl = "http://www7.haicaoyun.com/hlj-merchant-center/dist/index.html#/login"
account = "15744445510"
password = "123456mM"

timeout = 10
polTime = 0.5

customerManagerUrl = "http://crm7.haicaoyun.com/haicaoyun-front/dist/index.html#/businessOverview"
