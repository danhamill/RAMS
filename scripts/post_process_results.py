import rioxarray
import geopandas as gpd
import xarray as xr
import matplotlib.pyplot as plt
from geocube.api.core import make_geocube
import re

# Output Shapefile 
out = gpd.read_file(r'data\dfp_output_shp\s1_single_run2.shp')
out = out.reset_index()

# Input Terrain
src = rioxarray.open_rasterio(r'data\ascii\ascii_5m_nad83_utm_zone10n.asc').squeeze()

# Match the projection of the input terrain and output shapefile
out = out.to_crs(src.rio.crs)

# Convert shapefile to raster with same extents as input raster
out_grid = make_geocube(
    vector_data=out,
    measurements=["Depth"],
    like=src, # ensure the data are on the same grid
)

# Write rasterized shapefile to raster
out_grid.Depth.rio.to_raster(r'output\depth_raster.tif')

# This assumes positive depths are accumulation and negative depths are errosion
dod = src + out_grid.Depth
dod = dod.combine_first(src)
dod = dod.fillna(-9999.0)
dod = dod.rio.write_nodata(-9999.0)

outputFileName = r'output\updated_terrain3.asc'
# Write new terrain to raster
dod.rio.to_raster(outputFileName)

with open(outputFileName,'r+') as f:
    modified = re.sub('^.','',f.read(),flags=re.MULTILINE)
    f.seek(0,0)
    f.write(modified)






