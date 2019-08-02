#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/31'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
                                                                   
          ]]`.        .]O@@@@\`.    ..]O@@@\`.      .,O\.          
          O@@@@`     =@^.,]]]`\@`  ,@/`.]]]`,O^    =@@@@.     ./`  
 ,]`      O@@@@@@.  =@^ =@@`.=^\@..@^ .@@\ .\.@.  =@@@@@^   ./@@@^ 
 @@@@].. .@@@@@@@@. =@^ .@@@@/./@..@^ .\@@@@`.@. .@@@@@@@`./@@@@@@.
.@@@@@@@@@@@@@@@@@^. \@`. ..../O.  ,@\.. ...,@`  =@@@@@@@@@@@@@@@O.
 @@@@@@@@@@@@@@@@@O.  .,\@@@/`.     .,[O@@@/`.   =@@@@@@@@@@@@@@@^ 
 .@@@@@@@@@@@@@@@@`       =@\         .=@^       .@@@@@@@@@@@@@@^. 
  .\@@@@@@@@@@@@/.       ..@@\]]]]]]]]]@@^..      .\@@@@@@@@@@@`   
    .\@@@@@@@@@`     .,/@@@@@@@@@@@@@@@@@@@@@O].   .,@@/[[[[[.     
             ,@@@`../@@@@@@@@@@@@@@@@@@@@@@@@@@@\,/@@@/.           
              .[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/[..             
                 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`               
                .O@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O.              
                .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.              
                .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O]]            
              .]/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`.,\@^          
            .=@/`.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O@@@O`.\.         
            .@`./@@O@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O`..\@\.          
            .`.@@^..@@@\@@@@@@@@@@@@@@@@@@/[`...,@@O. .\^          
              =@`  =@/.                          .=@^              
              .`   =@`                            .=^              

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from config.conf import DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)
driver.maximize_window()

def get_url():
    driver.get("D:\\softwareDate\\pycharm\\wuch-api-1906A\\demo(1).html")

def open_a():
    baidu = driver.find_element_by_partial_link_text('度娘')
    jd = driver.find_element_by_partial_link_text('京东')
    dd = driver.find_element_by_partial_link_text('当当')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(baidu).click(jd).click(dd).key_up(Keys.CONTROL).perform()

def windows_change_demo():
    # 获取所有窗口的句柄
    handles = driver.window_handles
    # 根据窗口句柄遍历所用窗口
    for h in handles:
        driver.switch_to.window(h)
        sleep(2)
        if(driver.title.__contains__('京东')):
            break

def open_alert():
    driver.find_element_by_xpath('//input[@type="reset"]').click()

def alert_alert_demo():
    a = driver.switch_to.alert
    a.accept()

def open_submit_confirm():
    driver.find_element_by_xpath('//input[@type="submit"]').click()

def submit_confirm_demo():
    b = driver.switch_to.alert
    # b.accept()
    b.dismiss()

def open_button_prompt():
    driver.find_element_by_xpath('//input[@type="button"]').click()

def button_prompt_demo():
    c = driver.switch_to.alert
    # b.accept()
    c.send_keys('I am 李刚')
    c.dismiss()

if __name__ == '__main__':
    get_url()
    sleep(2)
    # open_a()
    # sleep(2)
    # windows_change_demo()
    open_button_prompt()
    sleep(2)
    button_prompt_demo()
    sleep(2)
    # open_alert()
    # sleep(2)
    # alert_alert_demo()
    # sleep(2)
    open_submit_confirm()
    sleep(2)
    submit_confirm_demo()
    sleep(2)
    driver.quit()

