def sort_break_down(s):
    l,u,o,e=[],[],[],[]
    for i in sorted(input()):
        if i.isalpha():
            x = u if i.isupper() else l
        else:
            x = o if int(i)%2 else e
        x.append(i)
    return "".join(l+u+o+e)

def sort_letter_digit(s):
    def get_key(x):
        if x.islower():
            return (1,x)
        elif x.isupper():
            return (2,x)
        elif x.isdigit() :
            if int(x)%2==1:
                return (3,x)
            else :
                return (4,x)

    return "".join(sorted(s, key=get_key))

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