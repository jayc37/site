import numpy as np
import pandas as pd
from oddeven import isEven,val1,val2
def analize(_dict):
       _d = _dict['rates']
       _index = get_keys(_d)
       _values = get_val(_d)
       dataSet = odd_even(_index,_values)
       return _index,dataSet


def odd_even(_index,_value):
       dataSet = {}
       for i in range(len(_index)):
              idx = _index[i]
              vl1 = _value[i]
              _inc = 10.0002 
              t = getlistIndex1(vl1)
              _ls =getlistIndex2(t,vl1,_inc)
              dataSet[idx] = _ls
       return dataSet

def getlistIndex1(vl1):
       _temp = []
       if (isEven(str(vl1))):
              _value1 = val1(vl1,'Even')
              _temp.append(_value1)
       else : 
              _value1 = val1(vl1,'Odd')
              _temp.append(_value1)
       return _temp
def getlistIndex2(_temp,vl,number):
       vl2 = vl + number
       if (isEven(str(vl2))):
              _value2 = val2(vl2,'Even')
              _temp.append(_value2)
       else : 
              _value2 = val2(vl2,'Odd')
              _temp.append(_value2)
       return _temp
def get_keys(_dict):
       return list(_dict.keys())
def get_val(_dict):

       return list(_dict.values())

              
      
# This code is contributed 
# by Nikita Tiwari. 