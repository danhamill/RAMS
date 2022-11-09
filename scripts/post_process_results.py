import rioxarray
import geopandas as gpd
import xarray as xr
import matplotlib.pyplot as plt
from geocube.api.core import make_geocube

# Output Shapefile 
out = gpd.read_file(r'data\scenario1_single_run2_output\s1_single_run2.shp')
out = out.reset_index()

# Input Terrain
src = rioxarray.open_rasterio(r'data\terrain1_ascii\hc_cp_ascii_5m.asc').rio.clip(
    out.geometry.values, out.crs, from_disk=True
).sel(band=1).drop("band")

# Match the projection of the input terrain and output shapefile
out = out.to_crs(src.rio.crs)

# Convert shapefile to raster with same extents as input raster
out_grid = make_geocube(
    vector_data=out,
    measurements=["Depth"],
    like=src, # ensure the data are on the same grid
)


# Write rasterized shapefile to raster
out_grid.Depth.rio.to_raster(r'output\test3.tif')







