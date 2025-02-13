import requests
import pandas as pd
from time import sleep

def get_location(address):
    basic_url = 'https://restapi.amap.com/v3/place/text'

    params = {
        'key':'b2b3b8122d34d535557df5b127595c84',
        'keywords':address,
        'city':'深圳'
    }

    res = requests.get(url=basic_url, params=params).json()
    # 取第一位解析出经纬度 pois-poi-location
    location = res['pois'][0]['location']
    x, y = map(float, location.split(','))
    
    print(f'{address} : {location}')
    
    sleep(0.4)
    return x,y
    


raw_data = pd.read_csv(rf'C:\Users\wanxi.wu\Desktop\答辩\毕业论文\code\深圳市定点零售药店名单.csv')
# 根据地址查找
raw_data[['X', 'Y']] = raw_data["地址"].apply(lambda addr: pd.Series(get_location(addr)))
raw_data.to_csv('./fill_x_y.csv')

