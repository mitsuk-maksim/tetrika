# Факториал числа n равен произведению всех чисел от 1 до n, то есть:
# n! = 1 * 2 * 3 * ... * n
#
# Написать функцию, которая возвращает количество идущих подряд нулей на конце n!.

def get_zeros(n):
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res

print(get_zeros(5))

print(get_zeros(12))