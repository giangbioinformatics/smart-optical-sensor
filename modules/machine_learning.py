import os
import argparse
import pandas as pd
import cv2
import glob
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pickle
# Get RGB values, return the standard deviation and regression
def parseargs(required_args=True):
    # Format help
    class formatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
        pass
    epilog = ("")
    parser = argparse.ArgumentParser(description='Feature engineering to decide',
                                     epilog=epilog,
                                     formatter_class=formatter)
    readable = argparse.FileType('r') 
    parser.add_argument("-i", "--indir", help="Image path location" ,default=".")
    parser.add_argument("-m", "--method",help="Method for regression", default="poly3D")
    parser.add_argument("-o", "--outdir",help="Path location for output" ,default=".")
    args = parser.parse_args()
    return(args)

# Find mean and mode of an array value or list with different dimension
def mean(array):
    return np.mean(np.array(array).flatten())
def mode(array):
    return np.bincount(np.array(array).flatten()).argmax()

# Extract RGB values
def RGB_extraction(indir,outdir):
    RGB_values=[]
    for image_location in glob.glob(os.path.join(indir,"*.jpg")):
        concentration = image_location.split("/")[-1].split('-')[0]
        image_id=image_location.split("/")[-1]
        # load
        image = cv2.imread(image_location,cv2.IMREAD_COLOR)
        RGB_values.append([image_id,concentration,mean(image[:,:,0]),mean(image[:,:,1]),mean(image[:,:,2]),
                       mode(image[:,:,0]),mode([:,:,1]),mode(image[:,:,2])])
    df = pd.DataFrame(RGB_values, columns=["image","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
    df["concentration"]=df["concentration"].astype(float)
    df.to_csv(os.path.join(outdir,"RGB_values"),index=False)
    return df    

# Regression for RGB values
def regression(RGB_values,outdir):
    x = RGB_values[["meanB","meanG","meanR","modeB","modeG","modeR"]].values.astype(float)
    y = RGB_values["concentration"].values.astype(float)  # target variable
    poly = PolynomialFeatures(degree=2)
    X_t = poly.fit_transform(x)
    clf = LinearRegression()
    clf.fit(X_t, y)
    # Save model
    filename =os.path.join(outdir,"RGB_model.sav")
    pickle.dump(clf, open(filename, 'wb'))

def main(args):
    train_data=RGB_extraction(args.indir,args.outdir)
    regression(train_data,args.outdir)

if __name__ == '__main__': 
    args = parseargs()
    main(args) 
