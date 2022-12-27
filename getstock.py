#coding=utf-8

# 导入tushare
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('f8da47455f2426a2b184f3e2fa0d2b4716639f8ee20f89ff966463ce')

# 拉取数据
df = pro.daily(**{
    "ts_code": "000001.sz",
    "trade_date": 20221227,
    "start_date": "",
    "end_date": "",
    "offset": "",
    "limit": ""
}, fields=[
    "ts_code",
    "trade_date",
    "open",
    "high",
    "low",
    "close",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount"
])
print(df)