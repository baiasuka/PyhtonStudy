import random
import pandas as pd

raw_data = []
for i in range(0, 90):
    distance = random.randint(0, 10000)
    face_score = random.randint(0,5)
    raw_data.append({"id": i, "distance": distance, "face_score": face_score})

df = pd.DataFrame(raw_data)

max_distance = df["distance"].max()
min_distance = df["distance"].min()
print(max_distance)
print(min_distance)
differ = max_distance - min_distance
df["score"] = 1 - (df["distance"] - min_distance)/differ + df["face_score"]*df["face_score"]/10
df = df.sort_index(axis=0, ascending=False, by='score')
result = df.to_dict(orient="record")
print(result)
