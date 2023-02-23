library(reshape2)
library(ggpubr)
library(hrbrthemes)
library(Metrics)

chisquare_test=function(name=name,reference=reference,df=df){
  df1 <- data.frame(matrix(ncol = 4, nrow = 0))
  colnames(df1)=c("Var1",'Var2',"Freq","value")
  # name="icu"
  # reference="m_status"
  # df=df
  df2=data.frame(table(df[,c(name)],df[,c(reference)]))
  for (i in unique(df2$Var2)){
    # print(i)
    df3=subset(df2,Var2==i)
    df3$value=round(prop.table(df3$Freq)*100,2)
    df1=rbind(df1,df3)
  }
  # Add into ()
  df1$value=paste0(df1$value,"(",df1$value,")")
  # Transform table
  df1=df1[,c("Var1","Var2","value")]
  df2=data.frame(dcast(df1,Var1~Var2))
  df2$feature=name
  df2$p.value=chisq.test(table(df[,c(name)],df[,c(reference)]),simulate.p.value = TRUE)$p.value
  return (df2)
}

# Test chisquare for threshold
chisquare_test_threshold=function(threshold=threshold,name=name,reference=reference,df=df){
  # Create contigentable
  # threshold=5
  # reference="gender"
  # df=df
  # name="numberpeopleinfamily"
  df1 <- data.frame(matrix(ncol = 4, nrow = 0))
  colnames(res)=c("Var1",'Var2',"Freq","value")
  new_name=paste0(name,">",threshold)
  df[,c(name)]=df[,c(name)]>threshold
  colnames(df)[which(colnames(df)==name)]=new_name
  df2=data.frame(table(df[,c(new_name)],df[,c(reference)]))
  
  for (i in unique(df2$Var2)){
    # print(i)
    df3=subset(df2,Var2==i)
    df3$value=round(prop.table(df3$Freq)*100,2)
    df1=rbind(df1,df3)
  }
  # Add into ()
  df1$value=paste0(df1$Freq,"(",df1$value,")")
  # Transform table
  df1=df1[,c("Var1","Var2","value")]
  df2=data.frame(dcast(df1,Var1~Var2))
  df2$feature=new_name
  df2$p.value=chisq.test(table(df[,c(new_name)],df[,c(reference)]),simulate.p.value = TRUE)$p.value
  return (df2)
}

# Chisquare table, numeric values will be converted to categorical data using mediean value
table_chisquare=function(df=df,reference=reference){
  res <- data.frame(matrix(ncol = 5, nrow = 0))
  colnames(res)=c("Var1",unique(df[,c(reference)])[1],unique(df[,c(reference)])[2],"feature","p.value")
  
  for (i in colnames(df)){
    if(class(df[,c(i)])!="character"){
      print(i)
      threshold=median(df[,c(i)])
      print(threshold)
      new_name=paste0(i,">",median(df[,c(i)]))
      df[,c(i)]=df[,c(i)]>threshold
      colnames(df)[which(colnames(df)==i)]=new_name
      df2=chisquare_test(name=new_name,reference=reference,df=df)
      res=rbind(res,df2)
    }
    else{
      # i="gender"
      df2=chisquare_test(name=i,reference=reference,df=df)
      res=rbind(res,df2)
    }
  } 
  return (res)
}

boxplot_testing=function(data=data,x=x,y=y,method="t.test",location="/home/nguyen/Desktop/Test.png"){
  p <- ggboxplot(data=data, x = x, y = y,
                 color = x, palette = "jco",
                 add = "jitter")
  # Change method by t test
  p<-p + stat_compare_means(method = method)
  # Savefig using high resolution at desktop
  ggsave(location,dpi=300)
  return (p)
}

simple_regression=function(x=x,y=y,xlab="xlab",ylab="ylab",xindex=10,yindex=100,font_size=5,data=data,location=location){
  p <- ggplot(data=data,aes(x=.data[[x]],y=.data[[y]])) +
    geom_point() +
    geom_smooth(method=lm , color="red", fill="#69b3a2", se=TRUE) +
    theme_ipsum()+
    stat_cor(label.x = xindex, label.y =yindex, aes(label = paste(..rr.label..)), size=font_size) +
    stat_regline_equation(label.x =xindex, label.y =yindex*0.9, size=font_size)+
    stat_cor(label.x = xindex, label.y =yindex*0.8, aes(label = paste(..p.label..)), size=font_size)
  ggsave(location,dpi=300)
  return (p)
}

# Get rmse
get_rmse=function(column="name",df=df){
  model=lm(as.formula(paste0("concentration~",column)),data=df)
  real=df$concentration
  predict=predict(model)
  return (rmse(real,predict))
}
# Get r2
get_r2=function(column="name",df=df){
  model=lm(as.formula(paste0("concentration~",column)),data=df)
  return (summary(model)$r.squared)
}
