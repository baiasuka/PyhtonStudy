import random
import pandas as pd
from datetime import datetime

#
# 产生数据
tag_str = "萌萌哒、女汉子、强迫症、拖延症、吃货、逗比、双重人格、简单生活、敢爱敢恨、选择恐惧症、密集事物恐惧症、宅、文艺、靠谱、厚道、讲义气、AJ控、女友永远是对的、大叔控、马甲线、长发及腰、安静、" \
          "健谈、随性、叛逆、热血、理想主义、小鲜肉、爱哭、追风少年、乐观主义、泡吧、奋斗、隔壁老王、技术宅、细节控、声控、足控、二次元、腹肌、爱运动、旅行达人、高玩、程序员、程序媛、爱吃辣、甜品控、" \
          "伪娘、有趣的灵魂、高冷、爱唱歌、小仙女、攻气十足、伪郎、爱摄影、学生党、95后、90后、大叔、肥宅、高富帅、白富美、幽默、眼镜、短发控、嘻哈、反差萌、宅舞达人、偶像宅、爱画画、爱购物、剁手党"

tag_list = tag_str.split('、')
# user_list = ["洪文俊", "侯需要", "何海超", "潘生铎", "吕明明", "童凯", "张志星", "邓玉", "金超群"]
user_list = ["洪文俊", "侯需要", "何海超", "潘生铎", "吕明明", "童凯", "张志星", "邓玉", "金超群",
             "张科", "李晗宁", "励俞翔", "余梦磊", "王明明", "何志强", "林家宝", "何继超",
             "张飞", "刘备", "关羽", "曹操", "孙权", "孙策", "孙坚", "曹丕",
             "黄忠", "赵云", "马超", "魏延", "张辽", "夏侯渊", "典韦", "夏侯淳"]
data = []
user_index = []
for user in user_list:
    random_indexs = random.sample(tag_list, random.randint(5,10))
    for i in random_indexs:
        exposure = random.randint(0,1)
        data.append((user, i))
        if user == '洪文俊':
            user_index.append(i)
start = datetime.now()
df = pd.DataFrame(data, columns=["user", "tag"])
user_group = df.groupby(["user"])
print(user_group)
for item in user_group:
    print(item)
df["value"] = 1

# 行转列
r_df = df.pivot(index="user", columns="tag", values="value").fillna(0)
n_df = r_df.loc[:,user_index]
n_df["score"] = 0
user_row = n_df.loc["洪文俊"]
result_dict = {}
for i in n_df.index.values:
    if i != '洪文俊':
        n_df.loc[i] = n_df.loc[i] + user_row
    result = n_df.loc[i].value_counts()
    score = result.get(2) or 0
    n_df.loc[i]["score"] = score
    result_dict[i] = score
# result = n_df[["index", "score"]].to_dict(orient="record")
end = datetime.now()
print(result_dict)
print('用时:', str(end-start))