# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:19:42 2020

@author: vinay
"""

import os 
import time
import requests
import sys

#os.makedirs('Data')

#this function will retrieve the data from the website and stores it in local html files
def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month,year)    
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month,year)
                
            texts = requests.get(url)
            texts_utf = texts.text.encode('utf=8')
            
            if not os.path.exists('Data/Html_data/{}'.format(year)):
                os.makedirs('Data/Html_data/{}'.format(year))
                
            with open('Data/Html_data/{}/{}.html'.format(year,month),'wb') as file:
                file.write(texts_utf)
                
        sys.stdout.flush()

if __name__ == '__main__':
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print('time taken = {}'.format(stop_time-start_time))
    