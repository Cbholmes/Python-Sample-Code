import pandas as pd
import plotly.express as plt
from datetime import datetime

df = pd.read_csv("https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_24h.csv")
ftimes = []
for i in df["acq_time"]:
    cur=str(i)
    if len(cur) < 4:
        for j in range(4-len(cur)):
            cur = "0" + cur
    ftimes.append(datetime.strptime(cur, "%H%M").strftime("%I:%M %p"))
df["ftime"] = ftimes
fig = plt.scatter_geo(df, "latitude", "longitude",
                      color="brightness", hover_name="ftime",
                      title="Fires in the last 24 Hours")
fig.show()
