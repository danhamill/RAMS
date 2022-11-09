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
https://github.com/danhamill/RAMS/blob/13b75427ca582d0e762c3bedda8d5a54e09aa5af/scripts/post_process_results.py#L12

Input shapefile
https://github.com/danhamill/RAMS/blob/13b75427ca582d0e762c3bedda8d5a54e09aa5af/scripts/post_process_results.py#L8

Shapefile field to rasterize
https://github.com/danhamill/RAMS/blob/13b75427ca582d0e762c3bedda8d5a54e09aa5af/scripts/post_process_results.py#L22

Output Raster Name
https://github.com/danhamill/RAMS/blob/13b75427ca582d0e762c3bedda8d5a54e09aa5af/scripts/post_process_results.py#L28

```
RAMS/scripts/post_process_results.py
```

Run Script to get outputs!
