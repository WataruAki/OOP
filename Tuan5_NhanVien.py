class NhanVien:
    # Bỏ tham số Luong khỏi hàm init vì nó là kết quả tự tính toán
    def __init__(self, ho_ten="", nam_sinh=0, gioi_tinh="", dia_chi="", luong_co_ban=0.0, he_so_luong=0.0, luong_toi_da=0.0):
        self.__ho_ten = ho_ten
        self.__nam_sinh = nam_sinh
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi
        self.__luong_co_ban = luong_co_ban
        self.__he_so_luong = he_so_luong
        self._luong_toi_da = luong_toi_da
        self.Luong = self.__luong_co_ban * self.__he_so_luong

    def inTTin(self):
        print(f'Họ và tên: {self.__ho_ten} | Năm sinh: {self.__nam_sinh} | Giới tính: {self.__gioi_tinh} | Địa chỉ: {self.__dia_chi}')
        print(f'Lương = {self.__luong_co_ban:,.0f} x {self.__he_so_luong} = {self.Luong:,.0f}')

class CongTacVien(NhanVien):
    def __init__(self, ho_ten="", nam_sinh=0, gioi_tinh="", dia_chi="", luong_co_ban=0.0, he_so_luong=0.0, luong_toi_da=0.0, thoi_han_hop_dong="", phu_cap_CTV=0.0):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi, luong_co_ban, he_so_luong, luong_toi_da)  
        self.__thoi_han_hop_dong = thoi_han_hop_dong
        self.__phu_cap_CTV = phu_cap_CTV
        
        self.LuongThucNhan = self.Luong + self.__phu_cap_CTV

    def inTTin1(self):
        super().inTTin()
        print(f'Cộng tác viên - Thời hạn hợp đồng: {self.__thoi_han_hop_dong}')
        print(f'Lương thực nhận = {self.LuongThucNhan:,.0f}')
        print('-----------------------------------------------------------------')

class NhanVienChinh(NhanVien):
    def __init__(self, ho_ten="", nam_sinh=0, gioi_tinh="", dia_chi="", luong_co_ban=0.0, he_so_luong=0.0, luong_toi_da=0.0,vi_tri=""):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi, luong_co_ban, he_so_luong, luong_toi_da)
        self.__vi_tri=vi_tri
    def inTTin1(self):
        super().inTTin()
        print(f'{self.__vi_tri}')
        print('-----------------------------------------------------------------')

class TruongPhong(NhanVien):
    def __init__(self, ho_ten="", nam_sinh=0, gioi_tinh="", dia_chi="", luong_co_ban=0, he_so_luong=0, luong_toi_da=0, ngay_bat_dau_QL="",phu_cap_QL=0.0):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi, luong_co_ban, he_so_luong, luong_toi_da)
        self.ngay_bat_dau_QL=ngay_bat_dau_QL
        self.phu_cap_QL=phu_cap_QL
        self.Luong_thuc_nhan= self.Luong+ self.phu_cap_QL

    def inTTin1(self):
        super().inTTin()
        print(f'Trưởng phòng- Quản lí từ: {self.ngay_bat_dau_QL}- Phụ cấp quản lí: {self.phu_cap_QL}')
        print(f'Lương thực nhận= {self.Luong_thuc_nhan:,.0f}')
        print('-----------------------------------------------------------------')

CTV = CongTacVien ("Tú Sena", 1996, "Nam", "Thành phố Hải Phòng", 5000000, 3.6, 18000000, "12 tháng", 100000)
CTV.inTTin()
NVCT = NhanVienChinh ("Wataru",2007,"Nam","Phú Thọ",10000000,3.35,335503370,"Chuyên viên Kỹ Thuật")
NVCT.inTTin()
TP= TruongPhong ("Zeros",2000,"Nam","Thành phố Hồ Chí Minh",20000000,4,80000000,"01/04/2026",7500000)
TP.inTTin()