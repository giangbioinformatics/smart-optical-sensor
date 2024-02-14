from smartsensor.base import (
    end2end_model,
    processing_images,
)
import glob
import os
import pandas as pd
import numpy as np
import subprocess

# params
# Summary: The data is CuSO4 focus which means the camera is focus on the CuSO4 solution to capture the image
data_path = "EDA/CuSO4_combine"
indir = f"{data_path}/raw_data"
batches = ["batch1", "batch2", "batch3"]

# without filter
process_outdir = f"{data_path}/process_data_not_filter"
# subprocess.call(f"rm -rf {process_outdir}", shell=True)
# processing_images(
#     indir=indir,
#     outdir=process_outdir,
#     # threshold=[(0, 120, 0), (150, 230, 80)],
#     # constant=[100, 145, 40],
#     # bg_index=[30, 80, 345, -345],
#     # roi_index=245,
#     overwrite=True,
#     threshold_stdev=np.inf,
#     threshold_ratio=np.inf,
#     threshold_delta=np.inf,
# )


subprocess.call(
    f"rm -rf {data_path}/result_without_filter_and_feature_selection_4_batches_train_1_batch_test",
    shell=True,
)
# QUESTION: DOES THE NORMALIZATION AFFECT THE RESULT?
# 1. Combine 3 batches into one models. Using train test split for each dataset and each concentration. Due to random
# split #noqa
# RAW
# Change here
raw_res = []
process_type = "raw_roi"
prefix = "raw_roi"
# Stable
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = f"{data_path}/result_without_filter_and_feature_selection_4_batches_train_1_batch_test"
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# repeat here
train_rgb_path = f"{indir_e2e}/RGB_values.csv"
for batch in batches:
    train_concentrations = [f"{indir}/{b}.csv" for b in batches if b != batch]
    # test
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    test_concentrations = [f"{indir}/{batch}.csv"]
    metric, detail = end2end_model(
        train_rgb_path,
        train_concentrations,
        test_rgb_path,
        test_concentrations,
        features,
        degree,
        outdir,
        prefix,
        random_state=None,
    )
    metric = metric[metric["train_data"] != metric["test_data"]]
    raw_res.append(metric)
# Change here
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_raw_4_batches_train_1_batch_test.csv", index=False
)
# DELTA
raw_res = []
process_type = "delta_normalized_roi"
prefix = "delta_roi"
# Stable
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = f"{data_path}/result_without_filter_and_feature_selection_4_batches_train_1_batch_test"
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# repeat here
for batch in batches:
    train_concentrations = [f"{indir}/{b}.csv" for b in batches if b != batch]
    # test
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    test_concentrations = [f"{indir}/{batch}.csv"]
    metric, detail = end2end_model(
        train_rgb_path,
        train_concentrations,
        test_rgb_path,
        test_concentrations,
        features,
        degree,
        outdir,
        prefix,
        random_state=None,
    )
    metric = metric[metric["train_data"] != metric["test_data"]]
    raw_res.append(metric)
# Change here
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_delta_4_batches_train_1_batch_test.csv", index=False
)

# RATIO
raw_res = []
process_type = "ratio_normalized_roi"
prefix = "ratio_roi"
# Stable
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = f"{data_path}/result_without_filter_and_feature_selection_4_batches_train_1_batch_test"
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# repeat here
for batch in batches:
    train_concentrations = [f"{indir}/{b}.csv" for b in batches if b != batch]
    # test
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    test_concentrations = [f"{indir}/{batch}.csv"]
    metric, detail = end2end_model(
        train_rgb_path,
        train_concentrations,
        test_rgb_path,
        test_concentrations,
        features,
        degree,
        outdir,
        prefix,
        random_state=None,
    )
    metric = metric[metric["train_data"] != metric["test_data"]]
    raw_res.append(metric)
# Change here
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_ratio_4_batches_train_1_batch_test.csv", index=False
)
# Integrate the result
metrics = glob.glob(f"{outdir_e2e}/*4_batches_train_1_batch_test.csv")
sum_stats = []
for m in metrics:
    prepare_stat = pd.read_csv(m)
    # only capture the test dataset
    prepare_stat = prepare_stat[prepare_stat["train_data"] != prepare_stat["test_data"]]
    stats = prepare_stat.describe().reset_index().rename(columns={"index": "metric"})
    stats["process_type"] = m.split("/")[-1].split(".")[0].split("_")[1]
    sum_stats.append(stats)
    prepare_export = pd.concat(sum_stats).sort_values("metric")
    export = prepare_export[
        prepare_export["metric"].isin(["mean", "min", "max", "std"])
    ].reset_index(drop=True)
    export.to_csv(f"{outdir_e2e}/sum_stats.csv", index=False)

print(export[export["metric"] == "mean"])
