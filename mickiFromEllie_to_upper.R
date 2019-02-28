####### ####### ####### ####### ####### ####### ####### 
## Ellie Bayat
## Date: July 28, 2018
## Description: Preprocessing the Flu Count data and make a map 
## from  flu count 
####### ####### ####### ####### ####### ####### ####### 
rm(list=ls())
install.packages("xlsx")
install.packages("plyr")
install.packages("ggplot2")
install.packages("Hmisc")
install.packages("maps")
install.packages("readx1")
### libraries
{
  library(plyr)
  library(ggplot2)
  library(xlsx)
  library(Hmisc)
  library(maps)
}

#install.packages("")
### Import data
#setwd("/Users/Elham/Dropbox (Personal)/Missoula Flu/RcodeEllie/")
#source("CleanFluData.R") 
final=read.csv("final.csv")
final=final[,-1]
#library(readx1)
actual_data=read.csv("montana_flu_compiled_master_weekly.csv", header=TRUE)
actual_data$NA.=NULL
colnames(actual_data)=colnames(final)

#setwd("/Users/Elham/Dropbox (Personal)/Missoula Flu/data/")
load(file = "x.rda")
rep.row<-function(x,n){
  matrix(rep(x,each=n),nrow=n)
}
## adding cmhd
aa=data.frame(rep.row(actual_data[,12],6))
colnames(aa)<-NULL
rownames(aa)= c("fergus","golden valley","judith basin" ,"musselshell","petroleum","wheatland")
actual_data=cbind(actual_data[,1:11],t(aa),actual_data[,13:56])

## makes Montana State map

{
  states<-map_data("state")
  mt_df <- subset(states, region == "montana")
  counties <- map_data("county")
  mt_county <- subset(counties, region == "montana")
  #head(mt_county)
}

{
  mt_df <- subset(states, region == "montana")
  counties <- map_data("county")
  mt_county <- subset(counties, region == "montana")
  mt_county$region=mt_county$subregion
  mt_county$subregion=NA 
}


ls=list()
meann=list()
for( i in 1565:1621){
  bh=subset(mt_county,group%in%c(i))
  ls[[i]]=bh
  meaN=apply(ls[[i]][,1:2],2,mean)
  meann[[i]]=meaN
}

df=rbind(ls[[1565]],ls[[1566]],ls[[1567]],ls[[1568]],ls[[1569]],ls[[1570]],
         ls[[1571]],ls[[1578]],ls[[1583]],ls[[1587]],ls[[1597]],ls[[1599]],
         ls[[1618]],ls[[1572]],ls[[1573]],ls[[1574]],ls[[1575]],ls[[1576]],
         ls[[1577]],ls[[1579]],ls[[1580]],ls[[1581]],ls[[1582]],ls[[1584]],
         ls[[1585]],ls[[1586]],ls[[1588]],ls[[1589]],ls[[1590]],ls[[1591]],
         ls[[1593]],ls[[1592]],ls[[1594]],ls[[1595]],ls[[1596]],ls[[1598]],
         ls[[1600]],ls[[1601]],ls[[1602]],ls[[1603]],ls[[1604]],ls[[1605]],
         ls[[1606]],ls[[1607]],ls[[1608]],ls[[1609]],ls[[1610]],ls[[1611]],
         ls[[1612]],ls[[1613]],ls[[1614]],ls[[1615]],ls[[1616]],ls[[1617]],
         ls[[1619]],ls[[1620]])

df_mean=rbind(meann[[1565]],meann[[1566]],meann[[1567]],meann[[1568]],meann[[1569]],meann[[1570]],
              meann[[1571]],meann[[1578]],meann[[1583]],meann[[1587]],meann[[1597]],meann[[1599]],
              meann[[1618]],meann[[1572]],meann[[1573]],meann[[1574]],meann[[1575]],meann[[1576]],
              meann[[1577]],meann[[1579]],meann[[1580]],meann[[1581]],meann[[1582]],meann[[1584]],
              meann[[1585]],meann[[1586]],meann[[1588]],meann[[1589]],meann[[1590]],meann[[1591]],
              meann[[1593]],meann[[1592]],meann[[1594]],meann[[1595]],meann[[1596]],meann[[1598]],
              meann[[1600]],meann[[1601]],meann[[1602]],meann[[1603]],meann[[1604]],meann[[1605]],
              meann[[1606]],meann[[1607]],meann[[1608]],meann[[1609]],meann[[1610]],meann[[1611]],
              meann[[1612]],meann[[1613]],meann[[1614]],meann[[1615]],meann[[1616]],meann[[1617]],
              meann[[1619]],meann[[1620]])

ab=df[!duplicated(df$region),]


#### #### #### #### #### #### #### #### #### ####  
####  count map
#### #### #### #### #### #### #### #### #### #### 

flu=data.frame(County=as.character(x$County),counts=as.numeric(actual_data[20,5:60]))
head(flu)
flu$County=tolower(flu$County)
colnames(flu)=c("County","Flu Count")
rownames(flu)=make.names(toupper(flu[,1]),unique = TRUE)
flu$Long=ab$long
flu$lat=ab$lat


p1=ggplot(flu, aes(map_id = County )) + 
  geom_map(aes(fill =`Flu Count` ), map = df,col="black") + 
  geom_label(aes(x=df_mean[,1],y=df_mean[,2]),colour="black",
             fill=NA,  label=toupper(flu$County),
             size=2.5,fontface="bold",label.size = NA)+
  expand_limits(x = df$long, y = df$lat)+
  scale_fill_gradient( low = "dark grey", high = "#115a9e",name = "Weekly\n Flu cases")+
  labs(x=NULL, y=NULL)+
  theme_classic()+
  theme(
    panel.border = element_blank(),
    panel.background = element_blank(),
    axis.ticks = element_blank(),
    axis.text = element_blank()
  )+
  ggtitle("Montana map")

p1




