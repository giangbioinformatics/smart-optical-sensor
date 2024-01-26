setwd("/home/nguyen/Desktop/Projects/smart-optiocal-sensor/")
source("scripts/basic_statistics.R")
source('http://www.sthda.com/upload/rquery_t_test.r')

# 01. Scatter plot full images
df=read.delim("data/nano_Fe3+/batch_1/result/RGB_values.csv",sep=",")
# Draw regression plot for all 6 features
# Mean
regress_nano=simple_regression(x="meanG",y="concentration",xindex=100,yindex=2,data=df,location="data/nano_Fe3+/batch_1/result/meanG.png")
regress_nano=simple_regression(x="meanR",y="concentration",xindex=12,yindex=2,data=df,location="data/nano_Fe3+/batch_1/result/meanR.png")
regress_nano=simple_regression(x="meanB",y="concentration",xindex=148,yindex=2,data=df,location="data/nano_Fe3+/batch_1/result/meanB.png")
# Mode
regress_nano=simple_regression(x="modeG",y="concentration",xindex=100,yindex=2,data=df,location="data/nano_Fe3+/batch_1/result/modeG.png")
regress_nano=simple_regression(x="modeR",y="concentration",xindex=12,yindex=2,data=df,location="data/nano_Fe3+/batch_1/result/modeR.png")
regress_nano=simple_regression(x="modeB",y="concentration",xindex=148,yindex=2,data=df,location="data/nano_Fe3+/batch_1/result/modeB.png")

# 02.rmse and r2 table (better with mea but I'm quite lazy)
# RMSE
# Mean
meanR=c("meanR",get_rmse(column="meanR",df=df))
meanB=c("meanB",get_rmse(column="meanB",df=df))
meanG=c("meanG",get_rmse(column="meanG",df=df))
# Mode
modeR=c("modeR",get_rmse(column="modeR",df=df))
modeB=c("modeB",get_rmse(column="modeB",df=df))
modeG=c("modeG",get_rmse(column="modeG",df=df))
# All
multiple=c("multiple",get_rmse(column="modeR+modeG+modeB+meanR+meanG+meanB",df=df))
# Combine to make table
rmse_all=rbind(meanR,meanG,meanB,modeR,modeG,modeB,multiple)
colnames(rmse_all)=c("features","rmse")
rmse_all=as.data.frame(rmse_all)
rmse_all$rmse=round(as.numeric(rmse_all$rmse),digit=4)

# R2 
# mean
meanR=c("meanR",get_r2(column="meanR",df=df))
meanB=c("meanB",get_r2(column="meanB",df=df))
meanG=c("meanG",get_r2(column="meanG",df=df))
# mode
modeR=c("modeR",get_r2(column="modeR",df=df))
modeB=c("modeB",get_r2(column="modeB",df=df))
modeG=c("modeG",get_r2(column="modeG",df=df))
multiple=c("multiple",get_r2(column="modeR+modeG+modeB+meanR+meanG+meanB",df=df))
# All
r2_all=rbind(meanR,meanG,meanB,modeR,modeG,modeB,multiple)
colnames(r2_all)=c("features","R2")
r2_all=as.data.frame(r2_all)
r2_all$R2=round(as.numeric(r2_all$R2),digit=4)

rmse_all
# features   rmse
# meanR       meanR 0.4666
# meanG       meanG 0.0925
# meanB       meanB 0.5813
# modeR       modeR 0.4654
# modeG       modeG 0.0947
# modeB       modeB 0.5729
# multiple multiple 0.0531
r2_all
# features     R2
# meanR       meanR 0.3729
# meanG       meanG 0.9753
# meanB       meanB 0.0269
# modeR       modeR 0.3761
# modeG       modeG 0.9742
# modeB       modeB 0.0547
# multiple multiple 0.9919

write.table(rmse_all,file="data/nano_Fe3+/batch_1/result/rmse_all.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)
write.table(r2_all,file="data/nano_Fe3+/batch_1/result/r2_all.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)

# 03.Barplot for visualization
library(RColorBrewer)
coul <- brewer.pal(7, "Set2")
# rmse
png("data/nano_Fe3+/batch_1/result/barplot_rmse.png",pointsize=10,width=1000,height=600)
plot=barplot(height=rmse_all$rmse, names=rmse_all$features, xlab="Features",ylab="RMSE",col=coul)
text(plot, y=rmse_all$rmse, labels=rmse_all$rmse, pos=1)
dev.off()
# r2
png("data/nano_Fe3+/batch_1/result/barplot_r2.png",pointsize=10,width=1000,height=600)
plot=barplot(height=r2_all$R2, names=r2_all$features, xlab="Features",ylab="R2",col=coul)
text(plot, y=r2_all$R2, labels=r2_all$R2, pos=1)
dev.off()

setwd("/home/nguyen/Desktop/Projects/smart-optiocal-sensor/")
source("scripts/basic_statistics.R")
source('http://www.sthda.com/upload/rquery_t_test.r')

# 01. Scatter plot full images
df=read.delim("data/nano_Fe3+/batch_2/result/RGB_values.csv",sep=",")
# Draw regression plot for all 6 features
# Mean
regress_nano=simple_regression(x="meanG",y="concentration",xindex=100,yindex=2,data=df,location="data/nano_Fe3+/batch_2/result/meanG.png")
regress_nano=simple_regression(x="meanR",y="concentration",xindex=12,yindex=2,data=df,location="data/nano_Fe3+/batch_2/result/meanR.png")
regress_nano=simple_regression(x="meanB",y="concentration",xindex=148,yindex=2,data=df,location="data/nano_Fe3+/batch_2/result/meanB.png")
# Mode
regress_nano=simple_regression(x="modeG",y="concentration",xindex=100,yindex=2,data=df,location="data/nano_Fe3+/batch_2/result/modeG.png")
regress_nano=simple_regression(x="modeR",y="concentration",xindex=12,yindex=2,data=df,location="data/nano_Fe3+/batch_2/result/modeR.png")
regress_nano=simple_regression(x="modeB",y="concentration",xindex=148,yindex=2,data=df,location="data/nano_Fe3+/batch_2/result/modeB.png")

# 02.rmse and r2 table (better with mea but I'm quite lazy)
# RMSE
# Mean
meanR=c("meanR",get_rmse(column="meanR",df=df))
meanB=c("meanB",get_rmse(column="meanB",df=df))
meanG=c("meanG",get_rmse(column="meanG",df=df))
# Mode
modeR=c("modeR",get_rmse(column="modeR",df=df))
modeB=c("modeB",get_rmse(column="modeB",df=df))
modeG=c("modeG",get_rmse(column="modeG",df=df))
# All
multiple=c("multiple",get_rmse(column="modeR+modeG+modeB+meanR+meanG+meanB",df=df))
# Combine to make table
rmse_all=rbind(meanR,meanG,meanB,modeR,modeG,modeB,multiple)
colnames(rmse_all)=c("features","rmse")
rmse_all=as.data.frame(rmse_all)
rmse_all$rmse=round(as.numeric(rmse_all$rmse),digit=4)

# R2 
# mean
meanR=c("meanR",get_r2(column="meanR",df=df))
meanB=c("meanB",get_r2(column="meanB",df=df))
meanG=c("meanG",get_r2(column="meanG",df=df))
# mode
modeR=c("modeR",get_r2(column="modeR",df=df))
modeB=c("modeB",get_r2(column="modeB",df=df))
modeG=c("modeG",get_r2(column="modeG",df=df))
multiple=c("multiple",get_r2(column="modeR+modeG+modeB+meanR+meanG+meanB",df=df))
# All
r2_all=rbind(meanR,meanG,meanB,modeR,modeG,modeB,multiple)
colnames(r2_all)=c("features","R2")
r2_all=as.data.frame(r2_all)
r2_all$R2=round(as.numeric(r2_all$R2),digit=4)

rmse_all
# features   rmse
# meanR       meanR 0.4666
# meanG       meanG 0.0925
# meanB       meanB 0.5813
# modeR       modeR 0.4654
# modeG       modeG 0.0947
# modeB       modeB 0.5729
# multiple multiple 0.0531
r2_all
# features     R2
# meanR       meanR 0.3729
# meanG       meanG 0.9753
# meanB       meanB 0.0269
# modeR       modeR 0.3761
# modeG       modeG 0.9742
# modeB       modeB 0.0547
# multiple multiple 0.9919

write.table(rmse_all,file="data/nano_Fe3+/batch_2/result/rmse_all.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)
write.table(r2_all,file="data/nano_Fe3+/batch_2/result/r2_all.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)

# 03.Barplot for visualization
library(RColorBrewer)
coul <- brewer.pal(7, "Set2")
# rmse
png("data/nano_Fe3+/batch_2/result/barplot_rmse.png",pointsize=10,width=1000,height=600)
plot=barplot(height=rmse_all$rmse, names=rmse_all$features, xlab="Features",ylab="RMSE",col=coul)
text(plot, y=rmse_all$rmse, labels=rmse_all$rmse, pos=1)
dev.off()
# r2
png("data/nano_Fe3+/batch_2/result/barplot_r2.png",pointsize=10,width=1000,height=600)
plot=barplot(height=r2_all$R2, names=r2_all$features, xlab="Features",ylab="R2",col=coul)
text(plot, y=r2_all$R2, labels=r2_all$R2, pos=1)
dev.off()

setwd("/home/nguyen/Desktop/Projects/smart-optiocal-sensor/")
source("scripts/basic_statistics.R")
source('http://www.sthda.com/upload/rquery_t_test.r')

# 01. Scatter plot full images
df=read.delim("data/nano_Fe3+/batch_3/result/RGB_values.csv",sep=",")
# Draw regression plot for all 6 features
# Mean
regress_nano=simple_regression(x="meanG",y="concentration",xindex=100,yindex=2,data=df,location="data/nano_Fe3+/batch_3/result/meanG.png")
regress_nano=simple_regression(x="meanR",y="concentration",xindex=12,yindex=2,data=df,location="data/nano_Fe3+/batch_3/result/meanR.png")
regress_nano=simple_regression(x="meanB",y="concentration",xindex=148,yindex=2,data=df,location="data/nano_Fe3+/batch_3/result/meanB.png")
# Mode
regress_nano=simple_regression(x="modeG",y="concentration",xindex=100,yindex=2,data=df,location="data/nano_Fe3+/batch_3/result/modeG.png")
regress_nano=simple_regression(x="modeR",y="concentration",xindex=12,yindex=2,data=df,location="data/nano_Fe3+/batch_3/result/modeR.png")
regress_nano=simple_regression(x="modeB",y="concentration",xindex=148,yindex=2,data=df,location="data/nano_Fe3+/batch_3/result/modeB.png")

# 02.rmse and r2 table (better with mea but I'm quite lazy)
# RMSE
# Mean
meanR=c("meanR",get_rmse(column="meanR",df=df))
meanB=c("meanB",get_rmse(column="meanB",df=df))
meanG=c("meanG",get_rmse(column="meanG",df=df))
# Mode
modeR=c("modeR",get_rmse(column="modeR",df=df))
modeB=c("modeB",get_rmse(column="modeB",df=df))
modeG=c("modeG",get_rmse(column="modeG",df=df))
# All
multiple=c("multiple",get_rmse(column="modeR+modeG+modeB+meanR+meanG+meanB",df=df))
# Combine to make table
rmse_all=rbind(meanR,meanG,meanB,modeR,modeG,modeB,multiple)
colnames(rmse_all)=c("features","rmse")
rmse_all=as.data.frame(rmse_all)
rmse_all$rmse=round(as.numeric(rmse_all$rmse),digit=4)

# R2 
# mean
meanR=c("meanR",get_r2(column="meanR",df=df))
meanB=c("meanB",get_r2(column="meanB",df=df))
meanG=c("meanG",get_r2(column="meanG",df=df))
# mode
modeR=c("modeR",get_r2(column="modeR",df=df))
modeB=c("modeB",get_r2(column="modeB",df=df))
modeG=c("modeG",get_r2(column="modeG",df=df))
multiple=c("multiple",get_r2(column="modeR+modeG+modeB+meanR+meanG+meanB",df=df))
# All
r2_all=rbind(meanR,meanG,meanB,modeR,modeG,modeB,multiple)
colnames(r2_all)=c("features","R2")
r2_all=as.data.frame(r2_all)
r2_all$R2=round(as.numeric(r2_all$R2),digit=4)

rmse_all
# features   rmse
# meanR       meanR 0.4666
# meanG       meanG 0.0925
# meanB       meanB 0.5813
# modeR       modeR 0.4654
# modeG       modeG 0.0947
# modeB       modeB 0.5729
# multiple multiple 0.0531
r2_all
# features     R2
# meanR       meanR 0.3729
# meanG       meanG 0.9753
# meanB       meanB 0.0269
# modeR       modeR 0.3761
# modeG       modeG 0.9742
# modeB       modeB 0.0547
# multiple multiple 0.9919

write.table(rmse_all,file="data/nano_Fe3+/batch_3/result/rmse_all.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)
write.table(r2_all,file="data/nano_Fe3+/batch_3/result/r2_all.txt", sep="\t", eol="\n",row.names=FALSE, quote=FALSE)

# 03.Barplot for visualization
library(RColorBrewer)
coul <- brewer.pal(7, "Set2")
# rmse
png("data/nano_Fe3+/batch_3/result/barplot_rmse.png",pointsize=10,width=1000,height=600)
plot=barplot(height=rmse_all$rmse, names=rmse_all$features, xlab="Features",ylab="RMSE",col=coul)
text(plot, y=rmse_all$rmse, labels=rmse_all$rmse, pos=1)
dev.off()
# r2
png("data/nano_Fe3+/batch_3/result/barplot_r2.png",pointsize=10,width=1000,height=600)
plot=barplot(height=r2_all$R2, names=r2_all$features, xlab="Features",ylab="R2",col=coul)
text(plot, y=r2_all$R2, labels=r2_all$R2, pos=1)
dev.off()

ggplot(data=data,aes(x=.data[[x]],y=.data[[y]])) +
  geom_point() +
  geom_smooth(method=lm , color="red", fill="#69b3a2", se=TRUE) +
  theme_ipsum()+
  stat_cor(label.x = xindex, label.y =yindex, aes(label = paste(..rr.label..)), size=font_size) +
  stat_regline_equation(label.x =xindex, label.y =yindex*0.9, size=font_size)+
  stat_cor(label.x = xindex, label.y =yindex*0.8, aes(label = paste(..p.label..)), size=font_size)

