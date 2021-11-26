import pandas as pd
from datetime import datetime, timedelta

import random

def df_merge():
    """
    dataframe的连接及连续日期数据的填充
    :return:
    """
    nowdate = datetime.now()
    origin_list = ["知乎", "百度", "今日头条", "朋友", "小红书", "其他"]
    date_list = []
    test_data = []
    for i in range(0, 10):
        nowdate = nowdate - timedelta(days=1)
        t_date = nowdate.strftime('%Y-%m-%d')
        date_list.append(t_date)
        for origin in origin_list:
            p = random.randint(0,10)
            if p > 2:
                test_data.append({"record_date": t_date, "origin": origin, "number": random.randint(10, 100)})
    date_df = pd.DataFrame(date_list, columns=["record_date"])
    t_df = pd.DataFrame(test_data)
    py_df = t_df.loc[t_df["origin"]=='朋友']
    print(py_df)
    final_df = pd.merge(date_df, py_df, how='left', on='record_date', sort='record_date')
    final_df["origin"] = '朋友'
    f_df = final_df.fillna(0)
    print(f_df)

