import pandas as pd

df = pd.read_pickle('model_item.pkl');

print(df.query('作品名 == "男の子の育て方"')["Unnamed: 0"])


