"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import argparse
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    raise NotImplementedError('VIẾT Ở ĐÂY')


# ---------- Nhiệm vụ E1 · Chỉ số đợt chạy thử ----------
def tinh_chi_so(reqs):
    """Trả về tử số và mẫu số của từng chỉ số, mỗi dòng CSV là một yêu cầu."""
    da_xem_lai = reqs.loc[reqs['duoc_xem_lai'].eq(1)]
    mo_lai = reqs['mo_lai_trong_7_ngay'].eq(1)
    dong_dat = reqs['dong_trong_24h'].eq(1) & reqs['mo_lai_trong_7_ngay'].eq(0)
    bo_qua = da_xem_lai['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    return {
        'Đóng trong 24 giờ, không mở lại trong 7 ngày': (dong_dat.sum(), len(reqs)),
        'Bỏ qua gợi ý': (bo_qua.sum(), len(da_xem_lai)),
        'Mở lại trong 7 ngày': (mo_lai.sum(), len(reqs)),
    }


def in_chi_so(reqs):
    print('E1 · Chỉ số trong đợt chạy thử')
    for ten, (tu_so, mau_so) in tinh_chi_so(reqs).items():
        ty_le = f'{tu_so / mau_so:.2%}' if mau_so else 'không xác định'
        print(f'{ten}: {tu_so}/{mau_so} ({ty_le})')


def in_rui_ro_kinh_te(runs, reqs):
    """Đối chiếu riêng hai dòng E2; không thay thế bảng B1 của nhóm."""
    token = (runs['tokens_in'].sum() * GIA_VAO
             + runs['tokens_out'].sum() * GIA_RA) / 1000
    tool = runs['tool_calls'].sum() * GIA_TOOL
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * LUONG_PHUT
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * LUONG_PHUT
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = reqs['ket_qua'].eq('thanh_cong').sum()
    print('E2 · Toàn bộ mẫu, chi phí simulated; chờ đối chiếu B1')
    print(f'Token: {token:.3f}; tool: {tool:.3f}')
    print(f'Xem lại: {xem_lai:.3f}; làm lại: {lam_lai:.3f}')
    print(f'Tổng gốc: {tong:.3f}; số việc thành công: {thanh_cong}')
    if not thanh_cong or not tong:
        print('Không xác định chi phí mỗi việc hoặc mức thay đổi do mẫu số bằng 0')
        return
    print(f'Chi phí gốc: {tong / thanh_cong:.2f} đ/việc (simulated)')
    for ten, tang_them in [('Làm lại gấp đôi', lam_lai), ('Xem lại gấp đôi', xem_lai)]:
        print(f'{ten}: {(tong + tang_them) / thanh_cong:.2f} đ/việc; '
              f'+{tang_them / tong:.2%} (simulated)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--chi-so', action='store_true', help='Chỉ tính ba chỉ số E1')
    parser.add_argument('--rui-ro', action='store_true', help='Đối chiếu hai dòng E2 độc lập với A/B')
    args = parser.parse_args()
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    if args.chi_so or args.rui_ro:
        if args.chi_so:
            in_chi_so(reqs)
        if args.rui_ro:
            in_rui_ro_kinh_te(pd.read_csv('logix_runs.csv'), reqs)
        raise SystemExit(0)

    runs = pd.read_csv('logix_runs.csv')
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
    in_chi_so(reqs)
