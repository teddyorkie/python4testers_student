# [1] Morse Code:
Trước đây người ta dùng Morse Code để truyền tin qua đường điện thoại. Mỗi ký tự tương ứng với một dãy 
các dấu chấm (dots) và gạch (dashes) vd:
* 'a' tương ứng với ".-",
* 'b' tương ứng với "-...",
* 'c' tương ứng với "-.-.", và cứ thế.

Dưới đây là bảng 26 chữ cái tiếng Anh trong Morse Code và ghép các chữ cái này lại ta cũng sẽ có các từ 
tiếng Anh
```
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
```

Cho một list các từ tiếng Anh, viết hàm trả ra số lượng các biểu diễn khác nhau của các từ đó.
Vd: words = ["gin","zen","gig","msg"] kết quả là 2 vì từ gin và zen có biểu diễn giống nhau trong MorseCode:
"gin" -> "--...-."
"zen" -> "--...-."

Tương tự gig và msg cũng có biểu diễn giống nhau
"gig" -> "--...--."
"msg" -> "--...--."
Nên ta chỉ có 2 chuỗi là: "--...-." and "--...--.".

# [2] Reverse Vowels:
Cho chuỗi s các từ tiếng Anh hoặc tiếng Việt không dấu, viết hàm đảo ngược thứ tự tất cả các nguyên âm trong chuỗi và trả ra chuỗi mới
Các chữ cái 'a', 'e', 'i', 'o', và 'u' được xem là nguyên âm và có thể được viết hoa hoặc thường.
vd: s = 'hello' ---> trả ra 'holle'
    s = 'Lop PYTHON' ---> trả ra 'LOp PYTHon'