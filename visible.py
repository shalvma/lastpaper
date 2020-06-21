from pyecharts.charts import Bar
import xlrd
import math
import numpy as np
import matplotlib.pyplot as plt

#提取excel中的数据并进行整理
data = xlrd.open_workbook('LOL数据.xlsx')
table = data.sheets()[0]
kills = 0
deaths = 0
assists = 0
gold = 0
damage = 0
team = 0
for i in range(1, table.nrows):
    kills += int(table.row_values(i)[1])
    deaths += int(table.row_values(i)[2])
    assists += int(table.row_values(i)[3])
    gold += int(table.row_values(i)[7])
    damage += int(table.row_values(i)[4])
    team += int(table.row_values(i)[5]+table.row_values(i)[6])
kda = math.ceil((kills + assists)/deaths*10)
damage = math.ceil(damage/8000)
gold = math.ceil(gold/5000*1.5)
survive = math.ceil(deaths)
team = math.ceil(team)

#准备画布
labels = np.array(['团战', '发育', '输出', 'KDA', '生存'])
dataLenth = 5
data = np.array([team, gold, damage, kda, survive])
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, polar=True)

# 画若干个五边形
floor = np.floor(data.min())     # 大于最小值的最大整数
ceil = np.ceil(data.max())       # 小于最大值的最小整数

for i in np.arange(floor, ceil + 2, 2):
    ax.plot(angles, [i] * (int(len(labels)) + 1), '-', lw=0.3, color='black')

# 设置背景坐标系
ax.spines['polar'].set_visible(False)  # 不显示极坐标最外圈的圆
ax.grid(False)  # 不显示默认的分割线
ax.set_yticks([])  # 不显示坐标间隔
ax.plot(angles, data, 'ro-', linewidth=2)
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
# 填充
ax.set_title("LOL战绩", va='bottom', fontproperties="SimHei")
ax.grid(True)
plt.show()
