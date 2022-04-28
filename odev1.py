# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:18:59 2022

@author: Ilayda


Input takes space separated values, however direct copy-paste of the sample input takes a list of 6. 
In order to determine the input for both Alice and Bob, 
press enter after writing the scores for Alice to continue entering the scores for Bob.
"""
a = list(map(int, input().split()))
b = list(map(int, input().split()))

  
def compareTriplets(a, b):
    if len(a) == len(b)  and len(a)==3: #checking the boundaries for the ratings
        a1=all(i > 0 and i< 101 for i in a)== True 
        b1=all(c2 > 0 and c2< 101 for c2 in b)== True
        if a1 == b1: #if all the constraints checks out comparison will follow through
            score=[0]*2
            for i in range(len(a)):
                if a[i]>b[i]:
                    score[0]=score[0]+1
                elif a[i]<b[i]:
                    score[1]=score[1]+1
            print(*score)
        else: #if scores aren't between 0 and 100
            print('exceeds limits')
    else: #if the length isn't 3 for both Alice and Bob
        print('wrong length')
        
compareTriplets(a, b)