import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.options import VisualMapOpts
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
from pyecharts.charts import Pie
from pyecharts.charts import WordCloud

df = pd.read_csv("https://oss.xinchanjiao.com/upload/default/20231130-8d7819f8-6acf-44a3-bd4c-03c9a78e75d9.csv")
# 利用pandas读取csv列表
df['new_colum'] = 1
df['订单编号'] = df['订单编号'].astype('int')  # 订单编号等其他列进行格式化
df['收货地址 '] = df['收货地址 '].astype('str')
df['new_colum'] = df['new_colum'].astype('int')
df[['总金额', '买家实际支付金额', '退款金额']] = df[['总金额', '买家实际支付金额', '退款金额']].astype('int')

tuikuan = df['退款金额'].sum()
tuikuan = int(tuikuan)
Total_amount_data = df['买家实际支付金额'].sum()
Total_amount_data = int(Total_amount_data)
zongjin = df['总金额'].sum()
zongjin = int(zongjin)
qita = zongjin - Total_amount_data - tuikuan
bin_data = [('实际支付', Total_amount_data), ('未支付取消订单', qita), ('退款金额',tuikuan)]
shiji = df['买家实际支付金额'].sum()
pie = Pie()
pie.add(series_name="饼状图", data_pair=bin_data)
# 设置全局配置项
pie.set_global_opts(title_opts=opts.TitleOpts(title="支付情况"))
# 设置系列配置项
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# 在浏览器中渲染图表
pie.render("pie_chart.html")
Actual_payment_amount_line_sd = df[df['收货地址 '] == '山东省']
Actual_payment_amount_line_bj = df[df['收货地址 '] == '北京']
Actual_payment_amount_line_tj = df[df['收货地址 '] == '天津']
Actual_payment_amount_line_hb = df[df['收货地址 '] == '河北省']
Actual_payment_amount_line_sxx = df[df['收货地址 '] == '山西省']
Actual_payment_amount_line_hl = df[df['收货地址 '] == '黑龙江省']
Actual_payment_amount_line_jl = df[df['收货地址 '] == '吉林省']
Actual_payment_amount_line_ln = df[df['收货地址 '] == '辽宁省']
Actual_payment_amount_line_zj = df[df['收货地址 '] == '浙江省']
Actual_payment_amount_line_js = df[df['收货地址 '] == '江苏省']
Actual_payment_amount_line_ah = df[df['收货地址 '] == '安徽省']
Actual_payment_amount_line_fj = df[df['收货地址 '] == '福建省']
Actual_payment_amount_line_jx = df[df['收货地址 '] == '江西省']
Actual_payment_amount_line_hn = df[df['收货地址 '] == '河南省']
Actual_payment_amount_line_sc = df[df['收货地址 '] == '四川省']
Actual_payment_amount_line_gz = df[df['收货地址 '] == '贵州省']
Actual_payment_amount_line_yn = df[df['收货地址 '] == '云南省']
Actual_payment_amount_line_sx = df[df['收货地址 '] == '陕西省']
Actual_payment_amount_line_gs = df[df['收货地址 '] == '甘肃省']
Actual_payment_amount_line_qh = df[df['收货地址 '] == '青海省']
Actual_payment_amount_line_nm = df[df['收货地址 '] == '内蒙古自治区']
Actual_payment_amount_line_gx = df[df['收货地址 '] == '广西壮族自治区']
Actual_payment_amount_line_xz = df[df['收货地址 '] == '西藏自治区']
Actual_payment_amount_line_nx = df[df['收货地址 '] == '宁夏回族自治区']
Actual_payment_amount_line_xj = df[df['收货地址 '] == '新疆维吾尔自治区']
Actual_payment_amount_line_sh = df[df['收货地址 '] == '上海']
Actual_payment_amount_line_cq = df[df['收货地址 '] == '重庆']
Actual_payment_amount_line_hub = df[df['收货地址 '] == '湖北省']
Actual_payment_amount_line_hun = df[df['收货地址 '] == '湖南省']
Actual_payment_amount_line_han = df[df['收货地址 '] == '海南省']
Actual_payment_amount_line_gd = df[df['收货地址 '] == '广东省']
new_colum_data_hb = Actual_payment_amount_line_hb['new_colum'].sum()
new_colum_data_sxx = Actual_payment_amount_line_sxx['new_colum'].sum()
new_colum_data_hl = Actual_payment_amount_line_hl['new_colum'].sum()
new_colum_data_jl = Actual_payment_amount_line_jl['new_colum'].sum()
new_colum_data_ln = Actual_payment_amount_line_ln['new_colum'].sum()
new_colum_data_js = Actual_payment_amount_line_js['new_colum'].sum()
new_colum_data_zj = Actual_payment_amount_line_zj['new_colum'].sum()
new_colum_data_ah = Actual_payment_amount_line_ah['new_colum'].sum()
new_colum_data_fj = Actual_payment_amount_line_fj['new_colum'].sum()
new_colum_data_jx = Actual_payment_amount_line_jx['new_colum'].sum()
new_colum_data_sd = Actual_payment_amount_line_sd['new_colum'].sum()
new_colum_data_hn = Actual_payment_amount_line_hn['new_colum'].sum()
new_colum_data_hub = Actual_payment_amount_line_hub['new_colum'].sum()
new_colum_data_hun = Actual_payment_amount_line_hun['new_colum'].sum()
new_colum_data_gd = Actual_payment_amount_line_gd['new_colum'].sum()
new_colum_data_han = Actual_payment_amount_line_han['new_colum'].sum()
new_colum_data_sc = Actual_payment_amount_line_sc['new_colum'].sum()
new_colum_data_gz = Actual_payment_amount_line_gz['new_colum'].sum()
new_colum_data_yn = Actual_payment_amount_line_yn['new_colum'].sum()
new_colum_data_sx = Actual_payment_amount_line_sx['new_colum'].sum()
new_colum_data_gs = Actual_payment_amount_line_gs['new_colum'].sum()
new_colum_data_qh = Actual_payment_amount_line_qh['new_colum'].sum()
new_colum_data_nm = Actual_payment_amount_line_nm['new_colum'].sum()
new_colum_data_gx = Actual_payment_amount_line_gx['new_colum'].sum()
new_colum_data_xz = Actual_payment_amount_line_xz['new_colum'].sum()
new_colum_data_nx = Actual_payment_amount_line_nx['new_colum'].sum()
new_colum_data_xj = Actual_payment_amount_line_xj['new_colum'].sum()
new_colum_data_bj = Actual_payment_amount_line_bj['new_colum'].sum()
new_colum_data_tj = Actual_payment_amount_line_tj['new_colum'].sum()
new_colum_data_sh = Actual_payment_amount_line_sh['new_colum'].sum()
new_colum_data_cq = Actual_payment_amount_line_cq['new_colum'].sum()
Actual_payment_amount_data_hb = Actual_payment_amount_line_hb['买家实际支付金额'].sum()
Actual_payment_amount_data_sxx = Actual_payment_amount_line_sxx['买家实际支付金额'].sum()
Actual_payment_amount_data_hl = Actual_payment_amount_line_hl['买家实际支付金额'].sum()
Actual_payment_amount_data_jl = Actual_payment_amount_line_jl['买家实际支付金额'].sum()
Actual_payment_amount_data_ln = Actual_payment_amount_line_ln['买家实际支付金额'].sum()
Actual_payment_amount_data_js = Actual_payment_amount_line_js['买家实际支付金额'].sum()
Actual_payment_amount_data_zj = Actual_payment_amount_line_zj['买家实际支付金额'].sum()
Actual_payment_amount_data_ah = Actual_payment_amount_line_ah['买家实际支付金额'].sum()
Actual_payment_amount_data_fj = Actual_payment_amount_line_fj['买家实际支付金额'].sum()
Actual_payment_amount_data_jx = Actual_payment_amount_line_jx['买家实际支付金额'].sum()
Actual_payment_amount_data_sd = Actual_payment_amount_line_sd['买家实际支付金额'].sum()
Actual_payment_amount_data_hn = Actual_payment_amount_line_hn['买家实际支付金额'].sum()
Actual_payment_amount_data_hub = Actual_payment_amount_line_hub['买家实际支付金额'].sum()
Actual_payment_amount_data_hun = Actual_payment_amount_line_hun['买家实际支付金额'].sum()
Actual_payment_amount_data_gd = Actual_payment_amount_line_gd['买家实际支付金额'].sum()
Actual_payment_amount_data_han = Actual_payment_amount_line_han['买家实际支付金额'].sum()
Actual_payment_amount_data_sc = Actual_payment_amount_line_sc['买家实际支付金额'].sum()
Actual_payment_amount_data_tj = Actual_payment_amount_line_tj['买家实际支付金额'].sum()
Actual_payment_amount_data_gz = Actual_payment_amount_line_gz['买家实际支付金额'].sum()
Actual_payment_amount_data_yn = Actual_payment_amount_line_yn['买家实际支付金额'].sum()
Actual_payment_amount_data_sx = Actual_payment_amount_line_sx['买家实际支付金额'].sum()
Actual_payment_amount_data_gs = Actual_payment_amount_line_gs['买家实际支付金额'].sum()
Actual_payment_amount_data_qh = Actual_payment_amount_line_qh['买家实际支付金额'].sum()
Actual_payment_amount_data_nm = Actual_payment_amount_line_nm['买家实际支付金额'].sum()
Actual_payment_amount_data_gx = Actual_payment_amount_line_gx['买家实际支付金额'].sum()
Actual_payment_amount_data_xz = Actual_payment_amount_line_xz['买家实际支付金额'].sum()
Actual_payment_amount_data_nx = Actual_payment_amount_line_nx['买家实际支付金额'].sum()
Actual_payment_amount_data_xj = Actual_payment_amount_line_xj['买家实际支付金额'].sum()
Actual_payment_amount_data_bj = Actual_payment_amount_line_bj['买家实际支付金额'].sum()
Actual_payment_amount_data_sh = Actual_payment_amount_line_sh['买家实际支付金额'].sum()
Actual_payment_amount_data_cq = Actual_payment_amount_line_cq['买家实际支付金额'].sum()
Total_amount_hb = Actual_payment_amount_line_hb['总金额'].sum()
Total_amount_sxx = Actual_payment_amount_line_sxx['总金额'].sum()
Total_amount_hl = Actual_payment_amount_line_hl['总金额'].sum()
Total_amount_jl = Actual_payment_amount_line_jl['总金额'].sum()
Total_amount_ln = Actual_payment_amount_line_ln['总金额'].sum()
Total_amount_js = Actual_payment_amount_line_js['总金额'].sum()
Total_amount_zj = Actual_payment_amount_line_zj['总金额'].sum()
Total_amount_ah = Actual_payment_amount_line_ah['总金额'].sum()
Total_amount_fj = Actual_payment_amount_line_fj['总金额'].sum()
Total_amount_jx = Actual_payment_amount_line_jx['总金额'].sum()
Total_amount_sd = Actual_payment_amount_line_sd['总金额'].sum()
Total_amount_hn = Actual_payment_amount_line_hn['总金额'].sum()
Total_amount_hub = Actual_payment_amount_line_hub['总金额'].sum()
Total_amount_hun = Actual_payment_amount_line_hun['总金额'].sum()
Total_amount_gd = Actual_payment_amount_line_gd['总金额'].sum()
Total_amount_han = Actual_payment_amount_line_han['总金额'].sum()
Total_amount_sc = Actual_payment_amount_line_sc['总金额'].sum()
Total_amount_tj = Actual_payment_amount_line_tj['总金额'].sum()
Total_amount_gz = Actual_payment_amount_line_gz['总金额'].sum()
Total_amount_yn = Actual_payment_amount_line_yn['总金额'].sum()
Total_amount_sx = Actual_payment_amount_line_sx['总金额'].sum()
Total_amount_gs = Actual_payment_amount_line_gs['总金额'].sum()
Total_amount_qh = Actual_payment_amount_line_qh['总金额'].sum()
Total_amount_nm = Actual_payment_amount_line_nm['总金额'].sum()
Total_amount_gx = Actual_payment_amount_line_gx['总金额'].sum()
Total_amount_xz = Actual_payment_amount_line_xz['总金额'].sum()
Total_amount_nx = Actual_payment_amount_line_nx['总金额'].sum()
Total_amount_xj = Actual_payment_amount_line_xj['总金额'].sum()
Total_amount_bj = Actual_payment_amount_line_bj['总金额'].sum()
Total_amount_sh = Actual_payment_amount_line_sh['总金额'].sum()
Total_amount_cq = Actual_payment_amount_line_cq['总金额'].sum()
Refund_hb = Actual_payment_amount_line_hb['退款金额'].sum()
Refund_sxx = Actual_payment_amount_line_sxx['退款金额'].sum()
Refund_hl = Actual_payment_amount_line_hl['退款金额'].sum()
Refund_jl = Actual_payment_amount_line_jl['退款金额'].sum()
Refund_ln = Actual_payment_amount_line_ln['退款金额'].sum()
Refund_js = Actual_payment_amount_line_js['退款金额'].sum()
Refund_zj = Actual_payment_amount_line_zj['退款金额'].sum()
Refund_ah = Actual_payment_amount_line_ah['退款金额'].sum()
Refund_fj = Actual_payment_amount_line_fj['退款金额'].sum()
Refund_jx = Actual_payment_amount_line_jx['退款金额'].sum()
Refund_sd = Actual_payment_amount_line_sd['退款金额'].sum()
Refund_hn = Actual_payment_amount_line_hn['退款金额'].sum()
Refund_hub = Actual_payment_amount_line_hub['退款金额'].sum()
Refund_hun = Actual_payment_amount_line_hun['退款金额'].sum()
Refund_gd = Actual_payment_amount_line_gd['退款金额'].sum()
Refund_han = Actual_payment_amount_line_han['退款金额'].sum()
Refund_sc = Actual_payment_amount_line_sc['退款金额'].sum()
Refund_tj = Actual_payment_amount_line_tj['退款金额'].sum()
Refund_gz = Actual_payment_amount_line_gz['退款金额'].sum()
Refund_yn = Actual_payment_amount_line_yn['退款金额'].sum()
Refund_sx = Actual_payment_amount_line_sx['退款金额'].sum()
Refund_gs = Actual_payment_amount_line_gs['退款金额'].sum()
Refund_qh = Actual_payment_amount_line_qh['退款金额'].sum()
Refund_nm = Actual_payment_amount_line_nm['退款金额'].sum()
Refund_gx = Actual_payment_amount_line_gx['退款金额'].sum()
Refund_xz = Actual_payment_amount_line_xz['退款金额'].sum()
Refund_nx = Actual_payment_amount_line_nx['退款金额'].sum()
Refund_xj = Actual_payment_amount_line_xj['退款金额'].sum()
Refund_bj = Actual_payment_amount_line_bj['退款金额'].sum()
Refund_sh = Actual_payment_amount_line_sh['退款金额'].sum()
Refund_cq = Actual_payment_amount_line_cq['退款金额'].sum()
Actual_payment_amount_data_hb = int(Actual_payment_amount_data_hb)
Actual_payment_amount_data_sxx = int(Actual_payment_amount_data_sxx)
Actual_payment_amount_data_hl = int(Actual_payment_amount_data_hl)
Actual_payment_amount_data_jl = int(Actual_payment_amount_data_jl)
Actual_payment_amount_data_ln = int(Actual_payment_amount_data_ln)
Actual_payment_amount_data_js = int(Actual_payment_amount_data_js)
Actual_payment_amount_data_zj = int(Actual_payment_amount_data_zj)
Actual_payment_amount_data_ah = int(Actual_payment_amount_data_ah)
Actual_payment_amount_data_fj = int(Actual_payment_amount_data_fj)
Actual_payment_amount_data_jx = int(Actual_payment_amount_data_jx)
Actual_payment_amount_data_sd = int(Actual_payment_amount_data_sd)
Actual_payment_amount_data_hn = int(Actual_payment_amount_data_hn)
Actual_payment_amount_data_hub = int(Actual_payment_amount_data_hub)
Actual_payment_amount_data_hun = int(Actual_payment_amount_data_hun)
Actual_payment_amount_data_gd = int(Actual_payment_amount_data_gd)
Actual_payment_amount_data_han = int(Actual_payment_amount_data_han)
Actual_payment_amount_data_sc = int(Actual_payment_amount_data_sc)
Actual_payment_amount_data_gz = int(Actual_payment_amount_data_gz)
Actual_payment_amount_data_yn = int(Actual_payment_amount_data_yn)
Actual_payment_amount_data_sx = int(Actual_payment_amount_data_sx)
Actual_payment_amount_data_gs = int(Actual_payment_amount_data_gs)
Actual_payment_amount_data_qh = int(Actual_payment_amount_data_qh)
Actual_payment_amount_data_nm = int(Actual_payment_amount_data_nm)
Actual_payment_amount_data_gx = int(Actual_payment_amount_data_gx)
Actual_payment_amount_data_xz = int(Actual_payment_amount_data_xz)
Actual_payment_amount_data_nx = int(Actual_payment_amount_data_nx)
Actual_payment_amount_data_xj = int(Actual_payment_amount_data_xj)
Actual_payment_amount_data_bj = int(Actual_payment_amount_data_bj)
Actual_payment_amount_data_sh = int(Actual_payment_amount_data_sh)
Actual_payment_amount_data_cq = int(Actual_payment_amount_data_cq)
Actual_payment_amount_data_tj = int(Actual_payment_amount_data_tj)
Total_amount_hb = int(Total_amount_hb)
Total_amount_sxx = int(Total_amount_sxx)
Total_amount_hl = int(Total_amount_hl)
Total_amount_jl = int(Total_amount_jl)
Total_amount_ln = int(Total_amount_ln)
Total_amount_js = int(Total_amount_js)
Total_amount_zj = int(Total_amount_zj)
Total_amount_ah = int(Total_amount_ah)
Total_amount_fj = int(Total_amount_fj)
Total_amount_jx = int(Total_amount_jx)
Total_amount_sd = int(Total_amount_sd)
Total_amount_hn = int(Total_amount_hn)
Total_amount_hub = int(Total_amount_hub)
Total_amount_hun = int(Total_amount_hun)
Total_amount_gd = int(Total_amount_gd)
Total_amount_han = int(Total_amount_han)
Total_amount_sc = int(Total_amount_sc)
Total_amount_gz = int(Total_amount_gz)
Total_amount_yn = int(Total_amount_yn)
Total_amount_sx = int(Total_amount_sx)
Total_amount_gs = int(Total_amount_gs)
Total_amount_qh = int(Total_amount_qh)
Total_amount_nm = int(Total_amount_nm)
Total_amount_gx = int(Total_amount_gx)
Total_amount_xz = int(Total_amount_xz)
Total_amount_nx = int(Total_amount_nx)
Total_amount_xj = int(Total_amount_xj)
Total_amount_bj = int(Total_amount_bj)
Total_amount_sh = int(Total_amount_sh)
Total_amount_cq = int(Total_amount_cq)
Total_amount_tj = int(Total_amount_tj)
Refund_hb = int(Refund_hb)
Refund_sxx = int(Refund_sxx)
Refund_hl = int(Refund_hl)
Refund_jl = int(Refund_jl)
Refund_ln = int(Refund_ln)
Refund_js = int(Refund_js)
Refund_zj = int(Refund_zj)
Refund_ah = int(Refund_ah)
Refund_fj = int(Refund_fj)
Refund_jx = int(Refund_jx)
Refund_sd = int(Refund_sd)
Refund_hn = int(Refund_hn)
Refund_hub = int(Refund_hub)
Refund_hun = int(Refund_hun)
Refund_gd = int(Refund_gd)
Refund_han = int(Refund_han)
Refund_sc = int(Refund_sc)
Refund_gz = int(Refund_gz)
Refund_yn = int(Refund_yn)
Refund_sx = int(Refund_sx)
Refund_gs = int(Refund_gs)
Refund_qh = int(Refund_qh)
Refund_nm = int(Refund_nm)
Refund_gx = int(Refund_gx)
Refund_xz = int(Refund_xz)
Refund_nx = int(Refund_nx)
Refund_xj = int(Refund_xj)
Refund_bj = int(Refund_bj)
Refund_sh = int(Refund_sh)
Refund_cq = int(Refund_cq)
Refund_tj = int(Refund_tj)
new_colum_data_hb = int(new_colum_data_hb)
new_colum_data_sxx = int(new_colum_data_sxx)
new_colum_data_hl = int(new_colum_data_hl)
new_colum_data_jl = int(new_colum_data_jl)
new_colum_data_ln = int(new_colum_data_ln)
new_colum_data_js = int(new_colum_data_js)
new_colum_data_zj = int(new_colum_data_zj)
new_colum_data_ah = int(new_colum_data_ah)
new_colum_data_fj = int(new_colum_data_fj)
new_colum_data_jx = int(new_colum_data_jx)
new_colum_data_sd = int(new_colum_data_sd)
new_colum_data_hn = int(new_colum_data_hn)
new_colum_data_hub = int(new_colum_data_hub)
new_colum_data_hun = int(new_colum_data_hun)
new_colum_data_gd = int(new_colum_data_gd)
new_colum_data_han = int(new_colum_data_han)
new_colum_data_sc = int(new_colum_data_sc)
new_colum_data_gz = int(new_colum_data_gz)
new_colum_data_yn = int(new_colum_data_yn)
new_colum_data_sx = int(new_colum_data_sx)
new_colum_data_gs = int(new_colum_data_gs)
new_colum_data_qh = int(new_colum_data_qh)
new_colum_data_nm = int(new_colum_data_nm)
new_colum_data_gx = int(new_colum_data_gx)
new_colum_data_xz = int(new_colum_data_xz)
new_colum_data_nx = int(new_colum_data_nx)
new_colum_data_xj = int(new_colum_data_xj)
new_colum_data_bj = int(new_colum_data_bj)
new_colum_data_sh = int(new_colum_data_sh)
new_colum_data_cq = int(new_colum_data_cq)
new_colum_data_tj = int(new_colum_data_tj)
print(df['new_colum'].dtype)
map_Total_amount = Map(init_opts=opts.InitOpts(width="2000px", height="800px"))
map_Total_amount2 = Map(init_opts=opts.InitOpts(width="2000px", height="800px"))

data = [
    ("山东省", Actual_payment_amount_data_sd),
    ("北京市", Actual_payment_amount_data_bj),
    ("重庆市", Actual_payment_amount_data_cq),
    ("天津市", Actual_payment_amount_data_tj),
    ("河北省", Actual_payment_amount_data_hb),
    ("上海市", Actual_payment_amount_data_sh),
    ("河南省", Actual_payment_amount_data_hn),
    ("湖北省", Actual_payment_amount_data_hub),
    ("湖南省", Actual_payment_amount_data_hun),
    ("海南省", Actual_payment_amount_data_han),
    ("山西省", Actual_payment_amount_data_sx),
    ("浙江省", Actual_payment_amount_data_zj),
    ("广西壮族自治区", Actual_payment_amount_data_gx),
    ("新疆维吾尔自治区", Actual_payment_amount_data_xj),
    ("西藏自治区", Actual_payment_amount_data_xz),
    ("黑龙江省", Actual_payment_amount_data_hl),
    ("江苏省", Actual_payment_amount_data_js),
    ("福建省", Actual_payment_amount_data_fj),
    ("宁夏回族自治区", Actual_payment_amount_data_nx),
    ("甘肃省", Actual_payment_amount_data_gs),
    ("云南省", Actual_payment_amount_data_yn),
    ("贵州省", Actual_payment_amount_data_gz),
    ("陕西省", Actual_payment_amount_data_sx),
    ("吉林省", Actual_payment_amount_data_jl),
    ("辽宁省", Actual_payment_amount_data_ln),
    ("江西省", Actual_payment_amount_data_jx),
    ("四川省", Actual_payment_amount_data_sc),
    ("内蒙古自治区", Actual_payment_amount_data_nm),
    ("广东省", Actual_payment_amount_data_gd),
    ("重庆市", Actual_payment_amount_data_cq),
    ("青海省", Actual_payment_amount_data_qh),
    ("安徽省", Actual_payment_amount_data_ah),
]
data2 = [
    ("山东省", Total_amount_sd),
    ("北京市", Total_amount_bj),
    ("重庆市", Total_amount_cq),
    ("天津市", Total_amount_tj),
    ("河北省", Total_amount_hb),
    ("上海市", Total_amount_sh),
    ("河南省", Total_amount_hn),
    ("湖北省", Total_amount_hub),
    ("湖南省", Total_amount_hun),
    ("海南省", Total_amount_han),
    ("山西省", Total_amount_sx),
    ("浙江省", Total_amount_zj),
    ("广西壮族自治区", Total_amount_gx),
    ("新疆维吾尔自治区", Total_amount_xj),
    ("西藏自治区", Total_amount_xz),
    ("黑龙江省", Total_amount_hl),
    ("江苏省", Total_amount_js),
    ("福建省", Total_amount_fj),
    ("宁夏回族自治区", Total_amount_nx),
    ("甘肃省", Total_amount_gs),
    ("云南省", Total_amount_yn),
    ("贵州省", Total_amount_gz),
    ("陕西省", Total_amount_sx),
    ("吉林省", Total_amount_jl),
    ("辽宁省", Total_amount_ln),
    ("江西省", Total_amount_jx),
    ("四川省", Total_amount_sc),
    ("内蒙古自治区", Total_amount_nm),
    ("广东省", Total_amount_gd),
    ("重庆市", Total_amount_cq),
    ("青海省", Total_amount_qh),
    ("安徽省", Total_amount_ah),
]
data3 = [
    ("山东省", Refund_sd),
    ("北京市", Refund_bj),
    ("重庆市", Refund_cq),
    ("天津市", Refund_tj),
    ("河北省", Refund_hb),
    ("上海市", Refund_sh),
    ("河南省", Refund_hn),
    ("湖北省", Refund_hub),
    ("湖南省", Refund_hun),
    ("海南省", Refund_han),
    ("山西省", Refund_sx),
    ("浙江省", Refund_zj),
    ("广西壮族自治区", Refund_gx),
    ("新疆维吾尔自治区", Refund_xj),
    ("西藏自治区", Refund_xz),
    ("黑龙江省", Refund_hl),
    ("江苏省", Refund_js),
    ("福建省", Refund_fj),
    ("宁夏回族自治区", Refund_nx),
    ("甘肃省", Refund_gs),
    ("云南省", Refund_yn),
    ("贵州省", Refund_gz),
    ("陕西省", Refund_sx),
    ("吉林省", Refund_jl),
    ("辽宁省", Refund_ln),
    ("江西省", Refund_jx),
    ("四川省", Refund_sc),
    ("内蒙古自治区", Refund_nm),
    ("广东省", Refund_gd),
    ("重庆市", Refund_cq),
    ("青海省", Refund_qh),
    ("安徽省", Refund_ah),
]
data4 = [
    ("山东省", new_colum_data_sd),
    ("北京市", new_colum_data_bj),
    ("重庆市", new_colum_data_cq),
    ("天津市", new_colum_data_tj),
    ("河北省", new_colum_data_hb),
    ("上海市", new_colum_data_sh),
    ("河南省", new_colum_data_hn),
    ("湖北省", new_colum_data_hub),
    ("湖南省", new_colum_data_hun),
    ("海南省", new_colum_data_han),
    ("山西省", new_colum_data_sx),
    ("浙江省", new_colum_data_zj),
    ("广西壮族自治区", new_colum_data_gx),
    ("新疆维吾尔自治区", new_colum_data_xj),
    ("西藏自治区", new_colum_data_xz),
    ("黑龙江省", new_colum_data_hl),
    ("江苏省", new_colum_data_js),
    ("福建省", new_colum_data_fj),
    ("宁夏回族自治区", new_colum_data_nx),
    ("甘肃省", new_colum_data_gs),
    ("云南省", new_colum_data_yn),
    ("贵州省", new_colum_data_gz),
    ("陕西省", new_colum_data_sx),
    ("吉林省", new_colum_data_jl),
    ("辽宁省", new_colum_data_ln),
    ("江西省", new_colum_data_jx),
    ("四川省", new_colum_data_sc),
    ("内蒙古自治区", new_colum_data_nm),
    ("广东省", new_colum_data_gd),
    ("重庆市", new_colum_data_cq),
    ("青海省", new_colum_data_qh),
    ("安徽省", new_colum_data_ah),
]
map_Total_amount.add("天猫各省买家实际支付金额", data, "china", zoom=1)
map_Total_amount.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 1999, "label": "1~1999", "color": "#CCFFFF"},
            {"min": 2000, "max": 4999, "label": "2000~4999", "color": "#FFFF99"},
            {"min": 5000, "max": 9999, "label": "5000~9999", "color": "#FF9966"},
            {"min": 10000, "max": 49999, "label": "10000~49999", "color": "#FF6666"},
            {"min": 50000, "max": 99999, "label": "50000~99999", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    )
)
# map_Total_amount.render()
'''

map_Total_amount2.add("天猫各省买家总金额", data2, "china", zoom=1)
map_Total_amount2.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 1999, "label": "1~1999", "color": "#CCFFFF"},
            {"min": 2000, "max": 4999, "label": "2000~4999", "color": "#FFFF99"},
            {"min": 5000, "max": 9999, "label": "5000~9999", "color": "#FF9966"},
            {"min": 10000, "max": 49999, "label": "10000~49999", "color": "#FF6666"},
            {"min": 50000, "max": 99999, "label": "50000~99999", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    )
)
'''
bar = Bar(init_opts=opts.InitOpts(width="2000px", height="800px"))
bar.add_xaxis(
    ["山东省", "北京市", "天津市", "河北省", "山西省", "黑龙江省", "吉林省", "辽宁省", "浙江省", "江苏省", "安徽省",
     "福建省", "江西省", "河南省", "四川省", "贵州省", "云南省", "陕西省", "甘肃省", "青海省", "内蒙古自治区",
     "广西壮族自治区", "西藏自治区", "宁夏回族自治区", "新疆维吾尔自治区", "上海", "重庆", "湖北省", "湖南省", "海南省",
     "广东省"])
bar.add_yaxis("退款总金额", [Refund_sd, Refund_bj, Refund_tj, Refund_hb, Refund_sxx, Refund_hl, Refund_jl, Refund_ln,
                             Refund_zj, Refund_js, Refund_ah, Refund_fj, Refund_jx, Refund_hn, Refund_sc, Refund_gz,
                             Refund_yn, Refund_sx, Refund_gs, Refund_qh, Refund_nm, Refund_gx, Refund_xz, Refund_nx,
                             Refund_xj, Refund_sh, Refund_cq, Refund_hub, Refund_hun, Refund_han, Refund_gd],
              label_opts=LabelOpts(position="right")
              )
# 绘图
bar.render("各省退款金额.html")

print(new_colum_data_zj)
wc = WordCloud()
wc.add('下单省份词云图', data4, word_size_range=[16, 80], shape='triangle')
wc.render('词云图.html')
