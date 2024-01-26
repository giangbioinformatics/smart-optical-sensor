from smartsensor.base import processing_images, end2end_model
import os
import math

# Example
# Feature
data_path = "EDA/Fe3+"
indir = f"{data_path}/raw_data"
outdir = f"{data_path}/process_data"
processing_images(
    indir=indir,
    outdir=outdir,
    constant=[100, 150, 40],
    overwrite=True,
    threshold_stdev=5,
    threshold_ratio=math.log(1.2, 2),
    threshold_delta=15,
)


def process_data_and_model(data_path, process_type, train_batch, test_batch, outdir):
    train_rgb_path = f"{data_path}/process_data/{process_type}/RGB_values.csv"
    test_rgb_path = f"{data_path}/process_data/{process_type}/RGB_values.csv"
    train_concentration = f"{data_path}/raw_data/{train_batch}.csv"
    test_concentration = f"{data_path}/raw_data/{test_batch}.csv"
    features = "meanR,meanG,meanB,modeR,modeB,modeG"
    degree = 1
    prefix = "demo"
    outdir = os.path.join(outdir, process_type)
    os.makedirs(outdir, exist_ok=True)
    metric, detail = end2end_model(
        train_rgb_path,
        train_concentration,
        test_rgb_path,
        test_concentration,
        features,
        degree,
        outdir,
        prefix,
    )


# 0. Model raw data
# Standard value
outdir = f"{data_path}/result"
for test_batch in ["batch2", "batch3"]:
    process_data_and_model(data_path, "raw_roi", "batch1", test_batch, outdir)

# 1. Model ratio_normalized_roi
for test_batch in ["batch2", "batch3"]:
    process_data_and_model(
        data_path, "ratio_normalized_roi", "batch1", test_batch, outdir
    )

# 2. Model delta_normalized_roi
for test_batch in ["batch2", "batch3"]:
    process_data_and_model(
        data_path, "delta_normalized_roi", "batch1", test_batch, outdir
    )
# UVis value
# 0. Raw
outdir = f"{data_path}/result"
for test_batch in ["uv_batch2", "uv_batch3"]:
    process_data_and_model(data_path, "raw_roi", "uv_batch1", test_batch, outdir)

# 1. Model ratio_normalized_roi
for test_batch in ["uv_batch2", "uv_batch3"]:
    process_data_and_model(
        data_path, "ratio_normalized_roi", "uv_batch1", test_batch, outdir
    )

# 2. Model delta_normalized_roi
for test_batch in ["uv_batch2", "uv_batch3"]:
    process_data_and_model(
        data_path, "delta_normalized_roi", "uv_batch1", test_batch, outdir
    )
