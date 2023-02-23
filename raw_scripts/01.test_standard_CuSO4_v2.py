#!/usr/bin/env python3
import os
import argparse
import pandas as pd
import cv2
import glob
import numpy as np
import itertools
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

# Extract ROI, normalize and return RGB value
def image_processing(outdir):
    outdir="/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/CuSO4/example/result"
    indir="/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/CuSO4/example/raw_image"

    # mkdir for store the specifc type of image
    os.makedirs(os.path.join(outdir,"squared_frame"),exist_ok=True)
    os.makedirs(os.path.join(outdir,"raw_roi"),exist_ok=True)
    os.makedirs(os.path.join(outdir,"normalized_roi"),exist_ok=True)

    # cutoff value for countour to get ROI

    for image_location in glob.glob(os.path.join(indir,"*.jpg")):
        image=cv2.imread(image_location)
        file_name = image_location.split("/")[-1].split(".j")[0]
        # create hsv
        ranges=[]
        for b in range(20,240,20):
            for g in range(20,240,20):
                for r in range(20,240,20):
                    ranges.append((b,g,r))
        combinations_all = []
        combinations_all.extend(list(itertools.combinations(ranges, 2)))
        for k in combinations_all:
            try:
                low_val=k[0]
                high_val=k[1]
                for i in range(0,250,10):
                    try:
                
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
                        cv2.imwrite(outdir+"/"+file_name+str(low_val)+"_"+str(high_val)+"_coutour.jpg", mask)
                    except: pass
            except: pass

        
        squared_frame= image[y:y+h, x:x+w]

        # Section for cover
        dim = (740, 740)
        roi = cv2.resize(squared_frame, dim, interpolation=cv2.INTER_AREA)
        roi = roi[450:-250, 250:-250]
        # Normalize
        normalized=normalized_execute(squared_frame_image=squared_frame,roi_image=roi)

        # Save image
        cv2.imwrite(os.path.join(args.outdir,"squared_frame/"+file_name+".jpg"), squared_frame)
        cv2.imwrite(os.path.join(args.outdir,"raw_roi/"+file_name+".jpg"), roi)
        cv2.imwrite(os.path.join(args.outdir,"normalized_roi/"+file_name+".jpg"),normalized)
    print("Completed!")

def main(args):
    image_processing(args)

if __name__ == '__main__': 
    args = parseargs()
    main(args) 
