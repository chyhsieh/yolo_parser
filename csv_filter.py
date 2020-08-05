import pandas as pd
import sys

filepath = sys.argv[1]

df = pd.read_csv(filepath)
df = df[df['Object'] == 'person']
#df = df[df['Frame_num']%30 == 0]
#print(df)
output = filepath.split('\\').pop().split('/').pop().rsplit('.', 1)[0]+'_filtered.csv'
df.to_csv(output, index=0)
