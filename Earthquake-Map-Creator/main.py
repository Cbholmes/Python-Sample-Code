from earthquakemap import EarthquakeMap as eqm

"""
File name: main.py
Driver code, uses earthquakemap class and geojsons containing 
earthquake data from the USGS website to plot a map based on user input.
"""

#Hyper links to earthquake data for the last hour
pasthoureqs = ["https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson",
               "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson",
               "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson",
               "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson",
               "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson"]

#Hyper links to earthquake data for the last day
pastdayeqs = ["https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson",
              "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson",
              "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson",
              "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson",
              "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson"]

#Hyper links to earthquake data for the last week
pastweekeqs = ["https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
               "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson",
               "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson",
               "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson",
               "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson"]

#Hyper links to earthquake data for the last month
pastmontheqs = ["https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson",
                "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson",
                "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson",
                "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson",
                "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"]

#contains lists of data of each time period
earthquakes = [pasthoureqs, pastdayeqs, pastweekeqs, pastmontheqs]
def main():
    
    print("This program creates a map of earthquake data and opens a webpage to display the map.")
    #loop until told to not generate another map at the end.
    while True:
        #Lists potential timeframes
        print("1. Past 60 Minutes")
        print("2. Past 24 Hours")
        print("3. Past 7 Days")
        print("4. Past 30 Days")
        
        #asks user to select a timeframe to plot/loop until a number from 1 to 4 is entered
        while True:
            tf = input("Choose a time frame for the map (1-4): ")
            if tf.isdecimal() and int(tf) <= 4 and int(tf) >= 1:
                break
            print("Error: Value out of range.")
        print()
        #Lists potential magnitude ranges
        print("1. All earthquakes")
        print("2. Magnitude 1.0+ earthquakes")
        print("3. Magnitude 2.5+ earthquakes")
        print("4. Magnitude 4.5+ earthquakes")
        print("5. Significant earthquakes")
        
        #asks user to select the mininum magnitude that will be plotted/loop until a number from 1 to 5 is entered
        while True:
            mr = input("Choose which earthquakes will be shown (1-5): ")
            if mr.isdecimal() and int(mr) <= 5 and int(mr) >= 1:
                break
            print("Error: Value out of range.")
        print("Generating Map")
        
        #Obtains list of urls from selected time frame then gets the url that matches the selected minimum magnitude
        tfused = earthquakes[int(tf)-1]
        eqgeojson = tfused[int(mr)-1]
        
        #creates and plots a map with earthquake data
        fig = eqm(eqgeojson)
        fig.showMap()
        
        #if user doesn't say yes, exit the program
        if input("Would you like to generate another map?(y/N): ").lower() != 'y':
            break
        
        

if __name__ == "__main__":
    main()
