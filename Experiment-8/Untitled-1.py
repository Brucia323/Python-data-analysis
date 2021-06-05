# In[0]:
from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv

train = read_csv("train (2).csv")
train = train[train['event_type'] == 'purchase']
train2 = DataFrame()
train2['product_id'] = train['product_id']
train2['user_id'] = train['user_id']
train2 = train2.drop_duplicates()
train2 = train2.reset_index(drop=True)
l2 = list()
for i in range(len(train2)):
    l1 = list()
    id = train2['user_id'][i]
    while(id == train2['user_id'][i]):
        l1.append(train2['product_id'][i])
        i += 1
        if(i == len(train2)):
            break
    l2.append(l1)
# In[1]:


def generateResult(dataset, support):
    C1 = list()
    for i in dataset:
        for j in i:
            C1.append(j)
    C1 = set(C1)
    L1 = list()
    L1_tem = list()
    for i in C1:
        num = 0
        for j in dataset:
            if(i in j):
                num += 1
        print("L1", i, '支持度 = ', num)
        if(num >= support):
            L1.append(i)
        else:
            L1_tem.append([i])
    C2 = list()
    for i in L1:
        for j in L1:
            if(i < j):
                C2.append(sorted([i, j]))
    C2_tem = C2.copy()
    for i in C2_tem:
        for n in L1_tem:
            if(set(n).issubset(set(i))):
                print(i)
                C2.remove(i)
    L2 = list()
    L2_tem = list()
    for i in C2:
        num1 = 0
        for j in dataset:
            if(set(i).issubset(set(j))):
                num1 += 1
        if(num1 >= support):
            print('L2:', i, '支持度 = ', num1)
            L2.append(i)
        else:
            L2_tem.append(i)
    C3 = list()
    for i in L2:
        for j in L2:
            length = len(i)
            set1 = set(i[0:length-1])
            set2 = set(j[0:length-1])
            result = list(set1.difference(set2))
            if(result == [] and list(set(i).difference(set(j))) != []):
                C3_temp = set(i).union(set(j))
                C3.append(sorted(list(C3_temp)))
    C3_df = DataFrame(C3)
    C3 = C3_df.drop_duplicates().values.tolist()
    C3_tem = C3.copy()
    for i in C3_tem:
        for j in L2_tem:
            if(set(j).issubset(set(i))):
                C3.remove(i)
    L3 = list()
    for i in C3:
        num = 0
        for j in dataset:
            if(set(i).issubset(j)):
                num += 1
        print('L3', i, '支持度 = ', num)
        if(num >= support):
            L3.append(i)
    result = list()
    for i in L2:
        for j in L3:
            if(set(i).issubset(set(j))):
                support = calsupport(j, i, dataset)
                confidence = calconfidence(j, dataset)
                sublist = list(set(j)-set(i))
                result.append(
                    [i, sublist, support, confidence, support/confidence])
    for i in result:
        print(i[0], '==>', i[1], '支持度：', i[2], '置信度：', i[3], '提升度：', i[4])


def calsupport(itemset1, itemset2, dataset):
    num1 = 0
    num2 = 0
    for i in dataset:
        if(set(itemset1).issubset(i)):
            num1 += 1
    for i in dataset:
        if(set(itemset2).issubset(i)):
            num2 += 1
            return num1/num2


def calconfidence(itemset, dataset):
    num1 = 0
    length = len(dataset)
    for i in dataset:
        if(set(itemset).issubset(i)):
            num1 += 1
    return num1/length


generateResult(l2, 100)
