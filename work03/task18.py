# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый 
# близкий по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input())
num = list(map(int, input().split()))
x = int(input())
min = abs(x - num[0])
index = 0
for i in range(1, n):
    count = abs(x - num[i])
    if count < min:
        min = count
        index = i
print({num[index]})