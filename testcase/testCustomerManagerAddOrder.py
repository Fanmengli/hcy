# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      :   2021/8/10 上午1:10
# @Author    :   fml
# @File      :   testCustomerManagerAddOrder.py  
# @Software  :   PyCharm

from datetime import datetime
from random import randint
import pytest
import time
from pages.customerManager_addOrder import customerManagerAddOrderObj

class TestCustomerManagerAddOrder:
    # 测试用例：先添加一个影集，再获取最新影集的标题和拍摄时间，与输入的标题和时间做比较
    name = "自动" + str(randint(100, 1000))
    first_name = name
    first_phone = "1578888{}".format(randint(1000, 9999))
    couple_name = "沐沐"
    couple_phone = "17764505169"
    current_time = datetime.now().strftime('%Y-%m-%d')

    def test_add_order(self):
        customerManagerAddOrderObj.gotoPage()
        customerManagerAddOrderObj.gotoConfirm()
        customerManagerAddOrderObj.gotoDeliver()
        customerManagerAddOrderObj.gotoDeliverAlbum()
        # 新建影集
        customerManagerAddOrderObj.add_order_action(self.first_name, self.first_phone, self.couple_name,
                                                    self.couple_phone)
        # 新建完成点击影集交付，进入交付首页
        customerManagerAddOrderObj.gotoDeliverAlbum()
        time.sleep(1)
        # 获取第一个订单的第一联系人和第二联系人姓名、时间
        real_first_name = customerManagerAddOrderObj.getOrderTitleAction()[0]
        real_couple_name = customerManagerAddOrderObj.getOrderTitleAction()[1]
        real_shoot_time = customerManagerAddOrderObj.getOrderShootTimeAction()

        assert real_first_name == self.first_name

        assert real_couple_name == self.couple_name

        assert real_shoot_time == self.current_time


if __name__ == '__main__':
    pytest.main(["testCustomerManagerAddOrder.py"])
