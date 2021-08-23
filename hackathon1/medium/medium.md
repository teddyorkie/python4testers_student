# [1] Ceasar cipher:

Mật mã này (có thể) được phát minh và sử dụng bởi Gaius Julius Caesar và quân đội của ông ta trong Chiến tranh Gallic. Ý tưởng khá đơn giản - mọi chữ cái của thông điệp được thay thế bằng chữ cái tiếp theo trong bảng chữ cái (A trở thành B, B trở thành C, v.v.). Ngoại lệ duy nhất là Z, trở thành A.

Hoàn thiện 2 hàm trong file ceasar.py để mã hóa và giải mã những thông điệp này.

# [2] Tên chuẩn IBAN (Số tài khoản ngân hàng quốc tế) 

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