class NhanVien:
    LUONG_MAX=36000000
    def __init__(self,tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien=tenNhanVien
        self.__luongCoBan=luongCoBan
        self.__heSoLuong=heSoLuong
    def get_ten_nhan_vien(self) -> str:
        return self.__tenNhanVien
    
    def set_ten_nhan_vien(self, ten: str):
        self.__tenNhanVien=ten

    def get_luong_co_ban(self) -> float:
        self.__luongCoBan

    def set_luong_co_ban(self, luong: float):
        self.__luongCoBan=luong
    
    def get_he_so_luong(self)->float:
        self.__heSoLuong

    def set_he_so_luong(self, he_so: float):
        self.__heSoLuong=he_so

#Tính lương
    def tinhLuong(self)->float:
        return self.__luongCoBan * self.__heSoLuong
    
#In Thông Tin
    def inTTin(self):
        print (f"Tên Nhân Viên: {self.__tenNhanVien} | Lương cơ bản: {self.__luongCoBan} | Hệ số: {self.__heSoLuong} | Tổng lương: {self.tinhLuong():,.0f}.")

    def tangLuong(self, inc:float):
        he_so_moi = self.__heSoLuong + inc
        luong_moi = self.__luongCoBan * he_so_moi

        if luong_moi > NhanVien.LUONG_MAX:
            print(f"Thất bại,lương mới ({luong_moi:,.0f}) đã vượt quá mức lương tối đa.")
            return False
        else:
            self.__heSoLuong = he_so_moi
            print(f"Thành công, hệ số lương đã tăng thêm {inc}.")
            return True
        



    