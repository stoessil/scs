#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 3 23:59:59 2019

@author: ZHAW

https://www.openstreetmap.org/

"""

import pandas as pd
import bs4 as BeautifulSoup
import requests
page = requests.get("https://www.20min.ch")



soup = BeautifulSoup(page.content, 'html.parser')



df = pd.DataFrame(page)
print(df)
df.to_csv('map.csv')

