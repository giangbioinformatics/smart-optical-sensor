from smartsensor.base import (
    end2end_model,
)
import os

# params
# Summary: The data is CuSO4 focus which means the camera is focus on the CuSO4 solution to capture the image
data_path = "EDA/Fe3+"
indir = f"{data_path}/raw_data"
test_size = 1
batches = ["batch1", "batch2", "batch3"]

# without filter
process_outdir = f"{data_path}/process_data_not_filter"
# DELTA
raw_res = []
process_type = "delta_normalized_roi"
prefix = "delta_roi"
# Stable
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = (
    f"{data_path}/result_without_filter_and_feature_selection_3_batches_get_fomula"
)
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw_data
train_rgb_path = f"{indir_e2e}/RGB_values.csv"
train_concentrations = [f"{indir}/{b}.csv" for b in batches]
# test
test_rgb_path = None
test_concentrations = []
metric, detail = end2end_model(
    train_rgb_path,
    train_concentrations,
    test_rgb_path,
    test_concentrations,
    features,
    degree,
    outdir,
    prefix,
    test_size=test_size,
    random_state=None,
)
