# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:57:33 2020

@author: hp
"""
import sys
import os
import pandas as pd
import math
import numpy as np

class Topsis:
    def __init__(self,filename):
        if os.path.isdir(filename):
            head_tail = os.path.split(filename)
            data = pd.read_csv(head_tail[1])
        if os.path.isfile(filename):
            data = pd.read_csv(filename)
        self.d = data.iloc[1:,1:].values
        self.features = len(self.d[0])
        self.samples = len(self.d)
    def fun(self,a):
        return a[1]
    def fun2(self,a):
        return a[0]
    def evaluate(self,w = None,im = None):
        d = self.d
        features = self.features
        samples = self.samples       
        if w==None:
           w=[1]*features
        if im==None:
         im=["+"]*features
        ideal_best=[]
        ideal_worst=[]
        for i in range(0,features):
            k = math.sqrt(sum(d[:,i]*d[:,i]))
            maxx = 0
            minn = 1 
            for j in range(0,samples):
                d[j,i] = (d[j,i]/k)*w[i]
                if d[j,i]>maxx:
                    maxx = d[j,i]
                if d[j,i]<minn:
                    minn = d[j,i]
            if im[i] == "+":
                ideal_best.append(maxx)
                ideal_worst.append(minn)
            else:
                ideal_best.append(minn)
                ideal_worst.append(maxx)
        p = []
        for i in range(0,samples):
            a = math.sqrt(sum((d[i]-ideal_worst)*(d[i]-ideal_worst)))
            b = math.sqrt(sum((d[i]-ideal_best)*(d[i]-ideal_best)))
            lst = []
            lst.append(i)
            lst.append(a/(a+b))
            p.append(lst)
        p.sort(key=self.fun)
        rank = 1
        for i in range(samples-1,-1,-1):
            p[i].append(rank)
            rank+=1
        p.sort(key=self.fun2)
        return p


def findTopsis(filename,w,i):
    ob = Topsis(filename)
    res = ob.evaluate(w,i)
    print(res)


def main():
    lst = sys.argv
    length = len(lst)
    if length > 4 or length< 4:
        print("wrong Parameters")
    else:
        w = list(map(int,lst[2].split(',')))
        i = lst[3].split(',')
        ob = Topsis(lst[1])
        res = ob.evaluate(w,i)
        print (res)
        

if __name__ == '__main__':
     main()
        