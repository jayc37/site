def format(_index,_dict):
    _dict = _dict
    dataSet = []
    for i in range(len(_index)):
        name = _dict[_index[i]]
        lnum1 = name[0]
        lnum2 = name[1]
        knum1 = list(lnum1.keys())[0]
        vnum1 = list(lnum1.values())[0]
        knum2 = list(lnum2.keys())[0]
        vnum2 = list(lnum2.values())[0]
        temp = [_index[i],str(knum1),vnum1,str(knum2),vnum2]
        dataSet.append(temp)
    return dataSet