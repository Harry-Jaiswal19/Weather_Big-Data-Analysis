#!/usr/bin/env python
# coding: utf-8

# # # # WEATHER DATASET BIG DATA ANALYSIS # # #
# 
# This dataset is in CSV format and we will solve this dataset using pandas dataFrame.
# 

import pandas as pd


#reading the CSV file through the pandas read command.
df = pd.read_csv(r"E:\MY  Data analytics project\Weather Data.csv")

#printing the  imported dataset. 
df


#show the first 10 rows in the data frame.
df.head(10)


#printing the shape of the dataframe.
df.shape


#Printing the index of the dataframe.
df.index



#showing all the columns name which is present in the dataframe.
df.columns




#Printing the data type of the dataframe.
df.dtypes



#printing Unique value in the data frame
df["Weather"].unique()



df.nunique()


df.count()




df.count


df["Weather"].value_counts()



df.info()



df["Wind Speed_km/h"].nunique()



df["Wind Speed_km/h"].unique()



df.head(2)


df.Weather.value_counts()



df[df.Weather=="Clear"]


df.groupby("Weather").get_group("Clear").head(10)


df[df["Wind Speed_km/h"]==4].head(10)



df[(df["Wind Speed_km/h"]==4)& (df["Weather"]=="Snow")]



df[(df["Visibility_km"]>24) |(df["Weather"]=="Snow")]





