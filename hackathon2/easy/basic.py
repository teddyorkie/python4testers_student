# 1
def morse_code(words):
  x=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
  s=set()
  for i in words:
    temp=''
    for j in i:
      temp += x[ord(j)-97]
    s.add(temp)
  return len(s)

# 2
def reverse_vowels(s):
    slist = list(s)
    vowels = set("aeiouAEIOU")
    i, j = 0, len(s)-1
    while i < j:
        while i < j and s[i] not in vowels:
            i += 1
        while i < j and s[j] not in vowels:
            j -= 1
        if i < j:
            slist[i], slist[j] = slist[j], slist[i]
        i += 1
        j -= 1
    return "".join(slist)