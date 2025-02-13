import re
import csv


pattern = r"(-?\d+\.\d+),(-?\d+\.\d+)"
text = '''深圳市南山区桃源街道桃源社区北环大道方大广场（一期）3、4号研发楼3号楼805 : 113.972673,22.556772
深圳市宝安区西乡街道固戍下围园工业区A栋1F103号 : 113.844884,22.596670
广东省深圳市宝安区西乡街道流塘社区工业路38号－2 : 113.885481,22.569978
深圳市宝安区西乡街道流塘社区新村6巷9号一楼101铺 : 113.885680,22.579188
深圳市宝安区西乡街道固戍社区固戍一路849号 : 113.849231,22.596885
深圳市宝安区航城街道三围社区西六巷10号102 : 113.844374,22.613456
深圳市宝安区西乡街道凤凰岗社区宝田一路213宝田一路213－2 : 113.885472,22.599791
深圳市宝安区西乡街道桃源居世外桃源12栋102号 : 113.864162,22.615899
深圳市宝安区福永街道福围社区东福围西街3号东福围西街3－2号－1 : 113.820142,22.653785
深圳市宝安区新桥街道新二社区新二路42号新二路42-2 : 113.840856,22.728572
深圳市宝安区新桥街道新桥社区新桥一路9号锦波楼9－1 : 113.837476,22.734862
深圳市宝安区航城街道黄田社区黄田市场E区003（3、4、5号铺） : 113.848572,22.627205
广东省深圳市宝安区西乡街道径贝社区径贝新村243号一楼102 : 113.876499,22.567437
深圳市宝安区新桥街道沙企社区富通路二巷2号创新花园富通路111 : 113.830891,22.720240
深圳市宝安区新桥街道上寮社区企安路12-64所在楼栋企安路12-64（8栋A座C01铺） : 113.883831,22.554986
深圳市宝安区西乡街道永丰社区一队A区4-95号一楼 : 113.869605,22.573758
深圳市宝安区西乡街道固戍社区海滨新村五区六巷4号102 : 113.845496,22.588233
深圳市宝安区新安街道宝城34区宝民路鸿景园5栋124 : 113.891776,22.573906
深圳市宝安区新安街道41区43栋首层（原新安镇翻身安乐41区109号） : 113.900711,22.558834
深圳市宝安区石岩街道龙腾社区上排新村南三巷3号一层101 : 113.935367,22.687220
深圳市宝安区石岩街道罗租社区罗租上新村八巷 14 号 一层 : 113.938744,22.673400
广东省深圳市宝安区沙井街道和一社区松福大道1021号101-103 : 113.790900,22.713266
深圳市宝安区西乡街道龙珠社区龙吟二路133号1层 : 113.879043,22.580057
深圳市宝安区西乡街道西乡社区真理街105号真理街123、125号 : 113.879009,22.574675
深圳市宝安区航城街道钟屋社区易尚三维产业楼1号楼703 : 113.859482,22.622234
深圳市宝安区西乡街道臣田社区臣田村西区1号101-102 : 113.876704,22.591358
深圳市宝安区西乡街道共乐社区上塘127号101 : 113.872806,22.578010
深圳市宝安区西乡街道固戍社区下围园新村六巷9-2号 : 113.846328,22.597752
深圳市宝安区福永街道怀德社区咸田三区一巷7号立新南路140号 : 113.816416,22.663919
深圳市宝安区西乡街道永丰社区劳动一队4-74号102铺 : 113.868884,22.573361
深圳市宝安区西乡街道流塘社区荔园一路60号一楼之一 : 113.889434,22.580289
深圳市宝安区松岗街道楼岗社区楼岗大道48号F栋101-1 : 113.858511,22.765830
深圳市宝安区福海街道桥头社区桥兴路31号桥兴路31号-2 : 113.807037,22.688810
深圳市宝安区西乡街道铁岗社区西六巷1号101 : 113.885976,22.601622
深圳市宝安区沙井街道蚝乡社区西沙路陞达厂公寓楼108 : 113.789532,22.736988
深圳市宝安区新安街道上川路31区A3栋101号（新号104号） : 113.896399,22.573488
深圳市宝安区西乡街道宝田一路臣田新苑5号楼首层4号铺 : 113.877218,22.593971
深圳市宝安区新安街道71区7#9幢首层（创业二路391号） : 113.918575,22.581777
深圳市宝安区新安街道新安大道东南侧深业＊新岸线11栋29 : 113.874742,22.559208
深圳市宝安区松岗街道平安路居乐苑添福楼10-10号铺 : 113.851499,22.767560
深圳市宝安区西乡街道固兴社区固戍一路353号所在楼栋相约网吧101 : 113.860263,22.600903
深圳市宝安区西乡街道铁岗社区南四巷五号-3 : 113.886800,22.600134
深圳市宝安区西乡街道铁岗社区东二巷2号101 : 113.888194,22.599560
深圳市宝安区沙井街道上寮社区三区教师楼105 : 113.815388,22.737115
深圳市宝安区航城街道鹤洲社区鹤洲渔业村工业区4号厂房3号铺 : 113.863362,22.627727
深圳市宝安区福永街道白石厦社区横巷十四巷15号横巷十四巷15-2号 : 113.823061,22.676442
深圳市宝安区西乡街道后瑞社区爱民路20号B栋101 : 113.837466,22.629557
深圳市宝安区松岗街道东方社区蚌岗新区五巷8号101 : 113.851319,22.751399
深圳市宝安区石岩街道石新社区青年西路15号109-201（109A-201A）109A-1、109-2 : 113.925148,22.673219
深圳市宝安区新桥街道万丰社区万丰中路473-2号 : 113.820194,22.707751
深圳市宝安区新安街道新城大道西南侧裕安路东南侧尚都花园2栋105 : 113.886299,22.558612
广东省深圳市福田区福保街道石厦社区石厦西村 105 号 104 : 114.048985,22.519669
深圳市宝安区西乡街道宝源路深圳市名优工业产品展示采购中心一楼Ｂ118、Ｂ119号 : 113.866046,22.567722深圳市宝安区西乡街道宝安大道碧海名园094号商铺之一 : 113.864325,22.581948
深圳市宝安区新安街道宝安20区洪浪北路碧涛居6栋A13号商铺 : 113.914420,22.571938
广东省深圳市宝安区新安街道新乐社区新安一路 20 号金泓凯 旋城 11 栋新安一路 20-52-2 : 113.897103,22.545555
广东省深圳市宝安区福海街道塘尾社区华强城市花园一期3栋D座136 : 113.813914,22.699613
深圳市宝安区福永街道和平社区永和路79-2-2号铺 : 113.792630,22.692398
深圳市宝安区福永街道白石厦社区裕华园西龙州百货楼123 : 113.825940,22.674340
广东省深圳市宝安区福永街道桥头社区桥南新村5号101 : 113.811930,22.691615
深圳市宝安区福海街道新和社区一区富和路6号桥新路36-1号 : 113.798990,22.673900
深圳市宝安区福永街道白石厦社区裕华园西3号裕花园西3-2-2、2单元201 : 113.825467,22.673399
深圳市宝安区新安街道办翻身路富佳苑1栋108 : 113.887957,22.565226
深圳市宝安区新安街道上川路东侧富民苑1栋103－104 : 113.889638,22.569374
深圳市宝安区福海街道桥头社区蚝业路4号4-4 : 113.800361,22.679967
深圳市宝安区新安街道灵芝园社区22区怡园路天河楼怡园路1088号 : 113.900143,22.579287
深圳市宝安区沙井街道共和社区福和路西十二巷1号101 : 113.802753,22.758230
广东省深圳市宝安区石岩街道官田社区吉祥路33号第10栋101 : 113.941102,22.679379
深圳市宝安区新安街道办前进路南侧冠城世家1栋1007 : 113.906299,22.565772
深圳市宝安区新安街道嘉安路与海秀路交汇处熙龙湾花园（N23区）5栋101 : 113.892909,22.545852
深圳市宝安区沙井街道沙井濠景城132号铺位 : 113.790007,22.735676
深圳市宝安区松岗街道红星社区松明大道105号一至三层之一楼右侧A02临街商铺 : 113.832565,22.765399
深圳市宝安区福海街道和平社区玻璃围新村南五巷12号玻璃围新村南五巷12-2号 : 113.794529,22.689969
广东省深圳市宝安区松岗街道松涛社区阳光二街 20 号 101 : 113.845391,22.768918
深圳市宝安区福海街道桥头社区黄屋十一巷3号A101 : 113.803413,22.688309
深圳市宝安区新安街道宝城路34区宝民路鸿景园5栋127号铺 : 113.891784,22.573925
深圳市宝安区福永街道怀德社区广深路福永段77号怀德公元L1-W70商铺 : 113.827113,22.670116
深圳市宝安区新桥街道黄埔社区黄埔南路和盛花园3栋1353－135／1363－136 : 113.844496,22.714512
深圳市宝安区沙井街道华盛新沙荟名庭（二期）第1栋一单元01层64号 : 113.816732,22.733779
深圳市宝安区福永街道怀德社区芳华一区一巷3号福靖苑德丰路86路 : 113.817496,22.669597
深圳市宝安区新安街道罗田路西北侧君逸世家花园1栋B08 : 113.881164,22.560840
深圳市宝安区松岗街道宏发君域花园3栋商铺S113之102-1 : 113.840230,22.777738
深圳市宝安区西乡街道76区丽景城2栋127、128号商铺 : 113.887324,22.588944
广东省深圳市宝安区沙井街道万科翡丽郡花园6栋01层商业100-2 : 113.813753,22.733057
深圳市宝安区西乡街道航城大道北侧领航里程花园4栋108 : 113.856978,22.609136
深圳市宝安区新安街道文雅社区34区华盛盛荟名庭2号楼119 : 113.893356,22.573923
深圳市宝安区西乡街道建安二路西侧富瑰园C栋108 : 113.885042,22.582254
深圳市宝安区西乡街道流塘社区流塘阳光花园1栋143号 : 113.891140,22.581640
深圳市宝安区石岩街道官田社区官田一路1号一层 : 113.941677,22.680332
深圳市宝安区三十一区上川路天源花园一楼第四间铺 : 113.898072,22.576161
深圳市宝安区新安街道勤诚达和园4#楼187、188号商铺 : 113.909090,22.572690
广东省深圳市宝安区松岗街道松涛社区宝利豪庭 001-1 : 113.850856,22.764220
广东省深圳市宝安区沙井街道沙井大街38号 : 113.807145,22.732764
深圳市宝安区新桥街道沙企社区万丰路东侧棕榈堡花园1栋006、005、007、008 : 113.829733,22.719013
深圳市宝安区新桥街道上星社区上星市场1号上星综合市场105 : 113.833100,22.727606
深圳市宝安区新桥街道万丰路万安路244号 : 113.824997,22.727096
深圳市宝安区沙井街道东塘社区新沙路617号101-103 : 113.804503,22.731346
广东省深圳市宝安区松岗街道松岗社区山门路30号天阳大厦106 : 113.844963,22.773504
深圳市宝安区新安街道30区建安新村17栋商铺110号 : 113.895512,22.574112
深圳市宝安区新安街道31区上合路59号 : 113.900503,22.575364
深圳市宝安区新安街道36区公园路上川大厦308Ｃ商铺 : 113.902064,22.579954
深圳市宝安区新安街道新安大道东南侧深业新岸线2栋24 : 113.874531,22.558146
深圳市宝安区石岩街道罗租社区罗租统建楼一巷1号石岩大道45号 : 113.939521,22.674760
深圳市宝安区石岩街道罗租社区佳华豪苑商铺32号 : 113.939299,22.676802
深圳市宝安区石岩街道育德路39号乐万家百货一层、二层（商铺1号铺） : 114.049727,22.697613 '''

matches = re.findall(pattern, text)
# for lon, lat in matches:
#     print(f"经度: {lon}, 纬度: {lat}")
    
csv_filename = "./coordinates.csv"

# 写入 CSV 文件
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Longitude", "Latitude"])  # 写入表头
    writer.writerows(matches)  # 写入数据

print(f"CSV 文件已生成: {csv_filename}")