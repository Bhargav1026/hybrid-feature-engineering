import pandas as pd

meta_path = "../../data/esc50/meta/esc50.csv"
df = pd.read_csv(meta_path)
print(df.head())
print("Total clips:", len(df))