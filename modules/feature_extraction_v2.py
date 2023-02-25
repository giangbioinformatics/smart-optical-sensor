#!/usr/bin/env python3
import os
import argparse
import pandas as pd
import cv2
import glob
import numpy as np

def parseargs(required_args=True):
    # Format help
    class formatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
        pass
    epilog = ("")
    parser = argparse.ArgumentParser(description='Get the ROI, normalized and return RGB value',
                                     epilog=epilog,
                                     formatter_class=formatter)
    readable = argparse.FileType('r') 
    parser.add_argument("-i", "--indir", help="Image path location" ,default=".")
    parser.add_argument("-fm","--feature_method",help="Method for featurinng",default=mean)
    parser.add_argument("-c", "--constant",help="Constant color for normalization",default=[60,90,30])
    parser.add_argument("-t", "--threshold",help="Threshold to detect the square frame region",default=[(0,110,60),(80,220,160)])
    parser.add_argument("-o", "--outdir",help="Path location for output" ,default=".")
    args = parser.parse_args()
    return(args)

# Find mean and mode of an array value or list with different dimension
def mean(array):
    return np.mean(np.array(array).flatten())
def mode(array):
    return np.bincount(np.array(array).flatten()).argmax()
def rgb2dataframe(array):
    return pd.DataFrame(array.reshape(-1, 3), columns=["B","G","R"])
# Nomalize image base on the standard color of green border
def normalized_execute(roi_image,background,lum,feature_method):
    # Take the upper region for balance cover
    B = feature_method(background[:, :, 0])
    G = feature_method(background[:, :, 1])
    R = feature_method(background[:, :, 2])
    # parameter for different cover border
    # The green border color to be normalized
    # ratio
    ratioB = lum[0]/B
    ratioG = lum[1]/G
    ratioR = lum[2]/R
    ratio_normalized_roi=rgb2dataframe(roi_image)
    ratio_normalized_roi["B"] = ratio_normalized_roi["B"]*ratioB
    ratio_normalized_roi["G"] = ratio_normalized_roi["G"]*ratioG
    ratio_normalized_roi["R"] = ratio_normalized_roi["R"]*ratioR
    # delta
    deltaB = lum[0]-B
    deltaG = lum[1]-G
    deltaR = lum[2]-R
    delta_normalized_roi=rgb2dataframe(roi_image)
    delta_normalized_roi["B"] = delta_normalized_roi["B"]+deltaB
    delta_normalized_roi["G"] = delta_normalized_roi["G"]+deltaG
    delta_normalized_roi["R"] = delta_normalized_roi["R"]+deltaR
    return ratio_normalized_roi, delta_normalized_roi, rgb2dataframe(roi_image)

# Extract ROI, normalize and return RGB value
def image_processing(args):
    # mkdir for storing intermediate files and result
    result_path=os.path.join(args.outdir,"result")
    os.makedirs(result_path,exist_ok=True)
    os.makedirs(os.path.join(result_path,"squared_frame"),exist_ok=True)
    os.makedirs(os.path.join(result_path,"raw_roi"),exist_ok=True)
    os.makedirs(os.path.join(result_path,"ratio_normalized_roi"),exist_ok=True)
    os.makedirs(os.path.join(result_path,"delta_normalized_roi"),exist_ok=True)
    os.makedirs(os.path.join(result_path,"background"),exist_ok=True)
    
    # coutour value
    low_val  = args.threshold[0]
    high_val = args.threshold[1]

    for image_location in glob.glob(os.path.join(args.indir,"*.jpg")):
        image=cv2.imread(image_location)
        file_name = image_location.split("/")[-1].split(".j")[0]
        # create hsv
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
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
        cv2.imwrite(result_path+"/squared_frame/"+file_name+".jpg", squared_frame)
        cv2.imwrite(result_path+"/background/"+file_name+".jpg", background)
        cv2.imwrite(result_path+"/raw_roi/"+file_name+".jpg", roi)

def balance_image(args):
    result_path=os.path.join(args.outdir,"result")
    for image_location in glob.glob(os.path.join(args.indir,"*.jpg")):
        image=cv2.imread(image_location)
        print(f"Processing image: {image_location}")
        file_name = image_location.split("/")[-1].split(".j")[0]
        # Save image
        squared_frame=cv2.imread(result_path+"/squared_frame/"+file_name+".jpg")
        roi=cv2.imread(result_path+"/raw_roi/"+file_name+".jpg")
        background=cv2.imread(result_path+"/background/"+file_name+".jpg")
        # Normalize
        ratio_normalized,delta_normalized,roi=normalized_execute(roi_image=roi,background=background,lum=args.constant,feature_method=args.feature_method)
        # cv2.imwrite(result_path+"/ratio_normalized_roi/"+file_name+".jpg", ratio_normalized)
        # cv2.imwrite(result_path+"/delta_normalized_roi/"+file_name+".jpg", delta_normalized)
        roi.to_csv(result_path+"/raw_roi/"+file_name+".csv",index=False)
        ratio_normalized.to_csv(result_path+"/ratio_normalized_roi/"+file_name+".csv",index=False)
        delta_normalized.to_csv(result_path+"/delta_normalized_roi/"+file_name+".csv",index=False)

def main(args):
    image_processing(args)
    balance_image(args)

if __name__ == '__main__': 
    args = parseargs()
    main(args) 
