number = [1, 1, 1]
def f(x): return number[x-3]+number[x-2]+number[x-1]


for i in range(3, 20):
    number.append(f(i))
print(number[19])
