from smartsensor.base import processing_images
import numpy as np

# Example
# Feature
data_path = "EDA/Fe3+"
indir = f"{data_path}/raw_data"
outdir = f"{data_path}/process_data"
process_outdir = f"{data_path}/process_data_not_filter"
processing_images(
    indir=indir,
    outdir=process_outdir,
    threshold=[(40, 70, 20), (80, 120, 50)],
    constant=[100, 145, 40],
    bg_index=[-80, -20, 340, -340],
    roi_index=175,
    overwrite=True,
    threshold_stdev=np.inf,
    threshold_ratio=np.inf,
    threshold_delta=np.inf,
)
