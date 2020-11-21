def isEven(s): 
    l = len(s) 
    d = False
    for i in range(l - 1, -1, -1 ) : 
        if (s[i] == '0'
           and d == False) : 
             continue
        if (s[i] == '.') : 
            d = True
            continue
        if ((int)(s[i]) % 2 == 0) : 
              return True
        return False

def val1(val,isOdEv):
       _val1 = {}
       _val1[val] = isOdEv
       return _val1

def val2(val,isOdEv):
       _val2 = {}
       _val2[val] = isOdEv
       return _val2