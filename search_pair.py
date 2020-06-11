# Дан массив целых чисел array и целое число k. Нужно вывести все уникальные пары чисел из массива, сумма которых равна k.
#
#  Примечание: под уникальностью понимается следующее:
#  если ответу удовлетворяет несколько пар вида (a, b) и (b, a), то достаточно вывести только одну пару (a, b).

#Решим методом 2х указателей

def search_pairs(array, k):
    array.sort()
    left = 0
    right = len(array) - 1
    result = []
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == k:
            result.append((array[left], array[right]))
            left += 1
            right -= 1
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    return [*set(result)]

print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

# - Какая сложность у вашего алгоритма?
#     Сложность алгоритма O(nlog(n))
# - Можно ли его оптимизировать?
#     Если бы массив изначально был отсортирован, то сложность была бы O(n)
