def str_process(s):
    words = [word for word in s.split(" ")]
    return " ".join(sorted(list(set(words))))

def roman_to_int(s):
    lookup = { "I" : 1, "V" : 5, "X" : 10, "L" : 50,
        "C" : 100, "D" : 500, "M" : 1000}
    last_value = 0
    number = 0
    for char in s:
        current_value = lookup[char]
        if current_value <= last_value:
            number += last_value
        else:
            number -= last_value
        last_value = current_value
    number += last_value
    return number