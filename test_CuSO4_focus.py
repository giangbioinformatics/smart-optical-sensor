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
data_path = "EDA/CUSO4"
indir = f"{data_path}/raw_data"

test_size = 0.3
batches = ["batch1", "batch2", "batch3"]

# Processing images
# without filter
process_outdir = f"{data_path}/process_data_test"
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
# QUESTION: DOES THE NORMALIZATION AFFECT THE RESULT?
# question: does the background affect the result ?
# 1. 3 batches, 3 process types, 3 models not filter and feature selection
# RAW
raw_res = []
process_type = "raw_roi"
prefix = "raw_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = f"{data_path}/result_without_filter_and_feature_selection"
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentration = f"{indir}/{batch}.csv"
    # test
    test_rgb_path = None
    test_concentration = None
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
    raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(f"{outdir_e2e}/result_raw.csv", index=False)

# DELTA
raw_res = []
process_type = "delta_normalized_roi"
prefix = "delta_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = f"{data_path}/result_without_filter_and_feature_selection"
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentration = f"{indir}/{batch}.csv"
    # test
    test_rgb_path = None
    test_concentration = None
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
    raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(f"{outdir_e2e}/result_delta.csv", index=False)

# RATIO
raw_res = []
process_type = "ratio_normalized_roi"
prefix = "ratio_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = f"{data_path}/result_without_filter_and_feature_selection"
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentration = f"{indir}/{batch}.csv"
    # test
    test_rgb_path = None
    test_concentration = None
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
    raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(f"{outdir_e2e}/result_ratio.csv", index=False)

# 2. Combine 3 batches into one models. Using one batch for train, test on the other 2 batches
# RAW
raw_res = []
process_type = "raw_roi"
prefix = "raw_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = (
    f"{data_path}/result_without_filter_and_feature_selection_iterate_each_batches"
)
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentration = f"{indir}/{batch}.csv"
    # test
    remain_batches = [x for x in batches if x != batch]
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    for remain_batch in remain_batches:
        print(f"Testing on batch {remain_batch}")
        test_concentration = f"{indir}/{remain_batch}.csv"
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
        raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_raw_iterate_each_batches.csv", index=False
)
# DELTA
raw_res = []
process_type = "delta_normalized_roi"
prefix = "delta_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = (
    f"{data_path}/result_without_filter_and_feature_selection_iterate_each_batches"
)
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentration = f"{indir}/{batch}.csv"
    # test
    remain_batches = [x for x in batches if x != batch]
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    for remain_batch in remain_batches:
        print(f"Testing on batch {remain_batch}")
        test_concentration = f"{indir}/{remain_batch}.csv"
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
        raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_delta_iterate_each_batches.csv", index=False
)

# RATIO
raw_res = []
process_type = "ratio_normalized_roi"
prefix = "ratio_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = (
    f"{data_path}/result_without_filter_and_feature_selection_iterate_each_batches"
)
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentration = f"{indir}/{batch}.csv"
    # test
    remain_batches = [x for x in batches if x != batch]
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    for remain_batch in remain_batches:
        print(f"Testing on batch {remain_batch}")
        test_concentration = f"{indir}/{remain_batch}.csv"
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
        raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_ratio_iterate_each_batches.csv", index=False
)
# Integrate the result
metrics = glob.glob(f"{outdir_e2e}/*iterate_each_batches.csv")
sum_stats = []
for m in metrics:
    stats = pd.read_csv(m).describe().reset_index().rename(columns={"index": "metric"})
    stats["process_type"] = m.split("/")[-1].split(".")[0].split("_")[1]
    sum_stats.append(stats)
pd.concat(sum_stats).sort_values("metric").to_csv(
    f"{outdir_e2e}/sum_stats.csv", index=False
)
