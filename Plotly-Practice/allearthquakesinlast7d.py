import geopandas as gpd
import plotly.express as plot
from datetime import datetime

earthquakes = gpd.read_file("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson")

ftimes, fdates = [], []
for i in earthquakes["time"]:
    ftimes.append(datetime.fromtimestamp(i/1000.0).strftime("%I:%M:%S %p"))
    fdates.append(datetime.fromtimestamp(i/1000.0).strftime("%B %d, %Y"))
earthquakes["time"] = ftimes
earthquakes["date"] = fdates

pointsizes = []
for i in earthquakes["mag"]:
    pointsizes.append(i+2)
earthquakes["psize"] = pointsizes

fig = plot.scatter_geo(earthquakes,
                       lat=earthquakes.geometry.y, lon=earthquakes.geometry.x,
                       color="date", color_continuous_scale="turbid_r", size="psize",
                       custom_data=["title","mag","time"],
                       title="All Earthquakes in the Past Week")

fig.update_traces(hovertemplate="<br>".join(["<b>%{customdata[0]}</b><br>",
                                             "Latitude: %{lat}",
                                             "Longitude: %{lon}",
                                             "Magnitude: %{customdata[1]}",
                                             "Time: %{customdata[2]}"]))
fig.show()
