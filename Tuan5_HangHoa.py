class HangHoa:
    def __init__(self, ma_hang, ten_hang,nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia_ban = gia
    
    def xuat_thong_tin(self):
        print(f"Mã hàng: {self.ma_hang}")
        print(f"Tên hàng: {self.ten_hang}")
        print(f"Nhà sản xuất: {self.nha_sx}")
        print(f"Giá bán: {self.gia_ban} VND")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"Thời gian bảo hành: {self.tg_baohanh}")
        print(f"Điện áp: {self.dien_ap} V")
        print(f"Công suất: {self.cong_suat} W\n")


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia=0)
        self.loai_nguyenlieu = loai_nguyenlieu

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"Loại nguyên liệu: {self.loai_nguyenlieu}\n")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia=0)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan
    
    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"Ngày sản xuất: {self.ngay_sx}")
        print(f"Ngày hết hạn: {self.ngay_hethan}\n")

TUF = HangDienMay("FX517ZC", "Laptop Asus TUF Dash F15", "ASUS", 24000000, "24 tháng", "180V", "150W")
TUF.xuat_thong_tin()

Bat = HangSanhSu("BS001", "Bộ bát sứ", "Minh Long", "Sứ cao cấp")
Bat.xuat_thong_tin()

ThucPham = HangThucPham("TP001", "Sữa tươi", "Vinamilk", "2023-01-01", "2023-07-01")
ThucPham.xuat_thong_tin()