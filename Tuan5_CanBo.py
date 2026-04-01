class CanBo:
    def __init__(self,hoten="",tuoi=0,gioitinh="",diachi=""):
        self.__hoten=hoten
        self.__tuoi=tuoi
        self.__gioitinh=gioitinh
        self.__diachi=diachi
    #Lấy họ tên để tìm kiếm    
    def get_hoten(self):
        return self.__hoten
    def inTTin(self):
        print('Thông tin công nhân/viên chức/người lao động')
        print(f'Họ và tên: {self.__hoten} - {self.__gioitinh} - {self.__tuoi} tuổi')
        print(f'Địa chỉ: {self.__diachi}')
class CongNhan(CanBo):
    def __init__(self,hoten="",tuoi=0,gioitinh="",diachi="",bac=0):
        super().__init__(hoten,tuoi,gioitinh,diachi)
        if 0<(bac)<11:
            self.__bac=bac
        else:
           self.__bac=0
           print('Lỗi nhập bậc')
    def inTTin1(self):
        super().inTTin()
        print(f'Bậc của công nhân: {self.__bac}')
class KySu(CanBo):
    def __init__(self,hoten="",tuoi=0,gioitinh="",diachi="",nganhdaotao=""):
        super().__init__(hoten,tuoi,gioitinh,diachi)
        self.__nganhdaotao=nganhdaotao
    def inTTin1(self):
        super().inTTin()
        print(f'Ngành đào tạo: {self.__nganhdaotao}')
class NhanVien(CanBo):
    def __init__(self,hoten="",tuoi=0,gioitinh="",diachi="",congviec=""):
        super().__init__(hoten,tuoi,gioitinh,diachi)
        self.__congviec=congviec
    def inTTin1(self):
        super().inTTin()
        print(f'Công việc: {self.__congviec}')
class QLCB:
    def __init__(self):
        self.danhsach=[]
    def addCB(self,canbo):
        self.danhsach.append(canbo)
        print('Thêm cán bộ thành công')
    def timKiem(self,ten_tim_kiem):
        ket_qua=False
        self.tu_khoa = ten_tim_kiem.strip().lower()
        print(f'Kết quả tìm kiếm cho "{ten_tim_kiem}" là: ')
        for i in self.danhsach:
            if self.tu_khoa in i.get_hoten().lower():
                i.inTTin1()
                print("-" * 25)
                ket_qua=True
        if not ket_qua:
            print('Không tìm thấy cán bộ khớp tên này')
        
    def hienthids(self):
        if not self.danhsach:
            print('Danh sách hiện đang trống')
            return
        
        print("Danh sách cán bộ: ")
        for cb in self.danhsach:
            cb.inTTin1()
            print("-" *25)
def main():
    quan_ly=QLCB() #object QLCB
    
    while True:
        print("\n" + "="*30)
        print(" CHƯƠNG TRÌNH QUẢN LÝ CÁN BỘ")
        print("="*30)
        print("1. Thêm mới cán bộ")
        print("2. Tìm kiếm theo họ tên")
        print("3. Hiển thị thông tin danh sách")
        print("4. Thoát khỏi chương trình")
        
        choice =input("Nhập lựa chọn của bạn: ")
        if choice== '1':
            print("\n-- Chọn loại cán bộ muốn thêm --")
            print("1. Công nhân | 2. Kỹ sư | 3. Nhân viên")
            loai = input("Lựa chọn: ")
            
            if loai not in ['1', '2', '3']:
                print('Lựa chọn không hợp lệ. Vui lòng thử lại!')
                continue #Quay lại While True
            #Nếu dùng else thì phải thụt lề phần còn lại
            hoten = input("Nhập họ tên: ")
            tuoi = int(input("Nhập tuổi: "))
            gioitinh = input("Nhập giới tính: ")
            diachi = input("Nhập địa chỉ: ")
            
            if loai == '1':
                bac = int(input("Nhập bậc (1-10): "))
                cb = CongNhan(hoten, tuoi, gioitinh, diachi, bac)
            elif loai == '2':
                nganh = input("Nhập ngành đào tạo: ")
                cb = KySu(hoten, tuoi, gioitinh, diachi, nganh)
            elif loai == '3':
                viec = input("Nhập công việc: ")
                cb = NhanVien(hoten, tuoi, gioitinh, diachi, viec)
                
            quan_ly.addCB(cb)
            
        elif choice == '2':
            ten = input("\nNhập tên cán bộ cần tìm: ")
            quan_ly.timKiem(ten)
            
        elif choice == '3':
            quan_ly.hienthids()
            
        elif choice == '4':
            print('Thoát chương trình')
            break
        
        else:
            print('Vui lòng nhập lại!')
            
if __name__ =="__main__":
    main()
        