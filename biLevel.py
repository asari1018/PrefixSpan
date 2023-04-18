from count_freq import count_freq
from postfix import postfix
from makeFreq import makeFreq
import copy

S1 = [ [0], [0,1,2], [0,2], [3], [2,5] ]
S2 = [ [0,3], [2], [1,2], [0,4] ]
S3 = [ [4,5], [0,1], [3,5], [2], [1] ]
S4 = [ [4], [6], [0,5], [2], [1], [2] ]
DB = [S1, S2, S3, S4]

all_elem = [[0], [1], [2], [3], [4], [5], [6]]

minsup = 2


def biLevel(DB, all_elem, minsup):
    DBcopy = copy.deepcopy(DB)
    # find the length-1 sequential patterns
    freq = []
    for i in all_elem:
        if count_freq(DBcopy, [i]) >= minsup:
            freq.append([i])
    
    # initialize matrix
    mat = []
    for i in range(len(freq)):
        mat.append([])
        for j in freq:
            mat[i].append([])

    # make <x:length-1> - projectedDB
    len1_projected_DBs = []
    for i in range(len(freq)):
        DBcopy = copy.deepcopy(DB)
        projected_DB = []
        for num in range(len(DBcopy)):
            projected_DB.append(postfix(DBcopy[num],[[i]]))
        len1_projected_DBs.append(projected_DB)
    
    # second step: len(freq) * len(freq) matrix (len1)
    for i in range(len(freq)):
        for j in range(len(freq)):
            if i==j:
                mat[i][j] = count_freq(len1_projected_DBs[i],[[i],[j]])
            elif i<=j:
                mat[i][j] = [count_freq(len1_projected_DBs[i],[[i],[j]]),
                             count_freq(len1_projected_DBs[j],[[j],[i]]),
                             count_freq(len1_projected_DBs[i],[[i,j]])]

    for i in mat:
        print(i)