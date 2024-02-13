from smartsensor.base import (
    processing_images,
    end2end_model,
)
import glob
import os
import pandas as pd
import numpy as np

# params
# Summary: The data is CuSO4 focus which means the camera is focus on the CuSO4 solution to capture the image
data_path = "EDA/120223_CuSO4_not_focus"
indir = f"{data_path}/raw_data"

test_size = 0.3
batches = ["batch1", "batch2", "batch3"]

# Processing images
# without filter
process_outdir = f"{data_path}/process_data_not_filter"
processing_images(
    indir=indir,
    outdir=process_outdir,
    constant=[100, 145, 40],
    bg_index=[20, 80, 80, -80],
    overwrite=True,
    threshold_stdev=np.inf,
    threshold_ratio=np.inf,
    threshold_delta=np.inf,
)
