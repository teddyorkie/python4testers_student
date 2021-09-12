# [1] String processing

Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.

- Giả sử đầu vào là: hello world and practice makes perfect and hello world again
- Thì đầu ra là: again and hello makes perfect practice world

Gợi ý:
* Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
* Sử dụng set để loại bỏ dữ liệu trùng lặp tự động và dùng sorted() để sắp xếp dữ liệu.

# [2] Ceasar cipher:

Mật mã này (có thể) được phát minh và sử dụng bởi Gaius Julius Caesar và quân đội của ông ta trong Chiến tranh Gallic. Ý tưởng khá đơn giản - mọi chữ cái của thông điệp được thay thế bằng chữ cái tiếp theo trong bảng chữ cái (A trở thành B, B trở thành C, v.v.). Ngoại lệ duy nhất là Z, trở thành A.

Hoàn thiện 2 hàm trong file ceasar.py để mã hóa và giải mã những thông điệp này.

# [3] Tên chuẩn IBAN (Số tài khoản ngân hàng quốc tế) 

IBAN cung cấp một phương pháp đơn giản và khá tin cậy để xác thực số tài khoản chống lại các lỗi đơn giản có thể xảy ra trong quá trình nhập số tk từ các tài liệu giấy, như biên nhận hoặc hóa đơn, vào máy tính.

Số tài khoản tuân thủ IBAN bao gồm:
* mã quốc gia gồm hai chữ cái được lấy từ tiêu chuẩn ISO 3166-1 (ví dụ: FR cho Pháp, GB cho Anh, DE cho Đức, v.v.)
* hai chữ số kiểm tra được sử dụng để thực hiện kiểm tra tính hợp lệ nhanh chóng và đơn giản, nhưng không hoàn toàn đáng tin cậy, cho thấy một số tk là không hợp lệ (do lỗi đánh máy) hoặc trông có vẻ tốt;
* số tài khoản thực (tối đa 30 ký tự chữ và số - độ dài của phần đó tùy thuộc vào quốc gia).

Xác nhận theo các bước sau (Wikipedia):

1. Kiểm tra xem tổng độ dài IBAN có đúng theo quốc gia không (chương trình này sẽ không làm điều đó, nhưng bạn có thể sửa đổi mã để đáp ứng yêu cầu này nếu bạn muốn; lưu ý: bạn phải cho code biết trước tất cả độ dài được sử dụng)
2. Di chuyển bốn ký tự đầu tiên đến cuối chuỗi (tức là mã quốc gia và các số kiểm tra)
3. Thay mỗi chữ cái trong chuỗi bằng hai chữ số, từ đó mở rộng chuỗi, trong đó A = 10, B = 11 ... Z = 35;
4. Xem chuỗi đó là dạng số nguyên và tính phần dư của số đó khi chia cho 97; Nếu phần dư là 1, nghĩa là pass bài test và IBAN có thể hợp lệ.

# [4] Roman to Integer
Các chữ số La Mã được thể hiện bằng bảy biểu tượng khác nhau: I, V, X, L, C, D và M với
I=1; V=5; X=10; L=50; C=100; D=500; M=1000

Ví dụ: 2 được viết là II bằng số La Mã, chỉ là hai chữ cái được thêm vào với nhau. 12 được viết là XII, đơn giản là X + II. Con số 27 được viết là XXVII, là XX + V + II.

Chữ số La mã thường được viết từ lớn nhất đến nhỏ nhất từ trái sang phải. Tuy nhiên, chữ số cho bốn không phải là IIII. Thay vào đó, số bốn được viết là IV. Bởi vì cái đứng trước năm, chúng ta trừ nó ra làm bốn. Nguyên tắc tương tự cũng áp dụng cho số chín, được viết là IX. Có sáu trường hợp phép trừ được sử dụng:

I có thể được đặt trước V (5) và X (10) để tạo thành 4 và 9.
X có thể được đặt trước L (50) và C (100) để tạo ra 40 và 90.
C có thể được đặt trước D (500) và M (1000) để tạo thành 400 và 900.
Cho một chữ số la mã, hãy chuyển nó thành một số nguyên.