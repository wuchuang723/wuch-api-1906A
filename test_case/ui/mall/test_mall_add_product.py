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

from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf

@allure.feature("添加商品分类")
def test_login(base):
    #打开登录界面 http://qa.yansl.com/#/login
    base.get("打开登录界面",'http://qa.yansl.com/#/login')
    #输入用户名 //input[@type="text"]
    base.send_keys('输入用户名','''//input[@type="text"]''','admin')
    #输入密码 //input[@type="password"]
    base.send_keys('输入密码','''//input[@type="password"]''','123456')
    #点击登录 //span[contains(text(),'登录')]
    base.click('点击登录','''//span[contains(text(),'登录')]''')
    try:
        #残忍决绝 //span[text()='残忍拒绝']
        base.click('残忍拒绝','''//span[text()='残忍拒绝']''')
        #再次登录 //span[contains(text(),'登录')]
        base.click('点击登录', '''//span[contains(text(),'登录')]''')
    except:
        pass
    #断言方法1
    # f = False
    # try:
    #     base.local_element("//span[text()='首页']")
    #     f = True
    # except:
    #     pass
    # assert_tool.assert_equal(f,True)
    # with allure.step("登录跳转页面断言：实际结果：{},预期结果：{}".format(f,True)):pass
    #断言方法2
    # page_source = base.driver.page_source
    # with allure.step("登录跳转页面断言：实际结果：{},预期结果：{}".format(page_source,'首页')):pass
    # assert_tool.assert_in(page_source,'首页')
    #点击下拉菜单 //div[@class="hamburger-container"]/*[name()='svg']
    #断言方法3
    sleep(3)
    page_source = base.driver.page_source
    with allure.step("登录跳转页面断言"):
        allure.attach(page_source,"实际结果",allure.attachment_type.TEXT)
        allure.attach('首页','预期结果',allure.attachment_type.TEXT)

    base.click('点击下拉菜单','''//div[@class="hamburger-container"]/*[name()='svg']''')
    sleep(2)
    #点击商品按钮 (//div[@class="el-submenu__title"])[1]
    base.click('点击商品按钮','''(//div[@class="el-submenu__title"])[1]''')
    sleep(2)
    #点击添加商品 //span[text()='添加商品']
    base.click('点击添加商品','''//span[text()='添加商品']''')
    sleep(2)
    #点击商品分类下拉框 //span[@class="el-cascader__label"]
    base.click('点击商品分类下拉框','''//span[@class="el-cascader__label"]''')
    #选择服装 //li[text()='服装']
    base.click('选择服装','''//li[text()='服装']''')
    #选择外套 //li[text()='外套']
    base.click('选择外套','''//li[text()='外套']''')
    #输入商品名称 //label[contains(text(),'商品名称')]/..//input
    base.send_keys('输入商品名称','''//label[contains(text(),'商品名称')]/..//input''','不能说的秘密')
    # 输入副标题 //label[contains(text(),'副标题')]/..//input
    base.send_keys('输入副标题', '''//label[contains(text(),'副标题')]/..//input''', '青春帅气')
    #选择商品品牌 //input[@placeholder="请选择品牌"]
    base.click('选择商品品牌','''//input[@placeholder="请选择品牌"]''')
    #选择海澜之家 //span[text()='海澜之家']
    base.click('选择海澜之家','''//span[text()='海澜之家']''')
    #点击“下一步，填写商品促销” //span[text()='下一步，填写商品促销']
    base.click('点击“下一步，填写商品促销”','''//span[text()='下一步，填写商品促销']''')

    # 点击“下一步，填写商品属性” //span[text()='下一步，填写商品属性']
    base.click('点击“下一步，填写商品属性”', '''//span[text()='下一步，填写商品属性']''')

    #滚动窗口
    base.scroll_screen("滚动窗口")
    #窗口切换至iframe
    # base.switch_to_frame('窗口切换至iframe','''(//iframe)[1]''')
    # #输入电脑端详情
    # base.send_keys('输入电脑端详情','''//body''','清仓大甩卖')
    # #切出iframe
    # base.switch_to_content('切出iframe')

    # 点击“下一步，选择商品关联” //span[text()='下一步，选择商品关联']
    base.click('点击“下一步，选择商品关联”', '''//span[text()='下一步，选择商品关联']''')

    # 点击“完成，提交商品” //span[text()='完成，提交商品']
    base.click('点击“完成，提交商品”', '''//span[text()='完成，提交商品']''')

    # 点击“确认” (//button/span)[last()]
    base.click('点击“确认”', '''(//button/span)[last()]''')
    sleep(2)
    pass