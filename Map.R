library(sf)
library(ggplot2)
library(tmap)
library(tmaptools)
library(leaflet)
library(dplyr)
#Interface between R and Python
library(reticulate)

#This command runs the given script and makes all the resulting objects accessible in R. Eventually
#this will be how we input rates (predicted )
#source_python("C:/Users/jakeo/OneDrive/Documents/M467/Scripts/Team3ForLoop.py")

#read in the shape file, stringsAsFactor makes it easier to join, I think
map <- st_read("C:/Users/jakeo/OneDrive/Documents/Personal/Projects/MontanaCounties_shp/County.shp", stringsAsFactors = FALSE)

#Change labels for CMHD
map$NAMEABBR[which(map$NAMEABBR == "JB" | map$NAMEABBR == "FE" | map$NAMEABBR == "PE"
                   | map$NAMEABBR == "MU" | map$NAMEABBR == "GV" | map$NAMEABBR == "WH")] <- "CMHD"

#Read in the flu data
D <- read.csv("current.csv")
#Transpose the dataset (not entirely necessary, but it's how this particular script is set up)
DT <- t(D)
#Extract rates from the transposed dataset
rates <- as.numeric(c(DT[8:59,15]))
#Extract county abbreviations from the flu dataset and give them the appropriate name (to match the map data)
NAMEABBR <- row.names(DT)[8:59]

#Combine rates and names into a data frame for inner join
test <- data.frame(rates,NAMEABBR)

#Link flu data to county map data in a new dataset
map_and_data <- inner_join(map, test)

#Create a static plot
ggplot(map_and_data) + geom_sf(aes(fill = rates)) + scale_fill_gradient(low = "#56B1F7", high = "#132B43")

#Create a slightly different static plot
tm_shape(map_and_data) + tm_polygons("rates", id = "NAMELABEL", palette = "Greens")

#Change the mode to view, which means interactive HTML widget
tmap_mode("view")
#Recreate the last map, now that the mode has been set to view, to create an interactive map
tmap_last()