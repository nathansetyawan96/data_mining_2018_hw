# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:43:30 2018

@author: Eileen
"""

import numpy as np
from random import randint

def ReadTxt(path):
    f = open(path,encoding='utf-8')
    txtmat = []   
    for line in f.readlines():
        elements = line.split(' ')
        if np.in1d(np.array(elements),np.array([''])).any()==True:
            del elements[elements.index('')]
        elif np.in1d(np.array(elements),np.array(["。"])).any()==True:
            del elements[elements.index("。")]
        elif np.in1d(np.array(elements),np.array(["…"])).any()==True:
            del elements[elements.index("…")]
        txtmat.append(elements)
    f.close()
    return txtmat

#+======================= load 10 best sentences =============================#
sents = ReadTxt('C:/Users/Eileen/NLPfinal/WanTing_DM/webcam/DM_best10examples.txt')
select_sent = sents[randint(0, 9)]

#======================== generate a news sentence ===========================#   
key_places = '高雄' ### ????? u can change here!!!

location=['高雄','台南','台北','彰化','雲林','嘉義','基隆','桃園','新竹','苗栗','屏東','台中','中南部','北部','中部','南部']          
#with open('C:/Users/Eileen/Desktop/AQ_PTT.test7.0', 'w',encoding = 'utf-8-sig') as f:    
with open('C:/Users/Eileen/NLPfinal/WanTing_DM/webcam/AQ_PTT.test7.0', 'w',encoding = 'utf-8-sig') as f:  
    for loc in location:
        if np.in1d(np.array(select_sent),np.array([loc])).any()==True:
            print(loc)
            ind = select_sent.index(loc)
            select_sent[ind] = key_places
            break
        else:
            select_sent = sents[randint(0, 9)]
            break
    f.write(" ".join(select_sent))
