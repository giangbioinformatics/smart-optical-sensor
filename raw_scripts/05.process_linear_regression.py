import pandas as pd
import numpy as np
import glob
import cv2
import os
# Fe3+ standard
# batch_1
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/nano_Fe3+/batch_1/result'
for image_location in glob.glob(os.path.join(path,"normalized_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
con= pd.read_csv("data/nano_Fe3+/batch_1/UVis_result.csv",sep=";")
con["concentration"]=con["concentration"].apply(lambda x: x.replace(",","."))
con["concentration"]=con["concentration"].astype(float)
df["image"]=df["image_id"].apply(lambda x: x.split(".j")[0])
df=df.drop(columns=["concentration"])
df1=pd.merge(df,con,on="image")
df1.head()
df1.to_csv(os.path.join(path,"RGB_values.csv"),index=False)



# batch_2
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/nano_Fe3+/batch_2/result'
for image_location in glob.glob(os.path.join(path,"normalized_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
con= pd.read_csv("data/nano_Fe3+/batch_2/UVis_result.csv",sep=";")
con["concentration"]=con["concentration"].apply(lambda x: x.replace(",","."))
con["concentration"]=con["concentration"].astype(float)
df["image"]=df["image_id"].apply(lambda x: x.split(".j")[0])
df=df.drop(columns=["concentration"])
df1=pd.merge(df,con,on="image")
df1.head()
df1.to_csv(os.path.join(path,"RGB_values.csv"),index=False)


# batch_3
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/nano_Fe3+/batch_3/result'
for image_location in glob.glob(os.path.join(path,"normalized_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
con= pd.read_csv("data/nano_Fe3+/batch_3/UVis_result.csv",sep=";")
con["concentration"]=con["concentration"].apply(lambda x: x.replace(",","."))
con["concentration"]=con["concentration"].astype(float)
df["image"]=df["image_id"].apply(lambda x: x.split(".j")[0])
df=df.drop(columns=["concentration"])
df1=pd.merge(df,con,on="image")
df1.head()
df1.to_csv(os.path.join(path,"RGB_values.csv"),index=False)

# Fe3+ water
# batch_1
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/water_Fe3+/batch_1/result'
for image_location in glob.glob(os.path.join(path,"normalized_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
df.to_csv(os.path.join(path,"RGB_values.csv"),index=False)



# batch_2
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/water_Fe3+/batch_2/result'
for image_location in glob.glob(os.path.join(path,"normalized_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
df.to_csv(os.path.join(path,"RGB_values.csv"),index=False)


# batch_3
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/water_Fe3+/batch_3/result'
for image_location in glob.glob(os.path.join(path,"normalized_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
df.to_csv(os.path.join(path,"RGB_values.csv"),index=False)


# CuSO4
# batch 1
# Normalized
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/CuSO4/batch_1/result'
for image_location in glob.glob(os.path.join(path,"normalized_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
df.to_csv(os.path.join(path,"normalized_RGB_values.csv"),index=False)

# Non normalized
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/CuSO4/batch_1/result'
for image_location in glob.glob(os.path.join(path,"raw_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])

# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
df.to_csv(os.path.join(path,"raw_RGB_values.csv"),index=False)

# CuSO4 new 19/02/2023
# Balanced
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/balance_image/CuSO4/result/'
for image_location in glob.glob(os.path.join(path,"normalized_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])
# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
df["concentration"]=df["concentration"].astype(float)
df.corr()

# raw
result=[]
path='/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/balance_image/CuSO4/result/'
for image_location in glob.glob(os.path.join(path,"raw_roi/*.jpg")):
    # config
    print(image_location)
    concentration = image_location.split("/")[-1].split('-')[0]
    image_id=image_location.split("/")[-1]
    # load
    image = cv2.imread(image_location,cv2.IMREAD_COLOR)
    result.append([image_id,concentration,np.mean(image[:,:,0]),np.mean(image[:,:,1]), np.mean(image[:,:,2]),
                np.bincount(image[:,:,0].flatten()).argmax(),np.bincount(image[:,:,1].flatten()).argmax(),np.bincount(image[:,:,2].flatten()).argmax()])
# save result
df = pd.DataFrame(result, columns=["image_id","concentration","meanB","meanG","meanR","modeB","modeG","modeR"])
df["concentration"]=df["concentration"].astype(float)
df.corr()


import numpy as np
from scipy.optimize import curve_fit

# define the polynomial function to fit the data
def polynomial_function(x, *params):
    """
    Returns the value of a polynomial function for input values x and a list of polynomial coefficients.
    
    Parameters:
        x (array-like): Input values.
        *params (float): Polynomial coefficients in descending order.
        
    Returns:
        array-like: Output values of the polynomial function.
    """
    return sum([params[i] * x**(len(params)-i-1) for i in range(len(params))])

# generate some random data for the regression
df["batch"]=df["image_id"].apply(lambda x: x.split(".j")[0].split("_")[1])
df1=df[df["batch"]=="batch1"]
x = df1[["meanR","meanB","meanG","modeR","modeB","modeG"]].values.astype(float) # 100 samples with 3 features each
y = df1["concentration"].values.astype(float)  # target variable

# fit the polynomial function to the data using curve_fit from Scipy
# popt, _ = curve_fit(polynomial_function, x.T, y)

# fit the polynomial function to the data using curve_fit
popt, pcov = curve_fit(polynomial_function, x, y)

# print the coefficients of the polynomial function
print('Coefficients:', popt)

# calculate the root-mean-squared error (RMSE) and percent mean absolute error (PMAE)
y_pred = polynomial_function(x, *popt)
rmse = np.sqrt(np.mean((y - y_pred)**2))
pmae = np.mean(np.abs((y - y_pred) / y))

# print the results
print(f"RMSE: {rmse}")
print(f"MAE: {pmae}")

coeffs = np.polyfit(x, y, deg=2)
# use the coefficients to make predictions
y_pred = np.polyval(coeffs, x)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df1=df[df["batch"]=="batch1"]
# df1=df
x = df1[["meanB","meanG","meanR","modeB","modeG","modeR"]].values.astype(float) # 100 samples with 3 features each
# x = df1[["meanG"]].values.astype(float) # 100 samples with 3 features each
y = df1["concentration"].values.astype(float)  # target variable

poly = PolynomialFeatures(degree=1)
X_t = poly.fit_transform(x)
clf = LinearRegression()
clf.fit(X_t, y)
print(clf.coef_)
print(clf.intercept_)
y_pred=clf.predict(X_t)
rmse = np.sqrt(np.mean((y - y_pred)**2))
mae  = np.mean(np.abs(y - y_pred))
pmae = np.mean(np.abs((y - y_pred) / y)) * 100
rmse
mae
pmae

df2=df[df["batch"]=="batch2"]
x_test = df2[["meanB","meanG","meanR","modeB","modeG","modeR"]].values.astype(float) # 100 samples with 3 features each
# x_test = df1[["meanG"]].values.astype(float) # 100 samples with 3 features each
y_test = df2["concentration"].values.astype(float)  # target variable
y_pred_test=clf.predict(poly.fit_transform(x_test))
np.mean(np.abs((y_test - y_pred_test) / y_test)) * 100




# B1: Normalize => std nhỏ hơn (cùng 1 nồng độ nhiều tấm ảnh)
# background=90,60,30
# B2: Regression (raw|normalized) rmse càng nhỏ càng tốt
# đợt 1 (train) đợt 2 (test) đợt 3(test)    bg 4 bg 0 roi 3 n_roi 1
# Khi nào thì dùng normalized (std background<roi)
# Khi nào thì dùng raw (std background>roi) bg 1.5 bg 0 roi 1 n_roi 1.2



