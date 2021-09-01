def str_process(s):
    words = [word for word in s.split(" ")]
    return " ".join(sorted(list(set(words))))

def approx_pi(n):
    tong = 0
    k = 1
    for i in range(1, n+1):
        if i % 2 == 1:
            tong = tong + k/i
            k = -k
    return tong * 4
