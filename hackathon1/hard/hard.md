# [1] Sort list tuple:
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

# [2] Mortgage Payment
Công thức tính số tiền phải trả ngân hàng hàng tháng sau khi vay mua nhà là 
```
    P * (r/12) * (1 + r/12)^n
M = -------------------------
        (1 + r/12)^n - 1
```
trong đó M = số tiền phải trả hàng tháng
         P = số tiền đã vay
         r = lãi suất năm
         n = số tháng còn phải trả.

Viết hàm tính M với đầu vào là P, số năm, và % lãi suất

# [3] Container Max Water
Cho mảng A chứa độ cao của các phương án xây tường đập chứa nước. Tìm 2 phần tử trong A sao cho phương án này chứa được nhiều nước nhất có thể.
Vd: A = [1,8,6,2,5,4,8,3,7] thể hiện độ cao của các tường ngăn ở vị trí index tương ứng. Lượng nước chứa được nhiều nhất là giữa tường số 1 và số 8 là = 7 * (8-1) = 49

```
8      x              x
7      x--------------x-----x
6      x  x           x     x
5      x  x     x     x     x
4      x  x     x  x  x     x
3      x  x     x  x  x  x  x
2      x  x  x  x  x  x  x  x
    0  1  2  3  4  5  6  7  8
```
