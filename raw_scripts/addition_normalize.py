import numpy as np
import cv2
import os
import sys
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy import stats
import glob

# Lost one raw image but we still get the squared_frame, therefore, it can be used to preproduce again
path = "data/water_Fe3+/batch_1/squared_frame_fix"

# Nomalize image base on the standard color of green border
def normalized_execute(squared_frame_image,roi_image):
    k1 = 20
    k2 = 80
    # Take the upper region for balance cover
    redB = np.mean(squared_frame_image[k1:k2, k1:-k1][:, :, 0])
    redG = np.mean(squared_frame_image[k1:k2, k1:-k1][:, :, 1])
    redR = np.mean(squared_frame_image[k1:k2, k1:-k1][:, :, 2])
    # return [redB,redG,redR]
    # parameter for different cover border
    # The green border color to be normalized
    lum = [60, 90, 30]

    # delta
    deltaB = lum[0]-redB
    deltaG = lum[1]-redG
    deltaR = lum[2]-redR
    
    delta_normalized_roi=np.array(roi_image)
    delta_normalized_roi[:, :, 0] = delta_normalized_roi[:, :, 0]+deltaB
    delta_normalized_roi[:, :, 1] = delta_normalized_roi[:, :, 1]+deltaG
    delta_normalized_roi[:, :, 2] = delta_normalized_roi[:, :, 2]+deltaR
    
    return delta_normalized_roi

# 02.Get region of interest
for image_location in glob.glob(path+"/*.jpg"):
    print(image_location)
    squared_frame=cv2.imread(image_location)
    file_name = image_location.split("/")[-1].split(".j")[0]
    # Section for cover
    dim = (740, 740)
    roi = cv2.resize(squared_frame, dim, interpolation=cv2.INTER_AREA)
    roi = roi[450:-250, 250:-250]
    # Normalize
    normalized=normalized_execute(squared_frame_image=squared_frame,roi_image=roi)
    # Save image
    # cv2.imwrite(path+"/roi_image/"+file_name+"_coutour.jpg", mask)
    cv2.imwrite(path+"/raw_roi/"+file_name+".jpg", roi)
    cv2.imwrite(path+"/normalized_roi/"+file_name+".jpg", normalized)
