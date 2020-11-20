import numpy as np
import pandas as pd
def analize(_dict):
   df = pd.DataFrame(data=_dict)
   df2 = df + 10.0002
   col = df.index.to_list()
   i1  =  df.values.tolist()
   print((type(i1)))
   i2  =  df2.values.tolist()
   ##
   _dict.clear
   _dict['column': col]
   _dict['index1': i1]
   _dict['index2': i2]
   return _dict
