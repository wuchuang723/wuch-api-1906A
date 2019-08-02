import os

GY_API_URL = 'http://qa.yansl.com:8080'

GY_WEB_URL = 'http://qa.yansl.com'

GY_DB_URL = {                               
    'host': 'qa.guoyasoft.com',             
    'port': 3306,                           
    'db': 'guoya_virtual_mall_1811',        
    'user': 'root',                         
    'passwd': 'Guoya006',                   
    'charset': 'utf8'                       
}											

# 设置driver的绝对路径
DRIVER_PATH = os.path.join(os.path.dirname(__file__), "../chrome_driver_v75/chromedriver.exe")