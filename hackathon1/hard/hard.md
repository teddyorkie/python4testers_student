# [1] Sort letters digits
Bạn được cung cấp một chuỗi chỉ chứa các ký tự chữ và số.
Nhiệm vụ của bạn là sắp xếp chuỗi theo cách sau:

Tất cả các chữ cái thường (theo thứ tự abc) được sắp đứng trước các chữ cái viết hoa.
Tất cả các chữ cái viết hoa (theo thứ tự abc) sẽ đứng trước các chữ số.
Tất cả các chữ số lẻ (từ nhỏ đến lớn) đứng trước các chữ số chẵn (từ nhỏ đến lớn).

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
# [4] Vé PowerPlay Vietlott
Truy cập trang web https://vietlott.vn/vi/choi/power-6-55/cach-choi, vào mục (3) Điền thông tin trên thẻ chọn số. Phần thông tin chơi bao, có giải thích cách chọn chơi bao của game Vietlott 6/45. Viết hàm nhận vào kiểu chơi bao và bộ số người dùng chọn, trả ra tất cả các số vé hệ thống sẽ mua cho bạn.

vd: power_6_45_ticket(7, [3, 5, 7, 8, 13, 23, 42]) trả ra
[(3, 5, 7, 8, 13, 23), (3, 5, 7, 8, 13, 42), (3, 5, 7, 8, 23, 42), (3, 5, 7, 13, 23, 42), (3, 5, 8, 13, 23, 42), (3, 7, 8, 13, 23, 42), (5, 7, 8, 13, 23, 42)]