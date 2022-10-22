#!/usr/bin/env python
# coding: utf-8

# In[1]:


inputday=input()
inputdate=int(input())
if inputday=="Sunday":
    day=0
if inputday=="Monday":
    day=1
if inputday=="Tuesday":
    day=2
if inputday=="Wednesday":
    day=3
if inputday=="Thursday":
    day=4
if inputday=="Friday":
    day=5
if inputday=="Saturday":
    day=6
date=(day+inputdate-1)
if((date%7)==1):
    print("Monday")
if((date%7)==2):
    print("Tuesday")
if((date%7)==3):
    print("Wednesday")
if((date%7)==4):
    print("Thursday")
if((date%7)==5):
    print("Friday")
if((date%7)==6):
    print("Saturday")
if((date%7)==0):
    print("Sunday")


# In[ ]:




