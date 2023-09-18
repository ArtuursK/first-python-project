import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('iot_telemetry_data.csv')

#print(datetime.fromtimestamp(df['ts']))
#df['ts'] = df['ts'].apply(lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
df['ts'] = pd.to_datetime(df['ts']).dt.strftime('%Y-%m-%d %H:%M:%S')

plt.plot(df['ts'], df['temp'])

plt.show()