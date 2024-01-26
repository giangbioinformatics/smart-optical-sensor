setwd("/home/nguyen/Desktop/Projects/smart-optiocal-sensor/")
source("scripts/basic_statistics.R")
source('http://www.sthda.com/upload/rquery_t_test.r')

# 01. Scatter plot full images
# train
train=read.delim("data/nano_Fe3+/batch_2/result/RGB_values.csv",sep=",")
# Linear regression
model=lm(as.formula(paste0("concentration~modeR+modeG+modeB+meanR+meanG+meanB")),data=train)

# test
# batch_1
test=read.delim("data/water_Fe3+/batch_1/result/RGB_values.csv",sep=",")
predict_data=predict(model,test)


# Set the row names using the list
row.names(df) <- row_names
result <- data.frame(cbind(test$image_id, predict_data))
colnames(result)<-c("image","predicted_concentration")                   
write.table(result,file="data/water_Fe3+/batch_1/result/predict_batch1.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)

# test
# batch_2
test=read.delim("data/water_Fe3+/batch_2/result/RGB_values.csv",sep=",")
predict_data=predict(model,test)


# Set the row names using the list
result <- data.frame(cbind(test$image_id, predict_data))
colnames(result)<-c("image","predicted_concentration")                   
write.table(result,file="data/water_Fe3+/batch_2/result/predict_batch2.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)

# test
# batch_3
test=read.delim("data/water_Fe3+/batch_3/result/RGB_values.csv",sep=",")
predict_data=predict(model,test)


# Set the row names using the list
result <- data.frame(cbind(test$image_id, predict_data))
colnames(result)<-c("image","predicted_concentration")                   
write.table(result,file="data/water_Fe3+/batch_3/result/predict_batch3.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)

