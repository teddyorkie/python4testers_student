[1] Logparser

Nhận vào 1 tên tệp. Tệp này là tệp nhật ký của hệ thống Linux mà bạn cần phải test. Xen lẫn giữa các câu lệnh khác nhau là các thông báo cho biết trạng thái của thiết bị. Chúng trông như thế này:
```
Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON
```
Thiết bị có thể có nhiều trạng thái, nhưng chương trình này chỉ quan tâm đến ba giá trị: ON, OFF và ERR.

Chương trình của bạn sẽ phân tích cú pháp tệp nhật ký đã cho và in ra một báo cáo cho biết thời gian thiết bị đã BẬT và những điểm thời gian của khi hệ thống gặp điều kiện ERR.
