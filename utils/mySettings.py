# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/8 下午2:45
# @Author    :   fml
# @File      :   mySettings.py  
# @Software  :   PyCharm

host = "http://www7.haicaoyun.com"

loginUrl = f"{host}/hlj-merchant-center/dist/index.html#/login"
account = "15744445510"
password = "123456mM"

# timeout = 15
polTime = 0.5

customerManagerUrl = f"{host}/haicaoyun-front/dist/index.html#/businessOverview"

if __name__ == '__main__':
    print(loginUrl)
