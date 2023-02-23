from sklearn.model_selection import train_test_split
import os
import pandas as pd
import glob
import cv2
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Basic function
def mean(array):
    return np.mean(np.array(array).flatten())
def mode(array):
    return np.bincount(np.array(array).flatten()).argmax()
def min1(array):
    return np.min(np.array(array).flatten())
def max1(array):
    return np.max(np.array(array).flatten())
def std1(array):
    return np.std(np.array(array).flatten())
def rgb(indir):
    # get values
    RGB_values=[]
    for image_location in glob.glob(indir):
        concentration = image_location.split("/")[-1].split('-')[0]
        image_id=image_location.split("/")[-1]
        # load
        image = cv2.imread(image_location,cv2.IMREAD_COLOR)
        RGB_values.append([image_id,concentration,mean(image[:,:,0]),mean(image[:,:,1]),mean(image[:,:,2]),
                                                  mode(image[:,:,0]),mode(image[:,:,1]),mode(image[:,:,2]),
                                                  min1(image[:,:,0]),min1(image[:,:,1]),min1(image[:,:,2]),
                                                  max1(image[:,:,0]),max1(image[:,:,1]),max1(image[:,:,2]),
                                                  std1(image[:,:,0]),std1(image[:,:,1]),std1(image[:,:,2])
                        ])
    columns_name=["image","concentration",
    "meanB","meanG","meanR",
    "modeB","modeG","modeR",
    "minB","minG","minR",
    "maxB","maxG","maxR",
    "stdB","stdG","stdR"]

    df = pd.DataFrame(RGB_values, columns=columns_name)
    df["batch"]=df["image"].apply(lambda x: x.split(".j")[0].split("_")[1])
    df["concentration"]=df["concentration"].astype(float)
    # get standard deviation 
    # note: this is different with std for each figures, this std for all figures with the same scene (1 concentration=10 figures for ex)
    std_result=[]
    for batch in df["batch"].unique():
        for concentration in df["concentration"].unique():
            df1=df[(df["batch"]==batch) & (df["concentration"]==concentration)]
            std=np.std(df1).to_list()[1:]
            std.insert(0,concentration)
            std.insert(0,batch)
            std_result.append(std)
    std_result=pd.DataFrame(std_result,columns=columns_name)
    return df,std_result

# Section 1: CuSO4
indir="data/balance_image/CuSO4"
outdir=indir
# Feature extraction
# raw_image=os.path.join(indir,"raw_image")
# os.system(f"python3 modules/feature_extraction.py -i {raw_image}  -o {outdir}")
# EDA

# background
indir=os.path.join(outdir,"result","background","*.jpg")
bg_val,bg_std=rgb(indir)
bg_val.to_csv("data/balance_image/CuSO4/result/EDA/val_background.csv",index=False)
bg_std.to_csv("data/balance_image/CuSO4/result/EDA/std_background.csv",index=False)
# ROI
indir=os.path.join(outdir,"result","raw_roi","*.jpg")
raw_roi_val,raw_roi_std=rgb(indir)
raw_roi_val.to_csv("data/balance_image/CuSO4/result/EDA/val_raw_roi.csv",index=False)
raw_roi_std.to_csv("data/balance_image/CuSO4/result/EDA/std_raw_roi.csv",index=False)
# Delta ROI
indir=os.path.join(outdir,"result","delta_normalized_roi","*.jpg")
delta_roi_val,delta_roi_std=rgb(indir)
delta_roi_val.to_csv("data/balance_image/CuSO4/result/EDA/val_delta_roi.csv",index=False)
delta_roi_std.to_csv("data/balance_image/CuSO4/result/EDA/std_delta_roi.csv",index=False)
# Ratio ROI
indir=os.path.join(outdir,"result","ratio_normalized_roi","*.jpg")
ratio_roi_val,ratio_roi_std=rgb(indir)
ratio_roi_val.to_csv("data/balance_image/CuSO4/result/EDA/val_ratio_roi.csv",index=False)
ratio_roi_std.to_csv("data/balance_image/CuSO4/result/EDA/std_ratio_roi.csv",index=False)

# Whether 



