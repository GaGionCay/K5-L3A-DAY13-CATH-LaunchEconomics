# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / tổng số yêu cầu | 994/1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số yêu cầu có quyết định `sua` hoặc `bo` trong tập `duoc_xem_lai = 1` / số yêu cầu trong tập này | 48/177 = **27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày, dùng làm chỉ số đại diện cho lỗi lọt đến khách | Số yêu cầu có `mo_lai_trong_7_ngay = 1` / tổng số yêu cầu | 51/1.200 = **4,25%** |
| Dùng | Tỉ lệ yêu cầu của nhánh trợ lý đã hiển thị gợi ý | Số yêu cầu nhánh trợ lý hiển thị ít nhất một gợi ý / tổng số yêu cầu nhánh trợ lý | Đo trong pilot |
| An toàn | Tỉ lệ hoàn sai số tiền trong mẫu kiểm toán | Số yêu cầu được kiểm toán có số tiền đã hoàn khác số tiền đúng / tổng số yêu cầu đã kiểm toán xong | Đo trong pilot |

Các tỉ lệ mô tả đợt chạy thử trên dữ liệu giả lập. Đợt chạy thử chưa có nhóm đối chứng. Tái lập trong thư mục `src/` bằng `python -X utf8 lab13.py --chi-so`.

### Đối chiếu phạm vi pilot đã cấu hình

Theo `pilot_plan.yaml`, chỉ nhận `noi_dia` + `hang_nang` tại D01–D12; dữ liệu lịch sử chỉ có D01–D06. Lọc CSV theo loại và depot trong cấu hình được 982 yêu cầu. Dùng cùng hàm `tinh_chi_so` trên tập đã lọc cho kết quả:

| Chỉ số | Tử số / mẫu số | Tỉ lệ |
| --- | --- | --- |
| Đóng trong 24 giờ, không mở lại 7 ngày | 906 / 982 | 92,26% |
| Bỏ qua gợi ý trong số được xem lại | 27 / 128 | 21,09% |
| Mở lại 7 ngày | 39 / 982 | 3,97% |

Đây vẫn là mô tả dữ liệu giả lập lịch sử, không chứng minh cải thiện do trợ lý và không đại diện dữ liệu chưa có của D07–D12. Ba số toàn bộ mẫu ở E1 giữ nguyên để đối chiếu đề bài. Baseline 0,70 trong thiết kế thử nghiệm là giả định của đề, không thay bằng 92,26%.

## Danh sách event

Mọi event có `event_id`, `event_at`, `request_id` và `trace_id`. Hệ thống cấp `trace_id` khi tạo yêu cầu ở cả hai nhánh và truyền mã này qua các lần chạy, giao diện nhân viên, hệ thống ticket và kiểm toán. Đếm yêu cầu duy nhất theo `request_id`.

| Event | Ai tạo | Thuộc tính bổ sung | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận | `arm`, `staff_id`, `depot`, `loai` | Khi nhận yêu cầu đủ điều kiện pilot |
| `agent_run_completed` | Agent | `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Khi một lần chạy kết thúc, kể cả khi lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `suggestion_id` | Khi hiển thị gợi ý |
| `staff_review_decision` | Giao diện nhân viên | `staff_id`, `suggestion_id`, `decision` (`giu`, `sua`, `bo`), `review_minutes` | Khi nhân viên chốt quyết định xem lại |
| `staff_rework_completed` | Giao diện nhân viên | `staff_id`, `reason`, `rework_minutes` | Khi nhân viên hoàn tất làm lại |
| `ticket_closed` | Hệ thống ticket | `closed_at` | Khi ticket chuyển sang trạng thái đóng |
| `ticket_reopened` | Hệ thống ticket | `reopened_at`, `reason` | Khi ticket mở lại |
| `audit_sample_checked` | Bộ phận kế toán | `audit_batch_id`, `refunded_amount_vnd`, `correct_amount_vnd` | Khi chốt kết quả đối soát của yêu cầu được chọn |
| `input_validation_failed` | Hệ thống tiếp nhận | `field`, `error_code`, `input_type`, `expected_type` | Khi đầu vào không hợp lệ; không ghi đầy đủ số tài khoản vào log |
| `handoff_to_staff` | Agent | `staff_id`, `reason`, `summary_ref` | Khi chuyển sang nhân viên, kể cả thiếu dữ liệu hoặc lỗi ghi sổ |
| `refund_ledger_write` | Dịch vụ sổ cái | `refund_id`, `refund_key`, `idempotency_key`, `order_id`, `amount_vnd`, `status`, `price_version` | Sau mỗi lần thử ghi sổ, kể cả lỗi và lặp |
| `refund_notification_sent` | Dịch vụ thông báo | `refund_id`, `refund_key`, `notification_status`, `claimed_refund_status` | Khi gửi thông báo trạng thái hoàn tiền cho khách |

### Kiểm tra chéo

- **Chỉ số chính:** Lấy mẫu số từ `refund_request_created`. Dùng lần `ticket_closed` đầu tiên trong 24 giờ và kiểm tra `ticket_reopened` trong 7 ngày sau lần đóng đó. Chốt cohort sau ít nhất 8 ngày kể từ lúc tạo yêu cầu.
- **Bỏ qua gợi ý:** Chỉ lấy yêu cầu nhánh trợ lý có `staff_review_decision` hợp lệ (`giu`, `sua`, `bo`). Với mỗi `request_id`, lấy quyết định có `event_at` muộn nhất ở thời điểm chốt dữ liệu, kể cả khi đã có nhiều `suggestion_id`; nếu trùng thời điểm, dùng `event_id` để chọn nhất quán. Mẫu số là số yêu cầu này, tử số là số yêu cầu có quyết định cuối là `sua` hoặc `bo`. Thiếu quyết định hợp lệ thì báo riêng, không coi là `giu`.
- **Mở lại trong 7 ngày:** Cùng cohort với chỉ số chính. Nối `ticket_closed` đầu tiên với `ticket_reopened` trong 7 ngày sau đó và đếm mỗi yêu cầu tối đa một lần. Dùng cùng mốc chốt dữ liệu cho hai nhánh, theo dõi đủ 7 ngày sau lần đóng trước khi kết luận về yêu cầu đã đóng.
- **Hiển thị gợi ý:** Lọc `refund_request_created.arm` theo nhánh trợ lý và nối với `agent_suggestion_shown`.
- **Hoàn sai số tiền:** So sánh hai trường số tiền trong `audit_sample_checked` theo từng đợt kiểm toán tuần và đếm mỗi yêu cầu đã kiểm toán xong một lần.
- **Lỗi nhập và chuyển nhân viên:** Đếm yêu cầu có `input_validation_failed` trên tổng yêu cầu cùng ngày; nhóm `handoff_to_staff` theo `reason`, loại yêu cầu và tuần. Đây là tín hiệu phục vụ bảng khắc phục C.
- **Hoàn trùng:** `refund_key` xác định cùng nghĩa vụ hoàn tiền (đơn, loại phí và lần hoàn hợp lệ), dùng chung khi khách tạo lại yêu cầu. Đếm ít nhất hai `refund_id` khác nhau ghi sổ `status = ok` cho cùng `refund_key`; không coi hai log gửi lặp của cùng giao dịch là hai lần hoàn. Từ một ca xác nhận hoàn trùng, áp dụng luật dừng an toàn của pilot.
- **Báo hoàn nhưng chưa ghi sổ:** Đối soát mỗi giờ các `refund_notification_sent` có `claimed_refund_status = completed` với giao dịch `refund_ledger_write.status = ok` theo `refund_id`; không có bản ghi khớp thì cảnh báo. `price_version` hỗ trợ kiểm toán bảng giá cũ ở ca 17.

### Quy ước đo trong pilot

- Báo cáo riêng theo `arm`, tuần tiếp nhận và phạm vi `loai` đã được chốt trong pilot; không dùng trực tiếp tỉ lệ toàn bộ 1.200 yêu cầu làm kết quả của phạm vi thu hẹp.
- Loại event gửi lặp theo `event_id` trước khi nối bảng; đếm yêu cầu theo `request_id`. Event thiếu mã nối được đưa vào danh sách lỗi dữ liệu để xử lý, không âm thầm bỏ khỏi mẫu số cohort.
- Với yêu cầu đóng muộn, chỉ kết luận chỉ số mở lại sau đủ 7 ngày từ lần đóng đầu tiên. Báo riêng số yêu cầu chưa đủ thời gian theo dõi và số chưa đóng; chưa so sánh an toàn giữa hai nhánh nếu độ trưởng thành dữ liệu khác nhau.
- Mẫu số bằng 0 thì ghi “không xác định”, không ghi 0%. Kiểm toán chỉ phản ánh mẫu đã kiểm tra, không mặc nhiên đại diện toàn bộ yêu cầu.
- Các event có `review_minutes` và `rework_minutes` cho phép thay chi phí thời gian simulated bằng thời gian đo trong pilot. Theo kế hoạch hiện tại: mở lại cao hơn đối chứng ít nhất 2 điểm hoặc vượt 6% trong 3 ngày liên tiếp, hoặc có ít nhất một ca hoàn trùng, thì Giám đốc vận hành tắt trợ lý trong 30 phút. Dùng cohort đủ thời gian theo dõi; không coi yêu cầu chưa đủ 7 ngày là không mở lại.
- Tỉ lệ bỏ qua gợi ý trên 40% trong một tuần: Trưởng nhóm CSKH phỏng vấn 5 nhân viên trong 3 ngày theo luật pilot. Ngưỡng này khác ngưỡng cảnh báo số lượng xem lại trong E2.

## E2 · Rủi ro kinh tế

Đã đối chiếu hai kịch bản dưới đây với [bảng B1 của Cường](bang_chi_phi.md#b1--đổi-từng-yếu-tố) và chạy lại `src/lab13.py` sau merge `d75e1fc`. Phạm vi là toàn bộ 1.200 yêu cầu, với 978 việc thành công. Chi phí gốc là 4.373.585,132 đ, trong đó xem lại 1.780.000 đ và làm lại 2.264.000 đ (đều **simulated**). Mỗi kịch bản cộng thêm đúng khoản chi phí bị nhân đôi vào tổng gốc, chia cho 978. Đây là chi phí biến đổi, chưa cộng chi phí cố định; không phải chi phí riêng của phạm vi pilot thu hẹp.

Tái lập: chạy `python -X utf8 lab13.py --rui-ro` trong `src/` (có thể thêm `--chi-so` để in cả E1). Lệnh E2 dùng chung `mo_hinh` của Cường để lấy chi phí gốc. Chi phí gốc cộng token và tool của mọi lần chạy, kể cả lỗi, cộng hai khoản thời gian simulated; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Chạy `python -X utf8 lab13.py` để đối chiếu trực tiếp toàn bộ A/B; B1 làm tròn phần trăm một chữ số, bảng E2 giữ hai chữ số.

- Làm lại gấp đôi: `(4.373.585,132 + 2.264.000) / 978`; mức tăng `2.264.000 / 4.373.585,132` (**simulated**).
- Xem lại gấp đôi: `(4.373.585,132 + 1.780.000) / 978`; mức tăng `1.780.000 / 4.373.585,132` (**simulated**).
- Các ngưỡng rà trace dưới đây là cảnh báo quản trị bổ sung, không thay thế luật dừng trong pilot. Trong phạm vi lịch sử đã lọc, xem lại là `128/982 = 13,03%`; gấp đôi là `256/982 = 26,07%`. Làm lại có phút simulated dương là `48/982 = 4,89%` (simulated). B1 vẫn tính toàn bộ mẫu; không suy diễn chi phí B1 thành chi phí riêng phạm vi pilot.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi với số phút trung bình mỗi ca giữ nguyên | **6.787 đ/việc thành công (+51,77%, simulated)** | Tỉ lệ làm lại theo tuần vượt 7%, tính từ số yêu cầu có `staff_rework_completed` chia số yêu cầu nhánh trợ lý | Rà tối đa 20 trace làm lại trong tuần, ưu tiên loại có nhiều ca nhất trước khi chuyển bước pilot | PM trợ lý hoàn phí |
| Tỉ lệ xem lại tăng gấp đôi với số phút trung bình mỗi ca giữ nguyên | **6.292 đ/việc thành công (+40,70%, simulated)** | Sau tuần 1 xem lại 100%, tỉ lệ yêu cầu được xem lại trong phạm vi pilot đạt 26,07% trong một tuần, gấp đôi mốc lịch sử 128/982 | Rà tối đa 20 quyết định xem lại theo loại yêu cầu và nguyên nhân, điều chỉnh luồng xem lại trước khi chuyển bước pilot | Trưởng nhóm CSKH |

### Cảnh báo bổ sung từ B4 đã có kết quả

[B4 của Cường](bang_chi_phi.md#b4--nếu-phải-xem-lại-tất-cả) cho thấy xem lại 100% trong phạm vi `noi_dia` + `hang_nang` có chi phí **11.743 đ/việc, 0,98× mức 12.000 đ** nếu làm lại 9 phút/ca; nếu dùng thời gian làm lại trung bình dữ liệu thì lên **12.415 đ/việc, 1,03×** (đều **simulated**, chưa cộng cố định). Vì vậy, event phải đo cả `review_minutes` và `rework_minutes`, không chỉ số ca. Đây là hai kịch bản giả định của B4, không phải chi phí pilot đã đo. Tuần 1 xem lại 100% giữ rollout ở bước hiện tại; chỉ áp dụng Ngưỡng chi phí pilot 8.000 đ/việc, chưa cộng cố định, khi vượt ngưỡng trong 2 tuần liên tiếp. Lý do: **8.000 đ = 0,67× của 12.000 đ, khoảng 2,3 lần 3.414 đ (A4, chưa cộng cố định) [simulated]**.

### Trạng thái bàn giao

- Đã xong: E1; hai dòng E2 khớp B1 của Cường; cảnh báo thời gian xem lại/làm lại có nguồn B4.
- Đã đối chiếu phạm vi, ngưỡng và quyền dừng theo `pilot_plan.yaml` hiện tại; đã bổ sung event cho các tín hiệu C và hoàn trùng. Luật chi phí áp dụng khi vượt 8.000 đ/việc trong hai tuần liên tiếp sau tuần 1; tuần 1 không mở rộng rollout.
- Hà đã ghép chỉ số vào mục 4 và rủi ro vào mục 7 của `ho_so_launch_v0.md`. Các event trên là đặc tả cần triển khai, không phải bằng chứng hệ thống đã phát event thật.
