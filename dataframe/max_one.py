# 用于获取每组最大值记录所在行
from pandas import DataFrame

a=[('Li','男','PE',98.),
   ('Li','男','MATH',60.),
   ('liu','女','MATH',75.),
   ('liu','男','PH',75.),
   ('liu','男','CS',100.),
   ('liu','女','PE',100.),
   ('Zhang','女','PE',55.),
   ('Zhang','女','MATH',99.)]
af=DataFrame(a,columns=['name','sex','course','score'])
print(af.to_dict(orient='record'))
result = af[af.groupby(['name','sex'])['score'].rank(method="first", ascending=True)==1]
print(result.to_dict(orient='record'))
print(af)