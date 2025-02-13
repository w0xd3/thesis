from datetime import datetime
import pandas as pd
from get_location import get_location_gaode, get_location_tencent, get_location_T

# 搞个log兜底比较好，获取到一行就输出一行到日志

def process_data(data):
    
    first_null_index = data[data['X'].isnull()].index.min()

    for idx, addr in enumerate(data.loc[first_null_index:, '地址']):
        location = get_location_T(addr)
        if location is None:
            print(f"Location not found for address: {addr}. Stopping further processing...")
            current_date = datetime.now().strftime('%Y-%m-%d')
            data.to_csv(f'./深圳市定点零售药品名单_{current_date}.csv')
            break  # 一旦返回 None，就停止循环
        data.loc[first_null_index + idx, ['X', 'Y']] = location
    data.to_csv(f'./深圳市定点零售药品名单_all.csv')

# 读取原始数据
raw_data = pd.read_csv(rf'C:\Users\wanxi.wu\Desktop\答辩\毕业论文\code\深圳市定点零售药店名单.csv')

# 批量处理数据
process_data(raw_data)
