import itertools
import numpy as np


'''
minsup = 2 #input("minsup:")#
#a~g → 0~6で表現  _は-1
S1 = [ [0], [0,1,2], [0,2], [3], [2,5] ]
S2 = [ [0,3], [2], [1,2], [0,4] ]
S3 = [ [4,5], [0,1], [3,5], [2], [1] ]
S4 = [ [4], [6], [0,5], [2], [1], [2] ]
DB = [S1, S2, S3, S4]
in1 = S2#
in2 = [[1]]#
'''

#generate postfix
def postfix(a,b):#a is alpha, b is beta and DB is projected DataBase.
    #b = <a b>
    if len(b[-1]) == 1:
        r = l = -1
        for i in range(len(a)):
            if -1 in a[i]:
                continue
            for j in range(len(a[i])):
                if a[i][j] == b[len(b)-1][0]:
                    r = i
                    l = j
                    break
            else:
                continue
            break

        if r == -1:
            return []
        else:
            del a[0:r]
            if len(a[0]) == 1:
                del a[0]
            elif l == 0:
                a[0][0] = -1
            else:
                del a[0][0:l]
                a[0][0] = -1
                if len(a[0]) == 1:
                    del a[0]

        if len(a)==1 and len(a[0])==1 and a[0][0]==-1:
            return []
        if not a:
            return []
        return a
    
    #b = <(ab)>
    else:
        x = b[len(b)-1][len(b[len(b)-1])-1]#アイテム集合の末尾
        r = l = -1
        for i in range(len(a)):
            if -1 in a[i]:
                for j in range(len(a[i])):
                    if a[i][j] == x:
                        r = i
                        l = j
                        '''print(r,l)'''
                        break
                else:
                    continue
                break
            else:#rlがbの位置になるように
                flag = 0 # 上手にbreakできませんでした
                for j in range(len(b[len(b)-1])-1):
                    flag = 1
                    if b[len(b)-1][j] not in a[i]:
                        flag = 0
                        break
                if flag == 1:
                    for j in range(len(a[i])):
                        if a[i][j] == x:
                            r = i
                            l = j
                            break
                    else:
                        continue
                    break    

        #配列処理
        if r == -1:
            return []
        else:
            del a[0:r]
            if len(a[0]) == 1:
                del a[0]
            elif l == 0:
                a[0][0] = -1
            else:
                del a[0][0:l]
                if len(a[0]) == 1:
                    del a[0]
                else:
                    a[0][0] = -1

        #emptyパターン
        if len(a)==1 and len(a[0])==1 and a[0][0]==-1:
            return []
        if not a:
            return []

        return a

'''
print("S1:",postfix(S1, in2, DB))
print("S2:",postfix(S2, in2, DB))
print("S3:",postfix(S3, in2, DB))
print("S4:",postfix(S4, in2, DB))
'''