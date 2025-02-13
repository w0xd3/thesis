import requests
import time

# X:经度
# Y:纬度

# 高德地图API
def get_location_gaode(address):
    basic_url = 'https://restapi.amap.com/v3/place/text'

    params = {
        'key': 'b2b3b8122d34d535557df5b127595c84',
        'keywords': address,
        'city': '深圳'
    }
    
    time.sleep(0.4)

    try:
        res = requests.get(url=basic_url, params=params).json()
        if res['status'] == '1' and len(res['pois']) > 0:
            location = res['pois'][0]['location']
            x, y = map(float, location.split(','))
            print(f"{address} : {x}, {y}")
            return x, y
        else:
            print(f"无法解析地址，今日额度达到上限: {address}")
            return None, None
    except Exception as e:
        print(f"请求失败: {e}")
        return None, None

# 腾讯地图API
def get_location_tencent(address):

    # 腾讯地图 API Key（换成你的 Key）
    API_KEY = "6TCBZ-3YK64-IG7UU-FSWPT-FD6EF-AMB3B"

    # 搜索关键词
    keyword = address

    # 构造请求 URL
    url = f"https://apis.map.qq.com/ws/place/v1/search?keyword={keyword}&boundary=region(深圳,0)&key={API_KEY}"
    
    time.sleep(0.3)
    
    try:
        res = requests.get(url).json()
        location = res['data'][0]['location']
        x = location['lng']
        y = location['lat']
        print(f"{address} : {x}, {y}")
        return x, y
    except Exception as e:
        print(f"请求失败: {e}")
        return None, None

# 天地图API
def get_location_T(address):
    base_url = 'http://api.tianditu.gov.cn/v2/search'
    
    params = {
        'postStr': '{"keyWord":"%s","queryType":12,"start":0,"count":10,"specify":"156440300"}' % address,
        'type': 'query',
        'tk': '549147d53133271c33290eef5c84eac5'
    }
    
    try:
        res = requests.get(base_url, params=params).json()
        location = res['pois'][0]['lonlat']
        x, y = map(float, location.split(','))
        print(f"{address} : {x}, {y}")
        time.sleep(0.2)
        return x, y
    except Exception as e:
        print(f"请求失败: {e}")
        return None, None
    
    