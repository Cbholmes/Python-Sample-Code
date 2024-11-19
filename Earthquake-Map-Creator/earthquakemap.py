import geopandas as gpd
import plotly.express as plot
from datetime import datetime
import urllib.request as url
import json

"""
File name: earthquakemap.py
Module creates an earthquake map
"""

class EarthquakeMap():
    """Object to represent an Earthquake plot map"""
    def __init__(self, geojsonurl):
        """Constructor creates map with points plotted to show earthquake data 
        based off a geojson from https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"""
        self._geojson=geojsonurl
        self._dataframe=self._createDataFrame()
        self._figure=self._createFigure()

    def _createDataFrame(self):
        """Constructor helper creates a geopandas dataframe to be used for plotting map"""
        
        #converts the geojson to a geopandas dataframe
        df = gpd.read_file(self._geojson)
        
        #creates formatted date and time lists with the time column of the dataframe
        ftimes, fdates = [], []
        for i in df["time"]:
            date = datetime.fromtimestamp(i/1000)
            ftimes.append(date.strftime("%I:%M:%S %p"))
            fdates.append(date.strftime("%B %d, %Y"))
        
        #creates a list of plot point sizes converted from the 
        #magnitude of the point proportionally to a scale from 1-6
        psizes = []
        magdiff = max(df["mag"]) - min(df["mag"])
        sizediff = 5
        for i in df["mag"]:
            psizes.append((i - min(df["mag"])) * sizediff / magdiff + 1)
        
        #adds new columns to the data frame with formatted dates and times and the point sizes
        df["ftime"] = ftimes
        df["fdate"] = fdates
        df["psize"] = psizes
        return df
    
    def _createFigure(self):
        """Constructor helper creates a world map with earthquake data using dataframe"""
       
       #gets the metadata section of the geojson to get the title of the map plot
        with url.urlopen(self._geojson) as f:
            title = json.load(f)["metadata"]["title"]
        
        #creates a scatter plot on top of a map using the dataframe that contains earthquake data
        fig = plot.scatter_geo(self._dataframe, lat=self._dataframe.geometry.y, lon=self._dataframe.geometry.x,
                       color="fdate", size="psize",
                       custom_data=["title","mag","ftime"], title=title)
        
        #sets a custom template for what users see when they hover over points of the map
        fig.update_traces(hovertemplate="<br>".join(["<b>%{customdata[0]}</b><br>",
                                                    "Latitude: %{lat}",
                                                    "Longitude: %{lon}",
                                                    "Magnitude: %{customdata[1]}",
                                                    "Time: %{customdata[2]}"]))
        return fig
    
    def showMap(self):
        self._figure.show()
