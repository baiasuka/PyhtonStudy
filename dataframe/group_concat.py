import pandas as pd

def group_concat():
    """
    DataFrame实现MySQL中group_concat的示例
    :return:
    """
    who_tags = [{"tagId": 1, "name": "双子座", "tip": "你们都是"}, {"tagId": 2, "name": "宅", "tip": "你们都是"},
                {"tagId": 3, "name": "王者荣耀", "tip": "你们都喜欢"}, {"tagId": 4, "name": "二次元", "tip": "你们都喜欢"},
                {"tagId": 7, "name": "程序员", "tip": "你们都是"}]
    which_tags = [{"tagId": 5, "name": "天蝎座", "tip": "你们都是"}, {"tagId": 2, "name": "宅", "tip": "你们都是"},
                  {"tagId": 6, "name": "和平精英", "tip": "你们都喜欢"}, {"tagId": 4, "name": "二次元", "tip": "你们都喜欢"},
                  {"tagId": 7, "name": "程序员", "tip": "你们都是"}]

    df_who = pd.DataFrame(who_tags)
    df_which = pd.DataFrame(which_tags)
    df_which["same"] = True
    # 去除指定列操作
    df_who = df_who.drop(axis=1, columns="tagId")
    df_which = df_which.drop(axis=1, columns="tagId")

    final_df = pd.merge(df_who, df_which, how='left', on=["name", "tip"], left_index=True)
    final_df.fillna(False, inplace=True)
    print(final_df)

    grouped = final_df.groupby("tip")

    def str_concat(data):
        total = '、'.join(data)
        return total

    concated_df = grouped.aggregate({'name': str_concat})
    # 通过索引列取指定行
    result_df = concated_df.loc[concated_df.index=='你们都是']
    print(result_df)
    for i in concated_df.itertuples():
        print(i[0], i[1])

group_concat()