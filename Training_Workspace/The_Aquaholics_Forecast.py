# Team Forecast: The Aquaholics
# Members: Diana, Danielle, Xenia and Camilo
# November 2020

# %%
import pandas as pd
import matplotlib.pyplot as plt
import os
import teamfns as tf
import seaborn as sn
from PIL import Image
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
import contextily as ctx

# %% Data retrieval of streamflows from USGS

# URL Variables
site = '09506000'
start = '2009-03-02'  # Adjusted according to information availability
end = '2020-11-14'
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" +\
       site + "&referred_module=sw&period=&begin_date=" + start + "&end_date="\
       + end

stream_data = pd.read_table(url, skiprows=30,
                            names=['agency_cd', 'site_no',
                                   'datetime', 'flow', 'code'],
                            parse_dates=['datetime'], index_col='datetime')

stream_data.index = stream_data.index.strftime('%Y-%m-%d')
stream_data = stream_data.set_index(pd.to_datetime(stream_data.index))


# %%
# Weekly Forecast - Week 11

# Common dataframe for both forecasts including only the flow column
daily_flow = stream_data[['flow']]
daily_flow = daily_flow.set_index(pd.to_datetime(stream_data.index))
weekly_flow_plot = stream_data[['flow']].resample('W-SUN').mean().round(2)

# Two-week forecast

# Training period for the AR Model
start_train_date = '2009-10-01'
end_train_date = '2009-11-30'

# Forecasting period
start_for_date = '2020-11-15'
end_for_date = '2020-11-29'

# Used parameters for the model
# Number of shifts
time_shifts = 3

# Function Call
flow_daily_2w, flow_weekly_2w, model_intercept, model_coefficients = \
    tf.forecast_flows(daily_flow, time_shifts, start_train_date,
                      end_train_date, start_for_date, end_for_date, 'week')

# %%
# Seasonal Forecast for weeks between Aug. 22 to Oct. 31

# Training period for the AR Model for first 6 weeks
start_train_date = '2019-08-25'
end_train_date = '2019-11-10'

# Forecasting period for first 6 weeks
start_for_date = '2020-08-22'
end_for_date = '2020-10-31'

# Number of shifts
time_shifts = 3

# Common dataframe for both forecasts including only the flow column
daily_flow_16w = stream_data.loc['1989-01-01':start_for_date][['flow']]

# Function Call
flow_daily_seas, flow_weekly_seas, model_intercept16, model_coefficients16 = \
    tf.forecast_flows(daily_flow_16w, time_shifts, start_train_date,
                      end_train_date, start_for_date, end_for_date, 'seasonal')
# %%
# Seasonal Forecast for weeks between Nov. 01 to Dec. 12
# NOTE: I did not use the outputs printed by the model to make the forecasts.\
# Rather, I used the model determined by the function.

# Training period for the AR Model for first 6 weeks
start_train_date = '2009-10-01'
end_train_date = '2009-11-30'

# Forecasting period for first 6 weeks
start_for_date = '2020-11-01'
end_for_date = '2020-12-12'

# Number of shifts
time_shifts = 3

# Common dataframe for both forecasts including only the flow column
daily_flow_16w = flow_daily_seas.loc['1989-01-01':start_for_date][['flow']]

# Function Call
flow_daily_seas, flow_weekly_seas, model_intercept16, model_coefficients16 = \
    tf.forecast_flows(daily_flow_16w, time_shifts, start_train_date,
                      end_train_date, start_for_date, end_for_date, 'seasonal')

# %%
# Making PLOTS with Mesowest and USGS Data
end_date = '202011070000'

# Calling the function to get Precipitation and Temperature data from Mesowest
data_Meso, data_Meso_D, data_Meso_W = tf.prec_temp_data(end_date)

# Printing my dataframe to know it
data_Meso_D

# %%
# Plots with Temperature & Precipitation
fig, ax = plt.subplots()
ax.plot(weekly_flow_plot['flow'], label='Streamflow', color='black',
        linewidth=0.5)
ax.plot(data_Meso_W['Precipitation'], 'r:', label='Precipitation',
        color='aqua', linestyle='-', alpha=1, linewidth=0.7)
ax.plot(data_Meso_W['Temperature'], 'r:', label='Temperature',
        color='mediumorchid', linestyle='-', alpha=1, linewidth=0.5)
ax.set(title="Data", xlabel="Date", ylabel="Weekly Avg values",
       yscale='log')

ax.legend()
fig.set_size_inches(7, 5)
fig.savefig("Data.png")

# %%
# Adding timezone = UTC to the flow data, to join the Mesowest data after
daily_flow.index = daily_flow.index.tz_localize(tz="UTC")
weekly_flow_plot.index = weekly_flow_plot.index.tz_localize(tz="UTC")

# Concatenate a single dataframe with all the time series
union = pd.concat([weekly_flow_plot[['flow']], data_Meso_W[['Temperature']],
                   data_Meso_W[['Precipitation']]], axis=1)

# %%
# Correlation Plot
corrMatrix = union.corr()
sn.heatmap(corrMatrix, annot=True, vmin=-1, vmax=1, center=0, cmap='PRGn')
plt.title("Correlation_Matrix")
plt.show()
fig.set_size_inches(7, 5)
plt.savefig("Correlation_Matrix.png")

# %%

# Code for the image, NOTE: Please see the last line of code to display the
# image if you do not want to download everything below.
# Gages:
# - https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder
# Rivers and Watersheds:
# - http://uair.library.arizona.edu/item/292543/browse-data/Water?page=1
# HUC 4:
# - https://www.sciencebase.gov/catalog/item/5a96cda0e4b06990606c4d0f

file = os.path.join('data-nongit', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)
gages_AZ = gages[gages['STATE'] == 'AZ']

file2 = os.path.join('data-nongit', 'Major Rivers.shp')
major_rivers = gpd.read_file(file2)
major_rivers_project = major_rivers.to_crs(gages_AZ.crs)

file3 = os.path.join('data-nongit', 'Watersheds.shp')
Watersheds = gpd.read_file(file3)
Watersheds_project = Watersheds.to_crs(gages_AZ.crs)

file4 = os.path.join('data-nongit', 'NHD_H_Arizona_State_GDB.gdb')
HUC4 = gpd.read_file(file4, layer="WBDHU4")

# Adding in some points of interest: Stream gauge location and
# beginning of Verde River (34.864282, -112.442660) and end of Verde River
# (33.547297, -111.660554)

Verde_beg = np.array([[-112.45172, 34.8559]])
usgs_sg = np.array([[-111.7891667, 34.44833333]])
Verde_end = np.array([[-111.660554, 33.547297]])
Phoenix = np.array([[-112.0740, 33.4484]])

# Making into spatial features
Verde_beg_geom = [Point(xy) for xy in Verde_beg]
usgs_sg_geom = [Point(xy) for xy in usgs_sg]
Verde_end_geom = [Point(xy) for xy in Verde_end]
Phoenix_geom = [Point(xy) for xy in Phoenix]

# Making into a dataframe
Verde_beg_df = gpd.GeoDataFrame(Verde_beg_geom, columns=['geometry'],
                                crs=HUC4.crs)
usgs_sg_df = gpd.GeoDataFrame(usgs_sg_geom, columns=['geometry'],
                              crs=HUC4.crs)
Verde_end_df = gpd.GeoDataFrame(Verde_end_geom, columns=['geometry'],
                                crs=HUC4.crs)
Phoenix_df = gpd.GeoDataFrame(Phoenix_geom, columns=['geometry'],
                              crs=HUC4.crs)

# Reproject onto map
Verde_beg_point = Verde_beg_df.to_crs(gages_AZ.crs)
usgs_sg_point = usgs_sg_df.to_crs(gages_AZ.crs)
Verde_end_point = Verde_end_df.to_crs(gages_AZ.crs)
Phoenix_point = Phoenix_df.to_crs(gages_AZ.crs)

# Plotting all the layers together
fig, ax = plt.subplots(figsize=(5, 5))
major_rivers_project.plot(ax=ax, zorder=3, label="Major Rivers")
Verde_beg_point.plot(ax=ax, color='purple', marker='^', zorder=5,
                     label="Verde River Start")
usgs_sg_point.plot(ax=ax, color='red', marker='o', zorder=5,
                   label="USGS SG")
Verde_end_point.plot(ax=ax, color='black', marker="x", zorder=5,
                     label="Verde River End")
Phoenix_point.plot(ax=ax, color='c', marker="P", zorder=5,
                   label="Phoenix, AZ")
Watersheds_project.boundary.plot(ax=ax, color=None, edgecolor='black',
                                 linewidth=.75, label="Watershed Boundaries",
                                 zorder=1)
ax.set_title("Verde River Watershed")
ax.set(ylim=[1.2e6, 1.6e6], xlim=[-1.6e6, -1.3e6])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel('Easting (m)')
ax.set_ylabel('Northing (m)')
ctx.add_basemap(ax, url=ctx.providers.OpenTopoMap, crs=gages_AZ.crs)
plt.savefig("Verde_River_Watershed.png")
plt.show()

# %%
# This is to display the image you will get if you download the data
# above and run the code.

im = Image.open("assets/Verde_River_Watershed.png")
im.show()

# %%
