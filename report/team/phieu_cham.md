# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): CATH (L3A)
- Nhóm được chấm: 3ConChatLGPT (L3A)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | "Go có điều kiện" khớp chi phí cả hệ thống 0,49× và 0,38× trong phạm vi [simulated]. Nêu các con số bất lợi chính kèm cách xử lý: power 0,64 ở mức 5 điểm → Giám đốc vận hành ký chấp nhận (điều kiện 2); xem lại 100% 11.743–12.415 đ = 0,98–1,03× [simulated] → giảm xem lại theo bậc khi sửa + bỏ < 15% (điều kiện 4); ca 7, 20 → khoá chống trùng (điều kiện 1). Mỗi điều kiện có vai trò và ngày kiểm tra |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Nhãn simulated ở mọi số tính từ cột `_simulated` (mục 1, 2, 3, 7 và ngưỡng 8.000 đ ở mục 6). Phạm vi thu hẹp về noi_dia + hang_nang có lý do bằng số: loại quoc_te 22.515 đ = 1,88× [simulated], thành công 27,3%; loại doi_tac 0,85× [simulated], thành công 54,4%. Góp ý nhỏ: mục 4 ghi "đo từ log thực", trong khi toàn bộ dữ liệu của lab là giả lập (dù hai cột đó không có đuôi `_simulated`) |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Tách được tác động: ngẫu nhiên theo nhân viên 20 + 20 (đủ 20 cụm mỗi nhóm). Đủ mẫu cho mức chênh 6 điểm: m ≥ 299 yêu cầu/người, DE 6,96; nêu rõ power 0,64 nếu tác động thật là 5 điểm. Ba luật dừng có ngưỡng, thời hạn và người có quyền dừng: an toàn +2 điểm hoặc > 6% hoặc ≥ 1 ca hoàn trùng trong 3 ngày → Giám đốc vận hành tắt trong 30 phút; chi phí > 8.000 đ trong 2 tuần → PM thu hẹp về noi_dia; bỏ qua > 40% trong 1 tuần → Trưởng nhóm CSKH. Thêm cơ chế dừng riêng hang_nang khi lệch > 3 điểm so với đối chứng |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Bằng chứng kinh tế ủng hộ pilot trong phạm vi noi_dia + hang_nang: 0,49× cả hệ thống, 0,38× trong phạm vi [simulated]; phạm vi thu hẹp có lý do bằng số; thiết kế có đối chứng ngẫu nhiên, đủ 20 cụm mỗi nhóm, ba luật dừng định lượng. Năm điều kiện đều có vai trò phụ trách và hạn kiểm tra. Hội đồng (bản chấm lại sau khi nhóm cập nhật hồ sơ; bản trước: 20/30) lưu ý thêm: dữ liệu mở lại 7 ngày chỉ đủ sau 7 ngày theo dõi, nên nhóm cần ghi rõ luật nào bảo vệ được tuần đầu.

**Một câu hỏi cho đội trình:** Chỉ số an toàn là mở lại trong **7 ngày**, nên trong tuần đầu của bước rollout 0,10 chưa có cohort nào đủ 7 ngày theo dõi. Trong tuần đầu, luật dừng nào thực sự bảo vệ khách hàng, và nhóm có dùng chỉ báo sớm nào (ví dụ mở lại trong 48 giờ) không?

**Câu trả lời của đội trình (ghi lại tại buổi):** (ghi khi đội trình trả lời tại buổi duyệt chéo)
