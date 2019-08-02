#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/25'
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
# 1、导包 demo_import_api
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

# 2、找模板写测试用例 demo_http_
# test_change_pwd_var方法名，可以自定义，但是必须是test_开头 test_user_admin_register_1
def test_user_admin_register_1():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    # url 网址， conf.GY_API_URL 需要在config.conf.py文件中配置，相当于http请求默认值 '/admin/register'请求地址
    url = conf.GY_API_URL + '/admin/register'
    # username 类似于jmeter中的变量
    username = "wuch_725"
    # 请求数据，数据格式统一选用字典类型 注意json null 对应的是字典中的None
    req = { "email": "276461755@qq.com",
            "icon": "",
            "nickName": "wuch",
            "note": "",
            "password": "123456",
            "username": "wuch_725"
    }
    # post_request表示发送一个post请求，json=表示发送的数据格式为json，如果数据格式为键值对，用data=
    resp = request_tool.post_request(url,json=req)
    # resp.json()获取响应正文中的数据，并把这些数据从字符串转成字典格式，如果想获取字符串格式的数据，resp.text
    body = resp.json()
    # 判断响应码 resp.status_code获取响应状态码，200预期结果
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言 body['data']["username"]字典中获取某个key的值，username 预期结果，是一个变量
    assert_tool.assert_equal(body['data']["username"],username)

