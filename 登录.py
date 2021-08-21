from selenium import webdriver
import time

#driver设置全局变量
driver =webdriver.Chrome("D:\jmeter视频教程\selenium\chromedriver.exe")

class LoginPage:
    def __init__(self,url,driver):
        self.driver = driver

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        self.driver.get(url)
        #账号密码输入框、登录按钮定位
        self.account = driver.find_element_by_css_selector(".index-module__account--238f5 input")
        time.sleep(1)
        self.password = driver.find_element_by_css_selector(".index-module__password--1fHpE input")
        time.sleep(1)
        self.loginButton = driver.find_element_by_class_name("index-module__login-btn--1En8M")

#抽离出页面动作类，继承对应的页面类
class LoginPageAction(LoginPage):
    def login(self):
        self.account.send_keys("15744445510")
        self.password.send_keys("123456mM")
        self.loginButton.click()

lpa = LoginPageAction("http://www7.haicaoyun.com/hlj-merchant-center/dist/index.html#/login",driver)
lpa.login()

class SystemSelect:
    def __init__(self,driver):
        self.driver = driver
    #照片管理按钮和确认按钮
    def customerManager(self):
        return driver.find_element_by_id("serviceCardItem4")
        # self.confirmButton = driver.find_element_by_class_name("hljd-btn")

class SystemSelectAction(SystemSelect):
    def entryCustomerManager(self):
        self.customerManager().click()
        # 切换tab
        allHandle = driver.window_handles
        for handle in allHandle:
            driver.switch_to.window(handle)
            if driver.current_url == "http://crm7.haicaoyun.com/haicaoyun-front/dist/index.html#/businessOverview":
                break
        time.sleep(2)

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def confirmButton(self):
        return driver.find_element_by_class_name("hljd-btn")
    # 交付
    def deliverButton(self):
        return driver.find_element_by_xpath("//ul[@role=\"menu\"]/li[7]")
    # 影集交付
    def deliverAlbum(self):
        return driver.find_element_by_css_selector("a[href=\"#/deliver/album\"]")
    # 产品交付
    def deliverProduct(self):
        return driver.find_element_by_css_selector("a[href=\"#/deliver/product\"]")

class HomePageAction(HomePage):
    def enter(self):
        self.confirmButton().click()
    def enterAlbumDeliver(self):
        self.deliverButton().click()
        self.deliverAlbum().click()

ssa = SystemSelectAction(driver)
ssa.entryCustomerManager()

hpa = HomePageAction(driver)
hpa.enter()
hpa.enterAlbumDeliver()


# driver = webdriver.Chrome("/Users/hunliji/Downloads/chromedriver")
# driver =webdriver.Chrome()
#
# driver.get("http://www7.haicaoyun.com/hlj-merchant-center/dist/index.html#/login")
# driver.implicitly_wait(5)
# driver.maximize_window()
# # time.sleep(3)
# #输入账号
# account = driver.find_element_by_css_selector(".index-module__account--238f5 input").send_keys("15744445510")
#
# time.sleep(1)
# password = driver.find_element_by_css_selector(".index-module__password--1fHpE input").send_keys("123456mM")
# # password.send_keys("123456mM")
#
# time.sleep(1)
# #登录按钮
# loginButton = driver.find_element_by_class_name("index-module__login-btn--1En8M").click()
#
# # driver.quit()
# #进入客户管理系统
# driver.find_element_by_id("serviceCardItem4").click()
# time.sleep(2)
# #切换tab
# allHandle = driver.window_handles
# for handle in allHandle:
#     driver.switch_to.window(handle)
#     if driver.current_url == "http://crm7.haicaoyun.com/haicaoyun-front/dist/index.html#/businessOverview":
#         break
# time.sleep(2)
# #关闭弹框
# confirmButton = driver.find_element_by_class_name("hljd-btn")
# confirmButton.click()
#
# deliverButton = driver.find_element_by_xpath("//ul[@role=\"menu\"]/li[7]").click()
# time.sleep(1)
# albumDeliver = driver.find_element_by_css_selector("a[href=\"#/deliver/album\"]").click()
#
# #添加影集
# driver.find_element_by_xpath(".style__pay_left--uYB41>button:nth-child(2)").click()

