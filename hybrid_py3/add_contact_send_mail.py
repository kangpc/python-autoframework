#coding=utf-8
# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print(u"启动浏览器...")
# 创建Chrome浏览器的实例
driver = webdriver.Chrome(executable_path="e:\\python27\\chromedriver")
# 最大化浏览器窗口
driver.maximize_window()
print(u"启动浏览器成功")
print(u"访问126邮箱登录页...")
driver.get("http://mail.126.com")
# 暂停5秒,以便邮箱登录页面加载完成
time.sleep(5)
assert u"126网易免费邮--你的专业电子邮局" in driver.title
print(u"访问126邮箱登录页成功")
# 创建显示等待
wait = WebDriverWait(driver, 30)
# 检查id为x-URS-iframe的frame是否存在，存在则切换进frame控件
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@id,'URS')]")))
# 获取用户名输入框
userName = driver.find_element_by_xpath('//input[@name="email"]')
# 输入用户名
userName.send_keys("zxhkpc")
# 获取密码输入框
pwd = driver.find_element_by_xpath("//input[@name='password']")
# 输入密码
pwd.send_keys("Aa0607!")
# 发送一个回车键
pwd.send_keys(Keys.RETURN)
print(u"用户登录...")
# 等待5秒,以便登录成功后的页面加载完成
time.sleep(5)
assert u"网易邮箱" in driver.title
print(u"登录成功")
print(u"添加联系人...")
# 显示等待通讯录链接页面元素的出现
addressBook = wait.until(EC.visibility_of_element_located
    ((By.XPATH, "//div[text()='通讯录']")))
# 点击“通讯录”按钮
addressBook.click()
# 显示等待新建联系人按钮出现
newContact = wait.until(EC.visibility_of_element_located
    ((By.XPATH, "//span[text()='新建联系人']")))
# 点击新建联系人按钮
newContact.click()

# 显示等待输入联系人输入框的出现
contactName = wait.until(EC.visibility_of_element_located
    ((By.XPATH,
    "//a[@title='编辑详细姓名']/preceding-sibling::div/input")))
contactName.send_keys(u"lily")
# 输入联系人电子邮箱
driver.find_element_by_xpath(
    "//*[@id='iaddress_MAIL_wrap']//input"
    ).send_keys(u"lily@qq.com")
driver.find_element_by_xpath(
    "//span[text()='设为星标联系人']/preceding-sibling::span/b"
    ).click()
# 输入联系人手机号
driver.find_element_by_xpath(
    "//*[@id='iaddress_TEL_wrap']//dd//input").send_keys("185xxxxxx")
# 输入备注信息
driver.find_element_by_xpath("//textarea").send_keys(u"朋友")
# 点击“确认”按钮
driver.find_element_by_xpath("//span[text()='确 定']").click()
time.sleep(2)
assert "lily@qq.com" in driver.page_source
print(u"添加联系人成功")

print(u"进入首页")
driver.find_element_by_xpath('//div[.="首页"]').click()
print(u"写信...")
# 显示等待写信链接页面元素的出现
element = wait.until(EC.visibility_of_element_located
    ((By.XPATH, "//span[text()='写 信']")))
# 点击写信链接
element.click()
# 写入收件人地址
driver.find_element_by_xpath(
    "//div[contains(@id,'_mail_emailinput')]/input"
    ).send_keys("testman1980@126.com")
# 写入邮件主题
driver.find_element_by_xpath(
    "//div[@aria-label='邮件主题输入框，请输入邮件主题']/input"
    ).send_keys(u"光荣之路")
# 切换进frame控件
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@tabindex=1]"))
editBox = driver.find_element_by_xpath("/html/body")
editBox.send_keys(u"发给光荣之路的一封信")
driver.switch_to.default_content()
print(u"写信完成")
driver.find_element_by_xpath("//header//span[text()='发送']").click()
print(u"开始发送邮件...")
time.sleep(3)
assert u"发送成功" in driver.page_source
print(u"邮件发送成功")
time.sleep(5)
driver.quit()
