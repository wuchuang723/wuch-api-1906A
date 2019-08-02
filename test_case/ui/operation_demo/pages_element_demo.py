#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __title__ = ''
# __author__ = 'xuepl'
# __mtime__ = '2019/7/30'
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config.conf import DRIVER_PATH



driver = webdriver.Chrome(DRIVER_PATH)
driver.maximize_window()


def get_url():
    driver.get("D:\\softwareDate\\pycharm\\wuch-api-1906A\\demo(1).html")

def quit_browser():
    # 退出驱动关闭浏览器
    driver.quit()

def text_demo():
    #操作页面元素
    #定位元素//input[@type="text"]
    text = driver.find_element_by_xpath('//input[@type="text"]')
    #操作元素
    #清空
    text.clear()
    #输入
    text.send_keys("整个江湖都任我闯，我的生命像一首歌")
    # print(text.get_attribute("value"))

def file_demo():
    file = driver.find_element_by_xpath('//input[@type="file"]')
    file.clear()
    file.send_keys("D:\\softwareDate\\第六周-界面自动化\\第一天\\1.png")


def radio_demo():
    radio = driver.find_element_by_xpath('(//input[@type="radio"])[1]')
    radio.click()

def checkbox_demo():
    checkbox1 = driver.find_element_by_xpath('(//input[@type="checkbox"])[1]')
    checkbox1.click()
    checkbox2 = driver.find_element_by_xpath('(//input[@type="checkbox"])[2]')
    checkbox2.click()

# def button_demo():
#     button = driver.find_element_by_xpath('//input[@type="button"]')
#     button.click()

def password_demo():
    password = driver.find_element_by_xpath('//input[@type="password"]')
    password.clear()
    password.send_keys("wuch123456")

def number_demo():
    number = driver.find_element_by_xpath('//input[@type="number"]')
    number.clear()
    number.send_keys("123456")

def date_demo():
    date = driver.find_element_by_xpath('//input[@type="date"]')
    js ='''var xpath = '//input[@type="date"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","2019-07-30");'''
    driver.execute_script(js)

def time_demo():
    time = driver.find_element_by_xpath('//input[@type="time"]')
    time.clear()
    time.send_keys("20:53")

def textarea_demo():
    textarea = driver.find_element_by_xpath('//td/textarea')
    textarea.clear()
    textarea.send_keys("飘向北方别问我家乡")

def select_demo():
    # select = driver.find_element_by_xpath('//select/option[2]')
    # select.click()
    s = driver.find_element_by_xpath('//select')
    select1 = Select(s)
    select1.select_by_index(2)
    sleep(2)
    select1.select_by_value('z2')
    sleep(2)
    select1.select_by_visible_text('周龙1')
    sleep(2)

def a_demo():
    # a = driver.find_element_by_xpath('//td/a[2]')
    # a.click()
    baidu = driver.find_element_by_partial_link_text('度娘')
    actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).click(baidu).key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.SHIFT).click(baidu).key_up(Keys.SHIFT).perform()

def submit_demo():
    submit = driver.find_element_by_xpath('//input[@type="submit"]')
    submit.click()

def open_alert():
    driver.find_element_by_xpath('//input[@type="reset"]').click()

def alert_alert_demo():
    a = driver.switch_to.alert
    a.accept()




if __name__ == '__main__':
    get_url() #获取网址
    sleep(1)
    # text_demo() #文本输入框
    # sleep(1)
    # file_demo() #文件上传框
    # sleep(1)
    # radio_demo() #单选框
    # sleep(1)
    # checkbox_demo() #多选框
    # sleep(1)
    # # button_demo() #普通按钮
    # # sleep(2)
    # password_demo() #密码输入框
    # sleep(1)
    # number_demo() #数字输入框
    # sleep(1)
    # date_demo() #日期控件
    # sleep(1)
    # time_demo() #时间控件
    # sleep(1)
    # textarea_demo() #文本输入区
    # sleep(1)
    select_demo() #下拉框
    a_demo() #超链接
    sleep(2)
    submit_demo() #提交按钮
    sleep(2)
    open_alert()
    sleep(2)
    alert_alert_demo()
    sleep(2)
    quit_browser() #关闭浏览器及驱动