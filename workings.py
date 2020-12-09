
# load data - take a look...
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gpxpy
import os
# activities file for summary stats
df = pd.read_csv('data/Activities.csv')
df.head(2)
df.shape
# gpx files for gps tracking
gpx_dict = {
    'lat':[],
    'lon':[],
    'elev':[],
    'time':[],
    'temp':[]
}

directory = 'data'
for filename in os.listdir(directory):
    if filename.endswith(".gpx"):
        #print(os.path.join(directory, filename))
        gpx_f=open(os.path.join(directory, filename),'r')
        gpx = gpxpy.parse(gpx_f)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    gpx_dict['lat'].append(point.latitude)
                    gpx_dict['lon'].append(point.longitude)
                    gpx_dict['elev'].append(point.elevation)
                    gpx_dict['time'].append(point.time)
                    for extension in point.extensions:
                        for child in extension.getchildren():
                            gpx_dict['temp'].append(child.text)

    else:
        continue
# takes a little while to load
gpx_df = pd.DataFrame(gpx_dict)
gpx_df.head(2)
gpx_df.shape
type(gpx_df.time[0])
gpx_df.describe()
gpx_df.info()
df.info()
df.columns
cols = ['Date','Title','Distance','Calories','Time','Avg Speed','Max Speed','Elev Gain','Elev Loss','Climb Time','Min Temp','Best Lap Time','Number of Laps']
df[cols].head(2)
lap_df = df[cols]
lap_df.info()
