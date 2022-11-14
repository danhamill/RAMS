# RAMS

Clone Repo Or [download](https://github.com/danhamill/RAMS/archive/refs/heads/master.zip)

```
cd c:\workspace
git clone https://github.com/danhamill/RAMS.git
cd RAMS
```

Create Conda enviromennt

```
conda create -n RAMS -f environment.yml
````

Activate RAMS

```
conda activate RAMS
```

Edit script for inputs and output file names

Input Raster 
https://github.com/danhamill/RAMS/blob/5e3751125795e00e6d2223ecb3c56b4db8fd0f18/scripts/post_process_results.py#L12

Input shapefile
https://github.com/danhamill/RAMS/blob/5e3751125795e00e6d2223ecb3c56b4db8fd0f18/scripts/post_process_results.py#L8

Shapefile field to rasterize
https://github.com/danhamill/RAMS/blob/5e3751125795e00e6d2223ecb3c56b4db8fd0f18/scripts/post_process_results.py#L20

Output Depth Raster
https://github.com/danhamill/RAMS/blob/5e3751125795e00e6d2223ecb3c56b4db8fd0f18/scripts/post_process_results.py#L25

Update Terrain with depths
https://github.com/danhamill/RAMS/blob/5e3751125795e00e6d2223ecb3c56b4db8fd0f18/scripts/post_process_results.py#L27-L30

Output Updated Terrain
https://github.com/danhamill/RAMS/blob/5e3751125795e00e6d2223ecb3c56b4db8fd0f18/scripts/post_process_results.py#L33

```
RAMS/scripts/post_process_results.py
```

Run Script to get outputs!
