def test_change_pwd(driver_data):
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = 'http://dev.guoyasoft.com:8080/cst/getAll/1/3'
    headers = {
        'token': driver_data['token'],
        'charset': 'UTF-8'
    }
    resp = request_tool.get_request(url,headers=headers)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)

# 在terminal控制台输入命令：
# pip install --upgrade guoya-api-test

from tools import init_tool

init_tool.init_api_project()
