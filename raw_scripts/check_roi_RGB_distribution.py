import numpy as np
import cv2
import os
import sys
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy import stats
import glob

path = "data/CuSO4/background_normalization_batch1"
path = "data/nano_Fe3+/background_normalization_batch1"

# Check ROI
def check_ROI_RGB(ROI_location):
    B_array=[]
    G_array=[]
    R_array=[]
    for squared_frame_image  in glob.glob(ROI_location+"/*.jpg"):
        squared_frame_image=cv2.imread(squared_frame_image)
        B = np.mean(squared_frame_image[:, :, 0])
        G = np.mean(squared_frame_image[:, :, 1])
        R = np.mean(squared_frame_image[:, :, 2])
        B_array.append(B)
        G_array.append(G)
        R_array.append(R)
    return [np.mean(R_array),np.mean(G_array),np.mean(B_array)],[np.std(R_array),np.std(G_array),np.std(B_array)]
mean_RGB,std_RGB=check_ROI_RGB(path+"/background")
mean_RGB,std_RGB=check_ROI_RGB(path+"/raw_roi")
