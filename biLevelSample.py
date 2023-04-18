from count_freq import count_freq
from postfix import postfix
import copy

S1 = [ [0], [0,1,2], [0,2], [3], [2,5] ]
S2 = [ [0,3], [2], [1,2], [0,4] ]
S3 = [ [4,5], [0,1], [3,5], [2], [1] ]
S4 = [ [4], [6], [0,5], [2], [1], [2] ]
DB = [S1, S2, S3, S4]

minsup = 2
all_elem = [[0], [1], [2], [3], [4], [5]] #[6] is not freq

mat = [[[],[],[],[],[],[]],
       [[],[],[],[],[],[]],
       [[],[],[],[],[],[]],
       [[],[],[],[],[],[]],
       [[],[],[],[],[],[]],
       [[],[],[],[],[],[]]]


projected = []
for num in range(len(all_elem)):
    DBcopy = copy.deepcopy(DB)
    DB_tmp = []
    for i in range(len(DBcopy)):
        DB_tmp.append(postfix(DBcopy[i],[[num]]))
    projected.append(DB_tmp)



for i in range(6):
    for j in range(6):
        if i==j:
            mat[i][j] = count_freq(projected[i],[[i],[j]])
        elif i<=j:
            mat[i][j] = [count_freq(projected[i],[[i],[j]]),
                        count_freq(projected[j],[[j],[i]]),
                        count_freq(projected[i],[[i,j]])]
for g in projected:
    print(g)


projected2 = []
r_num = 0
l_num = 1
projected_DB = projected[r_num] # <a>-DB
for num in range(len(projected_DB)):# when <ab>-DB
    projected_DB[num] = postfix(projected_DB[num],[[l_num]])


print(projected_DB)
a = [[0],[1]]
DBcopy = copy.deepcopy(projected_DB)
extended = [] #拡張する配列一覧
#[(ab)], [(ac)]... iを最後のアイテム集合に加える
for i in all_elem:
    a_dash = copy.deepcopy(a)#.appendは値が変わってしまうからa_dashに値をコピー
    if a_dash[-1][-1] < i[0]: #前に追加した要素より辞書順で後である(数字が大きい)アイテムのみ加える
        a_dash[-1].append(i[0]) #[[a]]のとき、[[a,a]]
        extended.append(a_dash)
#[a,a], [a,b]... 系列を最後に加える
#a_dash = a #.appendは値が変わってしまうからa_dashに値をコピー
for i in all_elem:
    a_dash = copy.deepcopy(a)#.appendは値が変わってしまうからa_dashに値をコピー
    a_dash.append(i) #[i]は系列で、系列同士を合体して[[a],[a]]
    extended.append(a_dash)

#print("extended patterns are:", extended)
frequents = []
for beta in extended:
    times = count_freq(DBcopy, beta)
    print(beta, ":",times)
    if times >= minsup:#拡張候補から頻出なものを探してfrequentsにまとめておく
            '''print(beta, " is frequent")'''
            frequents.append(beta)

print(frequents)

#mat is len(freq)



'''for num in range(len(all_elem)):
    DBcopy = copy.deepcopy(DB)
    DB_tmp = []
    for i in range(len(DBcopy)):
        DB_tmp.append(postfix(DBcopy[i],[[num]]))
    projected2.append(DB_tmp)

for i in mat:
    print(i)'''