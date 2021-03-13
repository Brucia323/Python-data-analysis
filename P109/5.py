""" 找一段英文文本，统计该文本中单词的出现次数。比如“How are you. How are you.”的统计结果是{“how”:2，“are”:2，“you”:2} """
str = "How are you. How are you."
str = str.lower()
l = []
l = str.split(' ')
result = {}
for word in l:
    if word in result.keys():
        result[word] += 1
    else:
        result[word] = 1
print(result)
