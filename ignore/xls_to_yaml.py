#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:26:27 2021

@author: danaukes
"""


import pandas
import yaml
import os
import sys
import math


files = []
files.append('data/research_projects.xlsx')
files.append('data/posters.xlsx')
files.append('data/class_projects.xlsx')
files.append('data/students.xlsx')

def convert(file):
    newfile = os.path.split(file)[1]
    newfile = os.path.splitext(newfile)[0]
    newfile = os.path.join('../','data',newfile+'.yaml')
    newfile = os.path.normpath(os.path.expanduser(newfile))
    
    df = pandas.read_excel(file)
    
    items = []
    
    dict1 = df.to_dict()
    
    for ii in range(len(df)):
        d = {}
        for key in df.keys():
            value = dict1[key][ii]
            # print(value)
            try:
                if not math.isnan(value):
                    d[key] = value
            except TypeError:
                d[key] = value
                    
        items.append(d)
    
    d2 = {}
    d2['keys'] = list(df.columns)
    d2['items'] = items
        
    with open(os.path.expanduser(newfile),'w') as f:
        yaml.dump(items,f)

for item in files:
    convert(item)