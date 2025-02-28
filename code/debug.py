import numpy as np
import pandas as pd
import random
import math

# 示例数据：随机生成的点的坐标和需求量
max_capacity = 40000
df = pd.read_csv('./data.csv')
df = df.sample(500)
center = pd.read_csv('../data/深圳市药品配送中心.csv', encoding='gbk')

# 计算两点之间的欧几里得距离
def distance(point1, point2):
    # 将经纬度转换为弧度
    lat1, lon1, lat2, lon2 = map(math.radians, [point1[0], point1[1], point2[0], point2[1]])
    
    # 计算纬度和经度的差值
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    
    # 应用 Haversine 公式
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # 地球平均半径（公里）
    R = 6371.0
    distance = R * c
    
    return distance

# 解析路径
def parse_route(solution):
    routes = []
    current_route = []
    current_capacity = 0
    
    for idx in solution:
        demand = df.loc[idx, 'demand']
        if current_capacity + demand > max_capacity:
            # 如果超出载重限制，结束当前子路径
            routes.append(current_route)
            current_route = []
            current_capacity = 0
        current_route.append(idx)
        current_capacity += demand
    
    # 添加最后一个子路径
    if current_route:
        routes.append(current_route)
    
    return routes

# 模拟退火算法
def simulated_annealing_vrp(df, num_points, center_x, center_y, name):
    # 初始化温度和冷却率
    temperature = 1000
    cooling_rate = 0.99
    stopping_temperature = 1
    
    # 随机生成初始解
    current_solution = list(df.index)
    random.shuffle(current_solution)
    current_solution = np.array(current_solution)
    
    # 计算初始解的适应度值
    def fitness(solution):
        total_distance = 0
        current_capacity = 0
        current_point = (center_x, center_y)  # 配送中心
        
        for idx in solution:
            next_point = (df.loc[idx, 'X'], df.loc[idx, 'Y'])
            demand = df.loc[idx, 'demand']
            
            # 检查载重约束
            if current_capacity + demand > max_capacity:
                # 如果超出载重限制，返回到配送中心并重新开始
                total_distance += distance(current_point, (center_x, center_y))
                current_point = (center_x, center_y)
                current_capacity = 0
            
            total_distance += distance(current_point, next_point)
            current_point = next_point
            current_capacity += demand
        
        # 最后返回配送中心
        total_distance += distance(current_point, (center_x, center_y))
        
        return 1 / (1 + total_distance)
    
    current_fitness = fitness(current_solution)
    
    while temperature > stopping_temperature:
        # 生成新的解
        new_solution = current_solution.copy()
        i, j = random.sample(range(num_points), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        
        # 计算新解的适应度值
        new_fitness = fitness(new_solution)
        
        # Metropolis准则
        if new_fitness > current_fitness or random.uniform(0, 1) < math.exp((new_fitness - current_fitness) / temperature):
            current_solution = new_solution
            current_fitness = new_fitness
        
        # 降低温度
        temperature *= cooling_rate
    
    # 输出最优解
    print(f"最优路径: {current_solution}")
    print(f"适应度值: {current_fitness}")
    print(f"配送中心: {name}")
    
    # 解析路径
    routes = parse_route(current_solution)
    print("车辆路径:")
    for i, route in enumerate(routes):
        print(f"子路径 {i+1}: {route}")
    
    return current_solution, current_fitness

# 调用模拟退火算法
for idx, frame in df.groupby('Cluster'):
    print('-' * 10)
    fn = simulated_annealing_vrp(frame, frame.shape[0], center.loc[idx, 'X'], center.loc[idx, 'Y'], center.loc[idx, '配送中心'])