def count_freq(DB,a): #DB:捜索するデータベース　a:頻度をカウントする系列パターン
    count = 0
    #登場頻度カウント
    #最後が単品の系列だった場合、"_"を含まないアイテム集合に最後の要素があればよい
    if (len(a[-1]) == 1) :
        for i in DB: #DB内全てのデータベース(S1-S4)において
            if (i != None):#空ではない
                for j in i :#S1-S4それぞれの中のアイテム集合において
                    if ((-1 not in j) and (a[-1][0] in j)): #"_"を含まないアイテム集合にあったら
                        count += 1
                        break
        return count
    #最後がアイテム集合だった場合、最後の要素が"_"を含むアイテム中に含まれるか、もしくはそのアイテム集合含むアイテム集合があるかを調べる
    else:
        for i in DB: #DB内全てのデータベース(S1-S4)において
            if (i != None):#空ではない
                for j in i :#S1-S4それぞれの中のアイテム集合において
                    if (-1 in j) and (a[-1][-1] in j):#"_"を含むアイテム集合にあったら
                        '''print(i)'''
                        count += 1
                        break
                    else:
                        flag = 0
                        for k in range(len(a[-1])):
                            flag = 1
                            if a[-1][k] not in j:
                                flag = 0
                                break
                        if flag == 1:
                            count += 1
                            break
        return count