list_numbers = [8, 3, 2, 4, 5, 6, 9]
print(list_numbers.count)
exit(0)


def summ():
    return summ(list_numbers)


print(summ)


def odd_number():
    # odd = []
    # odd.append(num)
    # return odd
    return [n for n in list_numbers if n % 2 != 0]


print(odd_number)


def max():
    return max(list_numbers)


print(max)

# Tom version without function summ
# result = 0
# for i in list_numbers:
#    result = result + i
# return result
