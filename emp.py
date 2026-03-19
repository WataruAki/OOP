class NhanVien:
    LUONG_MAX: float = 36000000.0 

    def __init__(self, ten_nhan_vien: str, luong_co_ban: float, he_so_luong: float):
        self.__tenNhanVien = ten_nhan_vien
        self.__luongCoBan = luong_co_ban
        self.__heSoLuong = he_so_luong

    def get_ten_nhan_vien(self) -> str:
        return self.__tenNhanVien

    def set_ten_nhan_vien(self, ten: str):
        self.__tenNhanVien = ten

    def get_luong_co_ban(self) -> float:
        return self.__luongCoBan

    def set_luong_co_ban(self, luong: float):
        self.__luongCoBan = luong

    def get_he_so_luong(self) -> float:
        return self.__heSoLuong

    def set_he_so_luong(self, he_so: float):
        self.__heSoLuong = he_so

    def tinh_luong(self) -> float:
        return self.__luongCoBan * self.__heSoLuong

    def in_ttin(self):
        print(f"Nhân viên: {self.__tenNhanVien} | Lương CB: {self.__luongCoBan:,.0f} | Hệ số: {self.__heSoLuong} | Tổng lương: {self.tinh_luong():,.0f}")

    def tang_luong(self, delta: float) -> bool:
        he_so_moi = self.__heSoLuong + delta
        luong_moi = self.__luongCoBan * he_so_moi

        if luong_moi > NhanVien.LUONG_MAX:
            print(f"-> Thất bại: Lương mới ({luong_moi:,.0f}) vượt giới hạn LUONG_MAX ({NhanVien.LUONG_MAX:,.0f}).")
            return False
        else:
            self.__heSoLuong = he_so_moi
            print(f"-> Thành công: Hệ số lương đã được tăng thêm {delta}.")
            return True


if __name__ == "__main__":

    nv1 = NhanVien("Nguyễn Văn A", 5000000, 2.5)
    
    print("=== THÔNG TIN BAN ĐẦU ===")
    nv1.in_ttin()

    print("\n=== THỬ TĂNG LƯƠNG LẦN 1 (Tăng hệ số thêm 1.5) ===")
    nv1.tang_luong(1.5)
    nv1.in_ttin()

    print("\n=== THỬ TĂNG LƯƠNG LẦN 2 (Tăng hệ số thêm 5.0) ===")
    
    nv1.tang_luong(5.0)
    nv1.in_ttin()