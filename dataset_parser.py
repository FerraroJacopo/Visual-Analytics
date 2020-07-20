import pandas as pd
import numpy as np


data=pd.read_csv("vgsales.csv", error_bad_lines=False, na_filter=True)
data.Global_Sales.replace(np.nan,0,inplace=True)
data.NA_Sales.replace(np.nan,0,inplace=True)
data.PAL_Sales.replace(np.nan,0,inplace=True)
data.JP_Sales.replace(np.nan,0,inplace=True)
data.Other_Sales.replace(np.nan,0,inplace=True)
data.Platform.replace(np.nan,"NA",inplace=True)
data.ESRB_Rating.replace(np.nan,"NP",inplace=True)
data.Critic_Score.replace(np.nan,0,inplace=True)
data.User_Score.replace(np.nan,0,inplace=True)
data.Total_Shipped.replace(np.nan,0,inplace=True)
data['Global_Sales']+=data['Total_Shipped']
data = data.drop('Total_Shipped', axis=1)
data = data.drop(data[data.Global_Sales == 0.0].index)
data = data.drop(data[(data.Year == 2020.0)].index)
data = data.drop(data[(data.Year < 1978)].index)
data.to_csv("vgsales_total.csv")
print("vgsales_total esportato")
data = data.drop(data[(data.NA_Sales == 0.0) & (data.JP_Sales == 0.0) & (data.PAL_Sales == 0.0) & (data.Other_Sales == 0.0)].index)
data.to_csv("vgsales_map.csv")
print("vgsales_map esportato")
data=pd.read_csv("vgsales_total.csv", error_bad_lines=False)
data = data.drop(data[data.Critic_Score == 0.0].index)
data.to_csv("vgsales_critic.csv")
print("vgsales_critic esportato")
