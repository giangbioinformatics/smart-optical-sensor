from smartsensor.base import (
    end2end_model,
)
import glob
import os
import pandas as pd

# params
# Summary: The data is CuSO4 focus which means the camera is focus on the CuSO4 solution to capture the image
data_path = "EDA/120223_CuSO4_not_focus"
indir = f"{data_path}/raw_data"

test_size = 0.3
batches = ["batch1", "batch2", "batch3"]

# Processing images
# without filter
process_outdir = f"{data_path}/process_data_not_filter"
# QUESTION: DOES THE NORMALIZATION AFFECT THE RESULT?
# 1. Combine 3 batches into one models. Using randomly 2 batches for train, the remaining batch for testing
# RAW
batches = ["batch1", "batch2", "batch3"]
raw_res = []
process_type = "raw_roi"
prefix = "raw_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = f"{data_path}/result_without_filter_and_feature_selection_iterate_2_batches_train_1_batch_test"
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    # raw_data
    train_batches = [b for b in batches if b != batch]
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentrations = [f"{indir}/{b}.csv" for b in train_batches]
    # test
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    print(f"Testing on batch {batch}")
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
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    # raw_data
    train_batches = [b for b in batches if b != batch]
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentrations = [f"{indir}/{b}.csv" for b in train_batches]
    # test
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    print(f"Testing on batch {batch}")
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
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    # raw_data
    train_batches = [b for b in batches if b != batch]
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentrations = [f"{indir}/{b}.csv" for b in train_batches]
    # test
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    print(f"Testing on batch {batch}")
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
    )
    raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_ratio_iterate_each_batches.csv", index=False
)
# Integrate the result
metrics = glob.glob(f"{outdir_e2e}/*iterate_each_batches.csv")
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


# 1. Combine 3 batches into one models. Using randomly 2 batches for train, the remaining batch for testing
# RAW
batches = [["batch12", "batch3"], ["batch23", "batch1"], ["batch31", "batch2"]]
raw_res = []
process_type = "raw_roi"
prefix = "raw_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = f"{data_path}/result_without_filter_and_feature_selection_iterate_2_batches_train_1_batch_test"
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch[0]}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentrations = [f"{indir}/{batch[0]}.csv"]
    # test
    remain_batch = batch[1]
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    print(f"Testing on batch {remain_batch}")
    test_concentrations = [f"{indir}/{remain_batch}.csv"]
    metric, detail = end2end_model(
        train_rgb_path,
        train_concentrations,
        test_rgb_path,
        test_concentrations,
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
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch[0]}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentrations = [f"{indir}/{batch[0]}.csv"]
    # test
    remain_batch = batch[1]
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    print(f"Testing on batch {remain_batch}")
    test_concentrations = [f"{indir}/{remain_batch}.csv"]
    metric, detail = end2end_model(
        train_rgb_path,
        train_concentrations,
        test_rgb_path,
        test_concentrations,
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
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
for batch in batches:
    print(f"Processing batch {batch[0]}")
    # raw_data
    train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    train_concentrations = [f"{indir}/{batch[0]}.csv"]
    # test
    remain_batch = batch[1]
    test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    print(f"Testing on batch {remain_batch}")
    test_concentrations = [f"{indir}/{remain_batch}.csv"]
    metric, detail = end2end_model(
        train_rgb_path,
        train_concentrations,
        test_rgb_path,
        test_concentrations,
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
