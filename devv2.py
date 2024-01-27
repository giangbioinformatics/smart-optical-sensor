from smartsensor.basev2 import (
    end2end_model,
)
import glob
import os
import pandas as pd
# params
data_path = "EDA/CUSO4"
indir = f"{data_path}/raw_data"

test_size = 0.3
batches = ["batch1", "batch2", "batch3"]

process_outdir = f"{data_path}/process_data_test"

# # RAW
# raw_res = []
# process_type = "raw_roi"
# prefix = "raw_roi"
# indir_e2e = f"{process_outdir}/{process_type}"
# outdir_e2e = (
#     f"{data_path}/result_without_filter_and_feature_selection_2train_1test"
# )
# features = "meanR,meanG,meanB,modeR,modeB,modeG"
# degree = 1
# outdir = os.path.join(outdir_e2e, process_type)
# os.makedirs(outdir, exist_ok=True)
# # raw data
# for batch in batches:
#     remain_batches = [x for x in batches if x != batch]
#     print(f"Training on batch {remain_batches}")
#     train_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     train_concentration = []
#     for remain_batch in remain_batches:
#         train_concentration.append(f"{indir}/{remain_batch}.csv")
#
#     print(f"Testing batch {batch}")
#     # raw_data
#     test_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     test_concentration = f"{indir}/{batch}.csv"
#     # test
#
#     metric, detail = end2end_model(
#         train_rgb_path,
#         train_concentration,
#         test_rgb_path,
#         test_concentration,
#         features,
#         degree,
#         outdir,
#         prefix,
#     )
#     raw_res.append(metric)
# pd.DataFrame(pd.concat(raw_res)).to_csv(
#     f"{outdir_e2e}/result_raw_2train_1test.csv", index=False
# )
# # DELTA
# raw_res = []
# process_type = "delta_normalized_roi"
# prefix = "delta_roi"
# indir_e2e = f"{process_outdir}/{process_type}"
# outdir_e2e = (
#     f"{data_path}/result_without_filter_and_feature_selection_2train_1test"
# )
# features = "meanR,meanG,meanB,modeR,modeB,modeG"
# degree = 1
# outdir = os.path.join(outdir_e2e, process_type)
# os.makedirs(outdir, exist_ok=True)
# # raw data
# for batch in batches:
#     # print(f"Processing batch {batch}")
#     # # raw_data
#     # train_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     # train_concentration = f"{indir}/{batch}.csv"
#     # # test
#     # remain_batches = [x for x in batches if x != batch]
#     # test_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     # for remain_batch in remain_batches:
#     #     print(f"Testing on batch {remain_batch}")
#     #     test_concentration = f"{indir}/{remain_batch}.csv"
#     remain_batches = [x for x in batches if x != batch]
#     print(f"Training on batch {remain_batches}")
#     train_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     train_concentration = []
#     for remain_batch in remain_batches:
#         train_concentration.append(f"{indir}/{remain_batch}.csv")
#
#     print(f"Testing batch {batch}")
#     # raw_data
#     test_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     test_concentration = f"{indir}/{batch}.csv"
#     # test
#     metric, detail = end2end_model(
#         train_rgb_path,
#         train_concentration,
#         test_rgb_path,
#         test_concentration,
#         features,
#         degree,
#         outdir,
#         prefix,
#     )
#     raw_res.append(metric)
# pd.DataFrame(pd.concat(raw_res)).to_csv(
#     f"{outdir_e2e}/result_delta_2train_1test.csv", index=False
# )
#
# # RATIO
# raw_res = []
# process_type = "ratio_normalized_roi"
# prefix = "ratio_roi"
# indir_e2e = f"{process_outdir}/{process_type}"
# outdir_e2e = (
#     f"{data_path}/result_without_filter_and_feature_selection_2train_1test"
# )
# features = "meanR,meanG,meanB,modeR,modeB,modeG"
# degree = 1
# outdir = os.path.join(outdir_e2e, process_type)
# os.makedirs(outdir, exist_ok=True)
# # raw data
# for batch in batches:
#     # print(f"Processing batch {batch}")
#     # # raw_data
#     # train_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     # train_concentration = f"{indir}/{batch}.csv"
#     # # test
#     # remain_batches = [x for x in batches if x != batch]
#     # test_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     # for remain_batch in remain_batches:
#     #     print(f"Testing on batch {remain_batch}")
#     #     test_concentration = f"{indir}/{remain_batch}.csv"
#     remain_batches = [x for x in batches if x != batch]
#     print(f"Training on batch {remain_batches}")
#     train_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     train_concentration = []
#     for remain_batch in remain_batches:
#         train_concentration.append(f"{indir}/{remain_batch}.csv")
#
#     print(f"Testing batch {batch}")
#     # raw_data
#     test_rgb_path = f"{indir_e2e}/RGB_values.csv"
#     test_concentration = f"{indir}/{batch}.csv"
#     # test
#     metric, detail = end2end_model(
#         train_rgb_path,
#         train_concentration,
#         test_rgb_path,
#         test_concentration,
#         features,
#         degree,
#         outdir,
#         prefix,
#     )
#     raw_res.append(metric)
#
# pd.DataFrame(pd.concat(raw_res)).to_csv(
#     f"{outdir_e2e}/result_ratio_2train_1test.csv", index=False
# )

# ****************************************
# Strategy 2 combine all and split
# RAW
raw_res = []
process_type = "raw_roi"
prefix = "raw_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = (
    f"{data_path}/result_without_filter_and_feature_selection_2train_1test"
)
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
# for batch in batches:
    # remain_batches = [x for x in batches if x != batch]
    # print(f"Training on batch {remain_batches}")
train_rgb_path = f"{indir_e2e}/RGB_values.csv"
train_concentration = []
for remain_batch in batches:
    train_concentration.append(f"{indir}/{remain_batch}.csv")

# print(f"Testing batch {batch}")
# # raw_data
# test_rgb_path = f"{indir_e2e}/RGB_values.csv"
# test_concentration = f"{indir}/{batch}.csv"
# test

metric, detail = end2end_model(
    train_rgb_path,
    train_concentration,
    None,
    None,
    features,
    degree,
    outdir,
    prefix,
)
raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_raw_2train_1test.csv", index=False
)
# DELTA
raw_res = []
process_type = "delta_normalized_roi"
prefix = "delta_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = (
    f"{data_path}/result_without_filter_and_feature_selection_2train_1test"
)
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
# for batch in batches:
    # print(f"Processing batch {batch}")
    # # raw_data
    # train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    # train_concentration = f"{indir}/{batch}.csv"
    # # test
    # remain_batches = [x for x in batches if x != batch]
    # test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    # for remain_batch in remain_batches:
    #     print(f"Testing on batch {remain_batch}")
    #     test_concentration = f"{indir}/{remain_batch}.csv"
    # remain_batches = [x for x in batches if x != batch]
    # print(f"Training on batch {remain_batches}")
train_rgb_path = f"{indir_e2e}/RGB_values.csv"
train_concentration = []
for remain_batch in batches:
    train_concentration.append(f"{indir}/{remain_batch}.csv")

# print(f"Testing batch {batch}")
# # raw_data
# test_rgb_path = f"{indir_e2e}/RGB_values.csv"
# test_concentration = f"{indir}/{batch}.csv"
# test
metric, detail = end2end_model(
    train_rgb_path,
    train_concentration,
    None,
    None,
    features,
    degree,
    outdir,
    prefix,
)
raw_res.append(metric)
pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_delta_2train_1test.csv", index=False
)

# RATIO
raw_res = []
process_type = "ratio_normalized_roi"
prefix = "ratio_roi"
indir_e2e = f"{process_outdir}/{process_type}"
outdir_e2e = (
    f"{data_path}/result_without_filter_and_feature_selection_2train_1test"
)
features = "meanR,meanG,meanB,modeR,modeB,modeG"
degree = 1
outdir = os.path.join(outdir_e2e, process_type)
os.makedirs(outdir, exist_ok=True)
# raw data
# for batch in batches:
    # print(f"Processing batch {batch}")
    # # raw_data
    # train_rgb_path = f"{indir_e2e}/RGB_values.csv"
    # train_concentration = f"{indir}/{batch}.csv"
    # # test
    # remain_batches = [x for x in batches if x != batch]
    # test_rgb_path = f"{indir_e2e}/RGB_values.csv"
    # for remain_batch in remain_batches:
    #     print(f"Testing on batch {remain_batch}")
    #     test_concentration = f"{indir}/{remain_batch}.csv"
    # remain_batches = [x for x in batches if x != batch]
    # print(f"Training on batch {remain_batches}")
train_rgb_path = f"{indir_e2e}/RGB_values.csv"
train_concentration = []
for remain_batch in batches:
    train_concentration.append(f"{indir}/{remain_batch}.csv")

# print(f"Testing batch {batch}")
# # raw_data
# test_rgb_path = f"{indir_e2e}/RGB_values.csv"
# test_concentration = f"{indir}/{batch}.csv"
# test
metric, detail = end2end_model(
    train_rgb_path,
    train_concentration,
    None,
    None,
    features,
    degree,
    outdir,
    prefix,
)
raw_res.append(metric)

pd.DataFrame(pd.concat(raw_res)).to_csv(
    f"{outdir_e2e}/result_ratio_2train_1test.csv", index=False
)