from operator import itemgetter

def sort_list_last(tuples):
    return sorted(tuples, key=itemgetter(2,1,0), reverse=True)


def mortgage_calc(mortgage, years, interest):
    interest /= 100
    interest_monthly = interest / 12

    nper = years * 12
    numerator = interest_monthly * ((1+interest_monthly)**nper)
    denominator = (1+interest_monthly)**nper - 1

    payment = float("{0:.2f}".format(mortgage * numerator / denominator))
    return payment

def max_water_area(height) -> int:
    i, j = 0, len(height)-1
    ans = 0
    while (i < j):
        area = min(height[i], height[j]) * (j-i)
        if area > ans:
            ans = area
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return ans

print(mortgage_calc(8e8, 15, 11))