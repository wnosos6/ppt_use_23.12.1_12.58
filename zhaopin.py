import matplotlib.font_manager
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pyecharts.charts import Pie
from pyecharts import options as opts

font = matplotlib.font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf",
                                              size=12)  # 字体设置，matplotlib生成的图像不能正常显示文字，这里调用一下windows自带的字体文件
df = pd.read_excel("F:\\BaiduSyncdisk\\其他类型文件\\招聘数据-市场营销-2000条.xlsx", sheet_name=0)  # 利用pandas读取文件
fen_com_name = df.groupby("职位名称").size().sort_values(
    ascending=False)  # 用groupby分组，size统计，sort_values排序import pandas
# 公司规模和所属行业这两列数据需要交换
df['公司规模'], df['所属行业'] = df['所属行业'], df['公司规模']
# 按照“学历”进行分类，统计各个学历的人数
df['学历'] = df['学历'].str.replace('  |  ', '')
fen_xue_li = df.groupby("学历").size().sort_values(ascending=False)
df['工资'] = df['工资'].str.replace('以上', '')
df['工资'] = df['工资'].str.replace('k', '')
df['工资'] = df['工资'].str.replace('K', '')
df['工资去k'] = df['工资'].apply(lambda xa: xa if '-' in xa else '50-' + xa)
df[['最低期望工资', '最高期望工资']] = df['工资去k'].str.split('-', expand=True)
df['最低期望工资'] = df['最低期望工资'].astype(float)*1000
df['最高期望工资'] = df['最高期望工资'].astype(float)*1000
# 按照工作经历分类，统计各个工作经历的人数
df['工作经验'] = df['工作经验'].str.replace('  |  ', '')
fen_gong_zuo_jin_li = df.groupby("工作经验").size().sort_values(ascending=False)
# 将除排前十一的公司外的公司合并为“其他”，再合并在一起
top_labels = fen_com_name.index.tolist()[:10]
top_values = fen_com_name.values.tolist()[:10]
other_values = sum(fen_com_name.values.tolist()[10:])
top_labels.append('其他')
top_values.append(other_values)

# 按照城市分类，统计各个城市的人数
df['城市名'] = df['地区'].str[:3]
fen_chen_name = df.groupby("城市名").size().sort_values(ascending=False)
fen_chen_gao = df.groupby('城市名')['最高期望工资'].mean()
fen_chen_di = df.groupby('城市名')['最低期望工资'].mean()

print(fen_chen_name)
print(fen_xue_li)
print(fen_gong_zuo_jin_li)
print(fen_com_name)
print(fen_chen_di)
print(fen_chen_gao)

plt.figure(figsize=(10, 5))
cities = fen_chen_gao.index
x = np.arange(len(cities))
width = 0.35
plt.bar(x - width / 2, fen_chen_gao, width, label='最高期望工资')
plt.bar(x + width / 2, fen_chen_di, width, label='最低期望工资')
plt.legend(prop=font)
plt.xticks(ticks=x, labels=cities, rotation=45, fontproperties=font)
plt.ylabel('工资', fontproperties=font)
plt.title('按城市分类的最低期望工资和最高期望工资', fontproperties=font)
plt.show()
# 用pyecharts绘制关于职务的饼状图
pie = Pie()
pie.add("", [list(z) for z in zip(top_labels, top_values)])
pie.set_global_opts(title_opts=opts.TitleOpts(title='职务名称占比', pos_left='center'),
                    legend_opts=opts.LegendOpts(pos_right='right'))
pie.render("pie_chart.html")

plt.figure(figsize=(10, 5))
cities = fen_chen_name.index
x = np.arange(len(cities))
plt.bar(x, fen_chen_name, width=0.35)
plt.xticks(ticks=x, labels=cities, rotation=45, fontproperties=font)
plt.ylabel('数量', fontproperties=font)
plt.title('按城市分类的公司数', fontproperties=font)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(fen_xue_li.index, fen_xue_li, width=0.35)
plt.xticks(rotation=45, fontproperties=font)
plt.ylabel('数量', fontproperties=font)
plt.title('不同公司需要的学历', fontproperties=font)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(fen_gong_zuo_jin_li.index, fen_gong_zuo_jin_li, width=0.35)
plt.xticks(rotation=45, fontproperties=font)
plt.ylabel('数量', fontproperties=font)
plt.title('企业需要的不同工作经历的人数', fontproperties=font)
plt.show()
