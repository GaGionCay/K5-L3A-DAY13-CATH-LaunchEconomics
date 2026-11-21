# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: CATH · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống: 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]. Trong phạm vi noi_dia + hang_nang: 4.599 đ = 0,38× (đã cộng cố định 40 triệu/tháng) [simulated] | Giả lập | Người viết code |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: 82,83% đóng trong 24h và không mở lại 7 ngày (994/1.200). Dùng: 27,12% bỏ qua gợi ý (48/177). An toàn: 4,25% mở lại trong 7 ngày (51/1.200) | Xong, có bằng chứng | Người kiểm số |
| 5 · Bảng lỗi và cách khắc phục | hai bộ nhãn khớp 20/20 có AI hỗ trợ; Hà đã tự rà và xác nhận, Ánh đã review và xác nhận ngày 21/11; 5 ca khắc phục đủ 5 loại Google PAIR, mỗi dòng có cách phát hiện đo được và vai trò phụ trách | Xong, có bằng chứng | Người gắn nhãn 1 & 2 |
| 6 · Pilot plan | Chia theo nhân viên, 20 + 20, mức chênh 6 điểm: 859 là cỡ mẫu hiệu dụng mỗi nhóm (DE 6,96), tương ứng 20 nhân viên × 299 = 5.980 yêu cầu thực tế cần thu mỗi nhóm. 3 luật dừng đúng mẫu NẾU–TRONG–THÌ–KHÔNG THÌ. Quyết định: 2027-01-05 | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%) [simulated]. Xem lại 100% → 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút [simulated]. Khối lượng giảm nửa → cố định +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Điều kiện cho Go có điều kiện:**

- Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu pilot → **Kỹ sư trưởng agent**, kiểm tra trước 2026-12-20.
- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power chỉ 0,64 nếu tác động thật là 5 điểm) → **Giám đốc vận hành**, trước 2026-12-15.
- Bật đủ event có `trace_id`; thay phút simulated bằng phút đo thật sau tuần 1 → **Kỹ sư trưởng agent**, kiểm tra cuối tuần 1.
- Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% thì chi phí 11.743 đ = 0,98× gần hoà vốn [simulated] → **Trưởng nhóm CSKH**, kiểm tra cuối bước 0.25.

**Đề xuất:** **Go có điều kiện** cho pilot phạm vi noi_dia + hang_nang (0,22× và 0,69× so với 12.000 đ [simulated]). Loại quoc_te (1,88×) và doi_tac (0,85×). Điều kiện ở trên.
