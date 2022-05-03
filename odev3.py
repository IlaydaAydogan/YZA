# -*- coding: utf-8 -*-
"""
Created on Sun May  1 10:43:15 2022

@author: Ilayda

"""

def minE(min_en, h): #takes the guessed mininum energy and the lego heights
    for i in range((len(h))):
        if min_en<=0: #if mininum energy is 0 or below, then the ball can't jump over the next lego
            return 0
        elif min_en<h[i]:
            new_en=min_en-(h[i]-min_en)
            min_en=new_en
        elif min_en>=h[i]:
            new_en=min_en+(min_en-h[i])
            min_en=new_en
        else:
            return 0

print("Enter the number of legos: ")
n = int(input())
print("Enter the height of legos: ")
h = list(map(int, input().split()))

if n>0 and n<=10**5: #function limitations 
    if len(h)==n:
        min_en= h[0] #starts with a guessed initial energy that can jump over the first lego
        new_en=min_en+(min_en-h[0])
        min_en=new_en
        while minE(min_en, h)==0: #if the minE function returns a 0, 1 is added to the guessed minimum energy
            min_en +=1   
        print("Minimum energy required to complete the path is " + str(min_en))
    else:
        print("number of legos don't match the given heights for the legos")
    
