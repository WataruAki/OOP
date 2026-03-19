from VD2 import SieuNhan

class QLSN:
    def __init__(self):
        self.danh_sach_sieu_nhan = []

    def them_sieu_nhan(self, sieu_nhan):
        self.danh_sach_sieu_nhan.append(sieu_nhan)

    def hien_thi_danh_sach(self):
        for sieu_nhan in self.danh_sach_sieu_nhan:
            sieu_nhan.hien_thi()

if __name__ == "__main__":
    danh_sach_sieu_nhan = []
    print ("=== CHƯƠNG TRÌNH QUẢN LÍ THÔNG TIN SIÊU NHÂN ===")
    while True:
        print("\nNhập thông tin siêu nhân mới:")
        ten = input("  Tên siêu nhân: ")
        vu_khi = input("  Năng lực chính: ")
        mau_sac = input("  Màu sắc: ")
        
        sieu_nhan_moi = SieuNhan(ten, vu_khi, mau_sac)
        danh_sach_sieu_nhan.append(sieu_nhan_moi)

        tiep_tuc = input("Bạn có muốn nhập thêm siêu nhân không? (y/n): ")
        if tiep_tuc.lower() != 'y':
            break

    print("\n===========================================")
    print("=== DANH SÁCH SIÊU NHÂN TOÀN THẾ GIỚI ===")

    if not danh_sach_sieu_nhan:
        print("Danh sách trống.")
    else:
        for i, sn in enumerate(danh_sach_sieu_nhan):
            print(f"{i + 1}.", end=" ")
            sn.hien_thi()