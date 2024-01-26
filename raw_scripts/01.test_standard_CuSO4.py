# Standard
import cv2
import glob
import os
import pandas as pd

# Stats
from scipy.optimize import curve_fit
from scipy import stats
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 00.Test for get region of interest from one image
image=cv2.imread("data/standard_CuSO4/example/0.5-1.jpg")
roi = image[2200:2400, 1150:1350]
cv2.imwrite("data/standard_CuSO4/example/roi_0.5-1.jpg", roi)

# 01.Loop to get ROI for all figure
for image_location in glob.glob("data/standard_CuSO4/raw_image/*.jpg"):
    image=cv2.imread(image_location)
    roi = image[2200:2400, 1150:1350]
    roi_image_location=image_location.replace("raw_image","roi_image")
    cv2.imwrite(roi_image_location, roi)

# 02.Get the value of mean,mode in RGB array
result=[]
for image_location in glob.glob("data/standard_CuSO4/roi_image/*.jpg"):
    # config
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
df["concentration"]=df["concentration"].astype(float)
df.to_csv("data/standard_CuSO4/regression/RGB_values.csv")




# 03. Linear regression

# Define the target column
target = 'concentration'

# Create a list of the independent variables (all columns except the target)
independent_vars = [col for col in df.columns if col != target]

# Loop through each independent variable
for column in independent_vars:
    # Fit a simple linear regression model using this independent variable and the target
    slope, intercept, r_value, p_value, std_err = stats.linregress(df[column], df[target])

    # Plot the scatter plot of the independent variable and the target
    sns.regplot(x=column, y=target, data=df)

    # Plot the regression line
    plt.plot(df[column], slope * df[column] + intercept, '-', color='red')

    # Add the regression equation to the plot
    plt.text(x=0.05, y=0.95, s=f'y = {slope:.2f}x + {intercept:.2f}', 
             transform=plt.gca().transAxes, ha='left', va='top')

    # Add the p-value of the f-test for R-squared to the plot
    plt.text(x=0.05, y=0.9, s=f'p-value for R-squared: {p_value:.2f}', 
             transform=plt.gca().transAxes, ha='left', va='top')

    # Add the R-squared value to the plot
    plt.text(x=0.05, y=0.85, s=f'R-squared: {r_value**2:.2f}', 
             transform=plt.gca().transAxes, ha='left', va='top')

    # Show the plot
    plt.show()