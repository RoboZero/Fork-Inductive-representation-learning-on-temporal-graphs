import pandas as pd

chunksize = 1 # ** 8
filename = "processed/reddit.csv"

# with pd.read_csv(filename, header=0, nrows=1) as reader:
#     print(reader)
#     for chunk in reader:
#         print(chunk)

df_header = pd.read_csv(filename, header=0, nrows=1).columns.tolist()
print(df_header)

df = pd.read_csv(filename, nrows=1)
print(df.head(1))