# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input())
sum = 0
while n > 0:
    k = n % 10
    n = n//10
    sum = sum + k
else:
    print(sum)


