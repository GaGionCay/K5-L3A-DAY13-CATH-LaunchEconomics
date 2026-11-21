"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from pathlib import Path
from statistics import NormalDist

import pandas as pd
import yaml

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ D · Cấu hình pilot ----------
PILOT_CONFIG_PATH = Path(__file__).resolve().parents[1] / 'report' / 'team' / 'pilot_01an.yaml'


def co_mau_hai_ty_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhánh cho phép thử hai tỷ lệ, làm tròn lên."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
                     / (p2 - p1) ** 2)


def tai_cau_hinh_pilot(path=PILOT_CONFIG_PATH):
    """Nạp và kiểm tra các tham số D1/D2, reopen rate và luật dừng của pilot."""
    with Path(path).open(encoding='utf-8') as file:
        config = yaml.safe_load(file)
    pilot = config['pilot']
    required = ('scope', 'cost_threshold_vnd', 'sample_size', 'reopen_rate',
                'identifiability', 'stop_rules')
    missing = [key for key in required if key not in pilot]
    if missing:
        raise ValueError(f'Thiếu khóa cấu hình pilot: {", ".join(missing)}')
    if pilot['assignment']['unit'] != 'staff' or pilot['primary_metric']['clusters_per_arm'] < 20:
        raise ValueError('Pilot phải phân bổ theo nhân viên với ít nhất 20 cụm mỗi nhánh.')
    if pilot['primary_metric']['n_per_arm'] != pilot['sample_size']['accepted_n_per_arm']:
        raise ValueError('n_per_arm phải khớp cỡ mẫu MDE đã chấp nhận.')
    sample = pilot['sample_size']
    if co_mau_hai_ty_le(0.70, 0.75) != sample['request_randomized_n_per_arm']:
        raise ValueError('Cỡ mẫu D1 cho chia theo yêu cầu không khớp.')
    if co_mau_hai_ty_le(0.70, 0.70 + sample['accepted_mde']) != sample['accepted_n_per_arm']:
        raise ValueError('Cỡ mẫu D1 cho MDE đã chấp nhận không khớp.')
    reopen = pilot['reopen_rate']
    if not 0 < reopen['relative_stop_gap'] < reopen['absolute_stop_ceiling'] < 1:
        raise ValueError('Ngưỡng reopen rate không hợp lệ.')
    if len(pilot['stop_rules']) < 3 or any(not all(word in rule for word in ('NẾU', 'TRONG', 'THÌ', 'KHÔNG THÌ'))
                                           for rule in pilot['stop_rules']):
        raise ValueError('Mỗi luật dừng phải có NẾU – TRONG – THÌ – KHÔNG THÌ.')
    return pilot


def danh_gia_reopen_rate(reqs, pilot):
    """Áp dụng phạm vi và ngưỡng reopen trong config vào dữ liệu baseline."""
    scope = ('noi_dia', 'hang_nang')
    baseline_scope = reqs.loc[reqs['loai'].isin(scope), 'mo_lai_trong_7_ngay'].mean()
    reopen = pilot['reopen_rate']
    return {
        'baseline_all': reqs['mo_lai_trong_7_ngay'].mean(),
        'baseline_scope': baseline_scope,
        'relative_stop_gap': reopen['relative_stop_gap'],
        'absolute_stop_ceiling': reopen['absolute_stop_ceiling'],
        'cost_threshold_vnd': pilot['cost_threshold_vnd'],
    }


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


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    pilot = tai_cau_hinh_pilot()
    print('Pilot D · reopen/cost:', danh_gia_reopen_rate(reqs, pilot))
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # Nhiệm vụ D: cấu hình, cỡ mẫu và ngưỡng pilot đã được nạp ở trên.
