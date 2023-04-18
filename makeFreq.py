from count_freq import count_freq
import copy

def makeFreq(alpha, DB, all_elem, minsup):
    DBcopy = copy.deepcopy(DB)
    extended = [] #拡張する配列一覧
    #[(ab)], [(ac)]... iを最後のアイテム集合に加える
    for i in all_elem:
        a_dash = copy.deepcopy(alpha)#.appendは値が変わってしまうからa_dashに値をコピー
        if a_dash[-1][-1] < i[0]: #前に追加した要素より辞書順で後である(数字が大きい)アイテムのみ加える
            a_dash[-1].append(i[0]) #[[a]]のとき、[[a,a]]
            extended.append(a_dash)
    #[a,a], [a,b]... 系列を最後に加える
    #a_dash = a #.appendは値が変わってしまうからa_dashに値をコピー
    for i in all_elem:
        a_dash = copy.deepcopy(alpha)#.appendは値が変わってしまうからa_dashに値をコピー
        a_dash.append(i) #[i]は系列で、系列同士を合体して[[a],[a]]
        extended.append(a_dash)

    '''print("extended patterns are:", extended)'''
    frequents = []
    for beta in extended:
        times = count_freq(DB, beta)
        '''print(beta, ":",times)'''
        if times >= minsup:#拡張候補から頻出なものを探してfrequentsにまとめておく
                '''print(beta, " is frequent")'''
                frequents.append(beta)
    return frequents