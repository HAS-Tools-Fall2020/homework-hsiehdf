# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import geopandas as gpd
import fiona
import os
from shapely.geometry import Point
import contextily as ctx

# %%

# Use these links to download the files used for this code:
# Gages: https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder
# Rivers and Watersheds: http://uair.library.arizona.edu/item/292543/browse-data/Water?page=1
# HUC 4: https://www.sciencebase.gov/catalog/item/5a96cda0e4b06990606c4d0f 

file = os.path.join('data-nongit', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)
gages_AZ=gages[gages['STATE']=='AZ']

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
usgs_sg =np.array([[-111.7891667, 34.44833333]])
Verde_end = np.array([[-111.660554, 33.547297]])
Phoenix = np.array([[-112.0740,33.4484]])

# Making into spatial features
Verde_beg_geom = [Point(xy) for xy in Verde_beg]
usgs_sg_geom =[Point(xy) for xy in usgs_sg]
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

# Something to think about, why did making crs= HUC4 first then
# Changing it to gages_AZ work but trying to start with gages_AZ
# did not? Not starting in the right CRS I guess?

#reproject onto map
Verde_beg_point= Verde_beg_df.to_crs(gages_AZ.crs)
usgs_sg_point= usgs_sg_df.to_crs(gages_AZ.crs)
Verde_end_point= Verde_end_df.to_crs(gages_AZ.crs)
Phoenix_point= Phoenix_df.to_crs(gages_AZ.crs)

# Plotting all the layers together
fig, ax = plt.subplots(figsize=(5, 5))
major_rivers_project.plot(ax=ax, zorder=3, label="Major Rivers")
Verde_beg_point.plot(ax=ax, color='purple', marker='^', zorder=5,
    label="Verde River Start")
usgs_sg_point.plot(ax=ax, color='red', marker ='o', zorder=5,
    label="USGS SG")
Verde_end_point.plot(ax=ax, color='black', marker = "x", zorder=5,
    label="Verde River End")
Phoenix_point.plot(ax=ax, color='c', marker = "P", zorder=5,
    label="Phoenix, AZ")
Watersheds_project.boundary.plot(ax=ax, color=None, edgecolor='black', linewidth=.75,
   label="Watershed Boundaries", zorder=1)
ax.set_title("Verde River Watershed")
ax.set(ylim=[1.2e6, 1.6e6], xlim=[-1.6e6, -1.3e6])
ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
ax.set_xlabel('Easting (m)')
ax.set_ylabel('Northing (m)')
ctx.add_basemap(ax, url=ctx.providers.OpenTopoMap, crs=gages_AZ.crs)
plt.savefig("Verde_River_Watershed.png")
plt.show()


#%%
