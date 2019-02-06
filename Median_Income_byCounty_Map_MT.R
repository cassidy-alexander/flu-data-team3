library(sf)
library(ggplot2)
library(tmap)
library(tmaptools)
library(leaflet)
library(dplyr)

#read in the shape file, stringsAsFactor makes it easier to join, I think
map <- st_read("C:/Users/jakeo/OneDrive/Documents/Personal/Projects/MontanaCounties_shp/County.shp", stringsAsFactors = FALSE)

#read in the income data, then convert NAMELABEL to match the data type in map
D <- read.csv("C:/Users/jakeo/OneDrive/Documents/Personal/Projects/ACS_16_5YR_S1901.csv")
D$NAMELABEL <- as.character(D$NAMELABEL)

#Link income data to counties in a new dataset
map_and_data <- inner_join(map, D)

#Create a static plot - This one doesn't work anymore, don't know why. 
#ggplot(map_and_data) + 
  #geom_sf(aes(fill = Median.income)) + scale_fill_gradient(low = "#56B1F7", high = "#132B43")

#Create a slightly different static plot
tm_shape(map_and_data) + 
  tm_polygons("Median.Income", id = "NAMELABEL", palette = "Greens")

#Change the mode to view, which means interactive HTML widget
tmap_mode("view")
#Recreate the last map, now that the mode has been set to view, to create an interactive map
tmap_last()