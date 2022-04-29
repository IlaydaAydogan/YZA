# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:42:58 2022

@author: Ilayda

Please press enter after writing the hour so that minutes can be entered accordingly. 
"""
import inflect

print("Enter the time: ")
h=int(input())
m=int(input())

def timeInWords(h, m):
    time=str()
    if (h in range(0,25))==True and (m in range(0,60))==True: #if the constrainsts aren't checked out prints out of range 
        if m<31: #for the minutes past syntax
            h=h%12
            h=12 if h==0 else h
            h1=inflect.engine().number_to_words(h)#number to word change via inflect
            m1=inflect.engine().number_to_words(m)
            time= m1 + " minutes past " + h1
            time=h1+" o'clock" if m==00 else time
            if m==15 or m==30:
                m1='quarter' if m==15 else 'half'
                time=m1 + " past "+ h1
        elif m>30: #for the minutes to syntax
            h=(h+1)%12
            h=12 if h==0 else h
            h1=inflect.engine().number_to_words(h)
            m=60-m
            m1=inflect.engine().number_to_words(m)   
            m1='quarter' if m==15 else m1
            time=m1 +" minutes to "+h1
    else:
        print("values out of range")
    print(time)
    
timeInWords(h, m)
