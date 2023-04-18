import prefixSpan

minsup = int(input("enter minsup: "))

#f = open('genTest.data', 'r')
f = open('sample.data', 'r')
data = f.readlines()
f.close

#generatorからのデータを整数型に整形
for line in range(len(data)):
    data[line] = data[line].split()
    data[line] = [int(elem) for elem in data[line]]



cnums = data[-1][0]
maxelm = 0

DB = []
for i in range(cnums):
    DB.append([])

for line in data:
    if line[-1] > maxelm:
        maxelm = line[-1]
    DB[line[0]-1].append(line[3:])

all_elem = []
for i in range(maxelm):
    all_elem.append([i])

'''
#a~g → 0~6で表現  _は-1
S1 = [ [0], [0,1,2], [0,2], [3], [2,5] ]
S2 = [ [0,3], [2], [1,2], [0,4] ]
S3 = [ [4,5], [0,1], [3,5], [2], [1] ]
S4 = [ [4], [6], [0,5], [2], [1], [2] ]
DB = [S1, S2, S3, S4]

all_elem = [[0], [1], [2], [3], [4], [5], [6]]
'''

sequential_patterns = []
prefixSpan.prefixSpan([], minsup, DB, sequential_patterns, all_elem)
print("sequential_patterns are")
for i in sequential_patterns:
    print("    ",i)

#prefixSpan.prefixSpan([], minsup, DB)