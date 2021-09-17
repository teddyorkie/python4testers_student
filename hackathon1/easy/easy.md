# [1] Approximate PI:
Viết hàm approx_pi(n) tính xấp xỉ số PI theo công thức sau, với n là số phần tử của dãy số vô hạn:
```
            PI/4 ~ 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ....
n = 1 --> PI = 4
n = 2 --> PI = 8/3
n = 6 --> PI/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11
```

# [2] Anagram Number:
Viết hàm có đầu vào là một số nguyên và trả ra True nếu sau khi đảo ngược thứ tự các chữ số của số đó vẫn cho ta số ban đầu. Trả ra False nếu không giống.
vd: anagram_number(121121) == True
    anagram_number(1254) == False

# [3] Combine Lists:
Cho 2 list các số nguyên, hãy tạo một list mới sao cho danh sách mới chỉ chứa các số lẻ từ danh sách đầu tiên và các số chẵn từ danh sách thứ hai.
list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

result List is [23, 11, 17, 24, 36, 12]

# [4] Day different:
Viết hàm nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05

# [5] Create Dict:
Cho một dictionary và một list các khóa, hãy tạo một dict mới chỉ bao gồm các khóa đã cho
vd: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york" }
    keys = ["name", "salary"]
Hàm dict_from_keys(sampleDict, keys) sẽ trả ra {'name': 'Kelly', 'salary': 8000}

# [6] :


# [7] Alphabet and Number:
Viết hàm tìm tất cả những từ trong một câu có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
Vd:
str1 = "Emma25 is Data scientist50 and AI Expert"
alpha_num(str1) == ["Emma25", "scientist50"]

# [8] Sort list tuple:
Điểm thi học kỳ của sinh viên được lưu ở định dạng 1 tuple có 3 phần tử (name, midterm, endterm) gồm:
name = (str) tên sinh viên
midterm = (int) điểm thi giữa kỳ
endterm = (int) điểm thi cuối kỳ

Cho một list gồm danh sách điểm thi của tất cả sinh viên 1 lớp. Viết chương trình Python để sắp xếp danh sách trước theo thứ tự giảm dần với thứ tự ưu tiên [Điểm thi cuối kỳ > Điểm thi giữa kỳ > Tên].

Nếu đầu vào là:
[('Tom', 5, 8), 
 ('John', 9, 10), 
 ('Jonny', 8, 10), 
 ('Jason', 10, 10), 
 ('Anna', 3, 8)]

Thì đầu ra sẽ là:
[('Jason', 10, 10), ('John', 9, 10), ('Jonny', 8, 10), ('Tom', 5, 8), ('Anna', 3, 8)]