

from selenium import webdriver
from selenium.webdriver.support.select import Select
#windows：import win32com.client
#mac要导入2个：from pykeyboard import PyKeyboard
#from pymouse import PyMouse

driver = webdriver.Chrome()

driver.find_element_by_class_name("")
driver.find_element_by_id("")
driver.find_element_by_name("")
driver.find_element_by_tag_name("")
driver.find_element_by_link_text("")
driver.find_element_by_partial_link_text("")
driver.find_element_by_css_selector("")
driver.find_element_by_xpath("")

# 定位下拉框元素
ele = driver.find_element_by_name("type")
Select(ele).select_by_value("2")
Select(ele).select_by_index(4) #下标从0开始
Select(ele).select_by_visible_text("z")
'''
文件上传：
1.input控件上传：当做一个输入框，用send_keys指定文件路径
2.非input标签：模拟键盘敲击的方式实现

'''

# 切换iframe内嵌网页
ifm = driver.find_element_by_css_selector("")
driver.switch_to.frame(ifm)
#定位frame中的元素，并填充文案
driver.find_element_by_css_selector("").send_keys("文案")
#回到上层
driver.switch_to.default_content()
#之后再操作iframe层的其他元素
