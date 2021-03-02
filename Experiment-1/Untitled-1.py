# Febonacci sequence
'''
斐波那契数列
输入：项数n
输出：前n项
'''
import os


def fibo(n):
    numbers = [1, 1]
    for i in range(n - 2):
        numbers.append(numbers[i] + numbers[i + 1])
    return numbers


answer = fibo(10)
print(answer)
if not os.path.exists('result'):
    os.mkdir('result')
file = open('result/fibo.txt', 'w')
for num in answer:
    file.write(str(num)+' ')
file.close()
