import numpy as np
import cv2
import os
import sys
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy import stats
import scipy
import glob

path = "data/CuSO4/background_normalization_batch1"
path = "data/nano_Fe3+/background_normalization_batch1"

def mode(array):
    mode_value=np.bincount(np.array(array).flatten()).argmax()
    return mode_value

# Detect lum value for scale
def detect_lum(background_image_location):
    B_array=[]
    G_array=[]
    R_array=[]
    for background_image  in glob.glob(background_image_location+"/*.jpg"):
        print(background_image)
        background_image=cv2.imread(background_image)
        B = mode(background_image[:, :, 0])
        G = mode(background_image[:, :, 1])
        R = mode(background_image[:, :, 2])
        B_array.append(B)
        G_array.append(G)
        R_array.append(R)
        print(B,G,R)
    return [mode(B_array),mode(G_array),mode(R_array)]

# Fix value for smaller than 0 and larger than 255
def fix_range_RGB(array):
    array[array<0]   = 0
    array[array>255] = 255
    return array

# Feature extraction
def normalized_execute(squared_frame_image,roi_image,lum,background):
    # Take the upper region for balance cover
    B = mode(background[:, :, 0])
    G = mode(background[:, :, 1])
    R = mode(background[:, :, 2])

    std_B = np.std(background[:, :, 0])
    std_G = np.std(background[:, :, 1])
    std_R = np.std(background[:, :, 2])
    print(std_B,std_G,std_R)
    # return [redB,redG,redR]
    # parameter for different cover border
    # The green border color to be normalized
    # ratio
    ratioB = lum[0]/B
    ratioG = lum[1]/G
    ratioR = lum[2]/R
    
    ratio_normalized_roi=np.array(roi_image)
    ratio_normalized_roi[:, :, 0] = fix_range_RGB(ratio_normalized_roi[:, :, 0]*ratioB)
    ratio_normalized_roi[:, :, 1] = fix_range_RGB(ratio_normalized_roi[:, :, 1]*ratioG)
    ratio_normalized_roi[:, :, 2] = fix_range_RGB(ratio_normalized_roi[:, :, 2]*ratioR)

    # delta
    deltaB = lum[0]-B
    deltaG = lum[1]-G
    deltaR = lum[2]-R

    # print(deltaB,deltaG,deltaR)
    
    delta_normalized_roi=np.array(roi_image)
    delta_normalized_roi[:, :, 0] = fix_range_RGB(delta_normalized_roi[:, :, 0] +deltaB)
    delta_normalized_roi[:, :, 1] = fix_range_RGB(delta_normalized_roi[:, :, 1] +deltaG)
    delta_normalized_roi[:, :, 2] = fix_range_RGB(delta_normalized_roi[:, :, 2] +deltaR)
    
    return ratio_normalized_roi, delta_normalized_roi

# Get ROI
for image_location in glob.glob(path+"/raw_image/*.jpg"):
    # print(image_location)
    image=cv2.imread(image_location)
    file_name = image_location.split("/")[-1].split(".j")[0]
    # create hsv
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # set lower and upper cover limits
    # if background == "white":
    # low_val = (70, 70, 70)
    # high_val = (200, 200, 200)
    low_val = (0, 110, 60)
    high_val = (80, 220,160)
    # Threshold the HSV image
    mask = cv2.inRange(hsv, low_val, high_val)
    # find contours in mask
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # select the largest contour
    largest_area = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > largest_area:
            cont = cnt
            largest_area = cv2.contourArea(cnt)
    # get the parameters of the boundingbox
    x, y, w, h = cv2.boundingRect(cont)
    squared_frame= image[y:y+h, x:x+w]
    # Section for cover
    dim = (740, 740)
    roi = cv2.resize(squared_frame, dim, interpolation=cv2.INTER_AREA)
    # Background image
    background=roi[50:60, 350:360]
    # ROI
    roi = roi[245:-245, 245:-245]
    # cv2.imwrite(path+"/roi_image/"+file_name+"_coutour.jpg", mask)
    cv2.imwrite(path+"/squared_frame/"+file_name+".jpg", squared_frame)
    cv2.imwrite(path+"/background/"+file_name+".jpg", background)
    cv2.imwrite(path+"/raw_roi/"+file_name+".jpg", roi)


# Feature extraction
# lum=detect_lum(path+"/background/")
lum= [30,90,60]

for image_location in glob.glob(path+"/raw_image/*.jpg"):
    image=cv2.imread(image_location)
    file_name = image_location.split("/")[-1].split(".j")[0]
    # Save image
    squared_frame=cv2.imread(path+"/squared_frame/"+file_name+".jpg")
    roi=cv2.imread(path+"/raw_roi/"+file_name+".jpg")
    background=cv2.imread(path+"/background/"+file_name+".jpg")
    # Normalize
    ratio_normalized,delta_normalized=normalized_execute(squared_frame_image=squared_frame,roi_image=roi,lum=lum,background=background)
    cv2.imwrite(path+"/ratio_normalized_roi/"+file_name+".jpg", ratio_normalized)
    cv2.imwrite(path+"/delta_normalized_roi/"+file_name+".jpg", delta_normalized)

# 04. Get the result of RGB value
# Normal, not do anything
result_normal=[]
for image_location in glob.glob(path+"/raw_roi/*.jpg"):
    # config
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result_normal.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
    mode(image[:,:,0].flatten()),mode(image[:,:,1].flatten()),mode(image[:,:,2].flatten())])
normal= pd.DataFrame(result_normal, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])

# Scale by multiply with ratio detected by border color
result_ratio=[]
for image_location in glob.glob(path+"/ratio_normalized_roi/*.jpg"):
    # config
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result_ratio.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
    mode(image[:,:,0].flatten()),mode(image[:,:,1].flatten()),mode(image[:,:,2].flatten())])

ratio= pd.DataFrame(result_ratio, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
# Scale by add difference
result_delta=[]
for image_location in glob.glob(path+"/delta_normalized_roi/*.jpg"):
    # config
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result_delta.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
    mode(image[:,:,0].flatten()),mode(image[:,:,1].flatten()),mode(image[:,:,2].flatten())])

delta= pd.DataFrame(result_delta, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])

np.std(normal)
np.std(ratio)
np.std(delta)
