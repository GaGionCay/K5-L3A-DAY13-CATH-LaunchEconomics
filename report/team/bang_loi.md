# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Chử Thị Ánh · Người gắn nhãn 2: Hà.

**Bộ 1 có Codex hỗ trợ đọc đề bài; Ánh đã review và xác nhận đồng ý cả 20 nhãn ngày 21/11/2026, bao gồm ca 9 giữ nhãn Do người dùng.** Không ghi nhận đã tự gắn độc lập trong 8 phút. Theo RULES.md, hai người phải gắn độc lập trước khi so; không sửa bộ nhãn độc lập sau khi so. Bộ 2 và kết quả đồng thuận còn trống.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |

## Lý do đề xuất bộ 1 để Ánh tự rà

Xem [dẫn chứng từng ca](dan_chung_nhan_C_bo1_Anh.md): nguyên văn 20 ca từ DOCX, nhãn đề xuất, lý do và ghi chú review của Ánh ở ca 9.

Nguồn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục “Hai mươi ca lỗi”. Không phải đáp án chính thức hay kết quả thống nhất với Hà.

| Ca | Lý do |
| --: | --- |
| 1 | Khách nhập thiếu hai chữ số tài khoản. |
| 2 | Trợ lý gọi tool sai loại hàng, gây hoàn thiếu. |
| 3 | Hoàn về ví đúng thiết kế nhưng khách chờ tiền vào ngân hàng. |
| 4 | Thiếu dữ liệu chặng nước ngoài, trợ lý nhận biết giới hạn và chuyển nhân viên. |
| 5 | Hoàn thừa nhưng cả khách lẫn hệ thống không phát hiện, chỉ kiểm toán thấy. |
| 6 | Khách chọn sai mục giao trễ khi thực tế hàng vỡ. |
| 7 | Ghi sổ thất bại nhưng vẫn báo hoàn tiền thành công. |
| 8 | Dẫn điều khoản không tồn tại là trả lời sai dù tiền đúng; chưa có căn cứ gọi là lỗi ngầm. |
| 9 | Khách dùng mã đơn sàn thay mã vận đơn; hướng dẫn phục hồi cũng cần cải thiện. |
| 10 | Đúng chính sách bất khả kháng nhưng không khớp kỳ vọng từ cam kết 24 giờ. |
| 11 | Âm thanh ngoài khả năng xử lý. |
| 12 | Kết quả đúng nhưng chi phí tăng kéo dài mà không ai phát hiện; lỗi ngầm vận hành. |
| 13 | Phí bảo hiểm đối tác ngoài phạm vi; trả lời chung chung là biểu hiện cần sửa. |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền. |
| 15 | Tính sai mức hoàn, nhân viên bắt được trước khi gửi; không phải lỗi ngầm. |
| 16 | Gửi ngay đúng thiết kế nhưng giờ gửi không phù hợp hoàn cảnh. |
| 17 | Bảng giá cũ gây lệch tiền kéo dài mà không ai mở lại; trọng tâm là sai sót không được nhận ra. |
| 18 | Tính đúng nhưng thiếu giải thích khiến khách cho là thiếu. |
| 19 | Yêu cầu vượt cửa sổ dữ liệu 12 tháng, trợ lý nói rõ và chuyển nhân viên. |
| 20 | Thiếu khóa chống trùng làm hoàn hai lần; lỗi hệ thống dù khách gửi lại. |
