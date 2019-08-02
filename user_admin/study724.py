#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/24'
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

# 发送请求的包名，工具，框架-requests  (发送请求，用到的技术)
# 安装包    (安装或者引入)
# 导入   (使用别人写好的代码，首先要导包)
import pytest
import requests
# 发送post json请求
# data = {
#     "password": "123456",
#     "username": "admin"
# }
# r = requests.post("http://qa.yansl.com:8080/admin/login",json=data)
# print(r.text)

# 发送post 键值对请求
# para = {"adminId":42,"roleIds":2}
# r = requests.post("http://qa.yansl.com:8080/admin/role/update",data=para)
# print(r.text)

# 发送get请求，键值对格式的数据
# param = {"name":"admin","pageSize":5,"pageNum":1}
# response = requests.get("http://qa.yansl.com:8080/admin/list",params=param)
# print(response.text)

# json数据为空位表示为null，python数据为空表示为none

# 测试框架pytest控制用例的执行

# 使用安装pytest
# 修改pycharm中默认执行框架 file->settings->tools->python integrated Tools->default test runner修改成pytest
# 文件命名 test_开头，用例名命名test_

# pytest执行用例的方法
# '''
# 1、执行单个用例
# pytest.main(['-v','user_admin/test_11.py::test_a'])
# 2、执行一个python文件
# pytest.main(['-v','user_admin/test_11.py'])
# 3、执行一个包里边所有python文件
# pytest.main(['-v','user_admin'])
# 4、执行全部用例
# pytest.main(['-v'])
# 5、执行指定用例
#  1）给用例打标记
#  @pytest.mark.标记名
#  2）执行用例
#  pytest.main(['-v','-m','标记名'])
#
# '''

