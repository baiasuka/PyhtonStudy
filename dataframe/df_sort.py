import pandas as pd
import random
import time

t_list = []
for i in range(10):
    t_list.append({"distance": random.randint(0,1000), "exposure": random.randint(0,1)})
df = pd.DataFrame(t_list)
df = df.sort_values(by=["distance", "exposure"], axis=0, ascending=[True, False])
print(df.to_dict(orient='records'))
