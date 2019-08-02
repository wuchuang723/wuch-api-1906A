#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __title__ = ''
# __author__ = 'xuepl'
# __mtime__ = '2019/7/30'

# 浏览器的基本操作
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH, GY_WEB_URL

# 打开
driver = webdriver.Chrome(DRIVER_PATH)
# 调整浏览器窗口大小
# 最大化
driver.maximize_window()
# 自定义窗口分辨率
# driver.set_window_size(1280,960)
# 打开网址
driver.get("https://www.baidu.com/")
sleep(2)
driver.get("https://www.taobao.com/")
sleep(2)
driver.get("http://music.migu.cn/v3/music/player/audio")
sleep(5)
# 后退
driver.back()
sleep(2)
# 前进
driver.forward()
sleep(2)
# 刷新
driver.refresh()


sleep(5)
# 关闭
driver.close()
# 退出驱动
driver.quit()

