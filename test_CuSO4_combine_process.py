from smartsensor.base import (
    processing_images,
)
import numpy as np

# params
# Summary: The data is CuSO4 focus which means the camera is focus on the CuSO4 solution to capture the image
data_path = "EDA/CuSO4_combine"
indir = f"{data_path}/raw_data"
batches = ["batch1", "batch2", "batch3", "batch4", "batch5"]

# Processing images
# without filter
process_outdir = f"{data_path}/process_data_not_filter"
processing_images(
    indir=indir,
    outdir=process_outdir,
    threshold=[(0, 120, 0), (150, 230, 80)],
    constant=[100, 145, 40],
    overwrite=True,
    threshold_stdev=np.inf,
    threshold_ratio=np.inf,
    threshold_delta=np.inf,
)
# with filter
# process_outdir = f"{data_path}/process_data_filter"
# processing_images(
#     indir=indir,
#     outdir=process_outdir,
#     threshold=[(0, 120, 0), (150, 230, 80)],
#     constant=[100, 145, 40],
#     overwrite=True,
#     threshold_stdev=4,
#     threshold_ratio=1,  # fold change (FC)=2
#     threshold_delta=20,
# )
