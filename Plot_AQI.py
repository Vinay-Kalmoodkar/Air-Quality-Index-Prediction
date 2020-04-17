# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:19:42 2020

@author: vinay
"""

import pandas as pd
import matplotlib.pyplot as plt

#this function returns the respone variable .i.e., PM2.5 of entire year i.e, 365 values 
def avg_data_2013():
    avg_365_days = [] #list which contains average PM2.5 of 365 days
    invalid_strings = ['NoData','PwrFail','---','InVld']
    
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize = 24):
        hour_sum = 0 #sum of 24 hours values
        day_avg = 0 #1 day's average value i.e., sum/24
        data = [] #list which contains 24 hours values
        df = pd.DataFrame(data = rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if(type(i) is int or type(i) is float):
                hour_sum += i
            elif(type(i) is str):
                #if(i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld')
                if i not in invalid_strings:
                    hour_sum += float(i)
                    
        day_avg = hour_sum/24
        avg_365_days.append(day_avg)
        
    return avg_365_days

def avg_data_2014():
    avg_365_days = [] #list which contains average PM2.5 of 365 days
    invalid_strings = ['NoData','PwrFail','---','InVld']
    
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize = 24):
        hour_sum = 0 #sum of 24 hours values
        day_avg = 0 #1 day's average value i.e., sum/24
        data = [] #list which contains 24 hours values
        df = pd.DataFrame(data = rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if(type(i) is int or type(i) is float):
                hour_sum += i
            elif(type(i) is str):
                #if(i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld')
                if i not in invalid_strings:
                    hour_sum += float(i)
                    
        day_avg = hour_sum / 24
        avg_365_days.append(day_avg)
        
    return avg_365_days

def avg_data_2015():
    avg_365_days = [] #list which contains average PM2.5 of 365 days
    invalid_strings = ['NoData','PwrFail','---','InVld']
    
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize = 24):
        hour_sum = 0 #sum of 24 hours values
        day_avg = 0 #1 day's average value i.e., sum/24
        data = [] #list which contains 24 hours values
        df = pd.DataFrame(data = rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if(type(i) is int or type(i) is float):
                hour_sum += i
            elif(type(i) is str):
                #if(i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld')
                if i not in invalid_strings:
                    hour_sum += float(i)
                    
        day_avg = hour_sum / 24
        avg_365_days.append(day_avg)
        
    return avg_365_days

def avg_data_2016():
    avg_365_days = [] #list which contains average PM2.5 of 365 days
    invalid_strings = ['NoData','PwrFail','---','InVld']
    
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize = 24):
        hour_sum = 0 #sum of 24 hours values
        day_avg = 0 #1 day's average value i.e., sum/24
        data = [] #list which contains 24 hours values
        df = pd.DataFrame(data = rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if(type(i) is int or type(i) is float):
                hour_sum += i
            elif(type(i) is str):
                #if(i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld')
                if i not in invalid_strings:
                    hour_sum += float(i)
                    
        day_avg = hour_sum / 24
        avg_365_days.append(day_avg)
        
    return avg_365_days

def avg_data_2017():
    avg_365_days = [] #list which contains average PM2.5 of 365 days
    invalid_strings = ['NoData','PwrFail','---','InVld']
    
    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize = 24):
        hour_sum = 0 #sum of 24 hours values
        day_avg = 0 #1 day's average value i.e., sum/24
        data = [] #list which contains 24 hours values
        df = pd.DataFrame(data = rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if(type(i) is int or type(i) is float):
                hour_sum += i
            elif(type(i) is str):
                #if(i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld')
                if i not in invalid_strings:
                    hour_sum += float(i)
                    
        day_avg = hour_sum / 24
        avg_365_days.append(day_avg)
        
    return avg_365_days

def avg_data_2018():
    avg_365_days = [] #list which contains average PM2.5 of 365 days
    invalid_strings = ['NoData','PwrFail','---','InVld']
    
    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize = 24):
        hour_sum = 0 #sum of 24 hours values
        day_avg = 0 #1 day's average value i.e., sum/24
        data = [] #list which contains 24 hours values
        df = pd.DataFrame(data = rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if(type(i) is int or type(i) is float):
                hour_sum += i
            elif(type(i) is str):
                #if(i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld')
                if i not in invalid_strings:
                    hour_sum += float(i)
                    
        day_avg = hour_sum / 24
        avg_365_days.append(day_avg)
        
    return avg_365_days

if __name__=="__main__":
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    plt.plot(range(len(lst2013)),lst2013,label="2013 data")
    plt.plot(range(len(lst2014)),lst2014,label="2014 data")
    plt.plot(range(len(lst2015)),lst2015,label="2015 data")
    plt.plot(range(len(lst2016)),lst2016,label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()