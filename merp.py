# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:45:23 2016

@author: DegaLaman
"""
import random

allowed_starts = ['m','d','f','g','sn','fl','gl','sl','t','n']
allowed_ends = ['','','','','','','y','y']

def generate_merp(n):
    res = ''
    for each in range(n):
        res += random.choice(allowed_starts)\
        + 'erp'\
        + random.choice(allowed_ends)
    return res