# [1] Print star:
Viết hàm có đầu vào là số n = số hàng cần in, và in ra hình sau (vd với n == 3)
```
    * * *
    * *
    *
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

# [6] Reverse Word Order and Swap Case:
Cho 1 chuỗi A (vd: "tHE fOX iS cOMING fOR tHE cHICKEN"). Viết hàm đảo ngược thứ tự các từ trong chuỗi và đổi tất cả các chữ cái từ hoa thành thường và ngược lại. (kết quả "Chicken The For Coming Is Fox The")

# [7] Alphabet and Number:
Viết hàm tìm tất cả những từ trong một câu có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
Vd:
str1 = "Emma25 is Data scientist50 and AI Expert"
alpha_num(str1) == ["Emma25", "scientist50"]

# [8] Unique value Dictionary:
Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết hàm để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.

    vd: unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}

Trường hợp trên danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất

    vd: unique_value_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S009', 'S007', 'S002', 'S001', 'S005'}

Trường hợp trên danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.