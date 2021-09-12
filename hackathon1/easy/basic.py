# 1
def approx_pi(n):
    tong = 0
    k = 1
    for i in range(1, n+1):
        if i % 2 == 1:
            tong = tong + k/i
            k = -k
    return tong * 4

# 2
def anagram_number(number):
    original_num = number
    reverse_num = 0
    while (number > 0):
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
    if (original_num == reverse_num):
        return True
    else:
        return False

# 3
def combine_list(list_one, list_two):
    result_list = []

    for num in list_one:
        if (num % 2 != 0):
            result_list.append(num)
    for num in list_two:
        if (num % 2 == 0):
            result_list.append(num)
    return result_list

# 4
def day_diff(release_date, code_complete_day):
    from datetime import datetime

    # 19/12/2021
    date_1 = datetime.strptime(release_date, "%d/%m/%Y").date()
    # 2021-17-05
    date_2 = datetime.strptime(code_complete_day, "%Y-%d-%m").date()

    delta = None
    if date_1 > date_2:
        delta = date_1 - date_2
    else:
        delta = date_2 - date_1
    return delta.days

# 5
def dict_from_keys(inputDict, keys):
    return {k: inputDict[k] for k in keys}

# 6
def reverse_and_swap(sentence):
    result = ''
    reverseWords = sentence[::-1].split(' ')
    for word in reverseWords:
        result += word[::-1].swapcase() + ' '
    return result.strip()

# 7
def alpha_num(sentence):
    res = []
    temp = sentence.split()
    for item in temp:
        if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
            res.append(item)
    return res

# 8
from operator import itemgetter
def sort_list_last(tuples):
    # return sorted(tuples, key=itemgetter(2,1,0), reverse=True)
    return sorted(tuples, key=lambda x: (x[2], x[1], x[0]), reverse=True)

print("Hello class from another path")