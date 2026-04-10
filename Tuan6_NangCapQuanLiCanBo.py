from abc import ABC, abstractmethod
import os
# --- 1. Custom Exceptions ---
class TuoiKhongHopLe(Exception):
    pass

class BacKhongHopLe(Exception):
    pass

# --- 2. Lớp trừu tượng (Abstract Base Class) ---
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioitinh, diachi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi  # Gọi property setter để validation
        self.gioitinh = gioitinh
        self.diachi = diachi

    # @property + Validation cho Tuổi (18-65)
    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(f"Lỗi: Tuổi {value} không hợp lệ! Tuổi cán bộ phải từ 18 đến 65.")
        self._tuoi = value

    # Abstract Method
    @abstractmethod
    def mo_ta(self):
        """Hàm mô tả loại cán bộ (buộc lớp con phải override)"""
        pass

    # Magic Methods
    def __str__(self):
        return f"Họ tên: {self.hoten:<15} | Tuổi: {self.tuoi} | Giới tính: {self.gioitinh:<4} | Địa chỉ: {self.diachi:<10}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """So sánh bằng nhau dựa trên Họ tên và Tuổi"""
        if isinstance(other, CanBo):
            return self.hoten == other.hoten and self.tuoi == other.tuoi
        return False

    def __lt__(self, other):
        """So sánh nhỏ hơn để sắp xếp theo tên ABC"""
        # Lấy tên cuối cùng trong chuỗi họ tên để so sánh (VD: "Nguyen Van A" -> "A")
        ten_self = self.hoten.split()[-1] if self.hoten else ""
        ten_other = other.hoten.split()[-1] if other.hoten else ""
        return ten_self < ten_other

# --- 3. Các lớp con (Override và Đa hình) ---
class CongNhan(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, bac):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.bac = bac  # Gọi setter validation

    # @property + Validation cho Bậc (1-10)
    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(f"Lỗi: Bậc {value} không hợp lệ! Bậc công nhân phải từ 1 đến 10.")
        self._bac = value

    def mo_ta(self):
        return "Công nhân"

    def __str__(self):
        return f"[{self.mo_ta()}] {super().__str__()} | Bậc: {self.bac}"


class KySu(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, nganhdaotao):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.nganhdaotao = nganhdaotao

    def mo_ta(self):
        return "Kỹ sư"

    def __str__(self):
        return f"[{self.mo_ta()}] {super().__str__()} | Ngành: {self.nganhdaotao}"


class NhanVien(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, congviec):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.congviec = congviec

    def mo_ta(self):
        return "Nhân viên"

    def __str__(self):
        return f"[{self.mo_ta()}] {super().__str__()} | Công việc: {self.congviec}"

class QuanLiCanBo:
    def __init__(self):
        self.danhsach = []

    def addCB(self, canbo):

        if canbo in self.danhsach:
            print("Cảnh báo: Cán bộ này (trùng tên và tuổi) đã tồn tại trong danh sách!")
        else:
            self.danhsach.append(canbo)
            print("-> Thêm cán bộ thành công!")

    def timKiem(self, ten_tim_kiem):
        tu_khoa = ten_tim_kiem.strip().lower()
        print(f"\n--- KẾT QUẢ TÌM KIẾM CHO '{ten_tim_kiem}' ---")
        ket_qua = [cb for cb in self.danhsach if tu_khoa in cb.hoten.lower()]
        
        if ket_qua:
            for cb in ket_qua:
                print(cb) # Gọi __str__
        else:
            print("Không tìm thấy cán bộ nào khớp tên này.")

    def hienthids(self):
        if not self.danhsach:
            print("\nDanh sách hiện đang trống.")
            return
        
        print("\n--- DANH SÁCH CÁN BỘ (Sắp xếp theo Tên ABC) ---")
        # Sử dụng sorted() sẽ tự động gọi magic method __lt__
        for cb in sorted(self.danhsach):
            print(cb) # Đa hình: In thông tin chuẩn theo từng loại cán bộ (Nhờ __str__)

    def luu_file(self, filename="danhsach_canbo.txt"):
        """Dùng Context Manager (with) để lưu file"""
        with open(filename, "w", encoding="utf-8") as f:
            for cb in self.danhsach:
                f.write(str(cb) + "\n")
        print(f"\n-> Đã lưu danh sách vào file '{filename}' thành công!")

    def doc_file(self, filename="danhsach_canbo.txt"):
        """Dùng Context Manager (with) để đọc file (dạng text view)"""
        if not os.path.exists(filename):
            print("\nFile chưa tồn tại, hãy lưu file trước.")
            return
            
        print(f"\n--- NỘI DUNG ĐỌC TỪ FILE '{filename}' ---")
        with open(filename, "r", encoding="utf-8") as f:
            noi_dung = f.read()
            print(noi_dung.strip() if noi_dung else "File trống.")

# --- 5. Hàm Main (Giao diện Console) ---
def main():
    quan_ly = QuanLiCanBo()
    
    while True:
        print("\n" + "="*40)
        print("   CHƯƠNG TRÌNH QUẢN LÝ CÁN BỘ (V2)   ")
        print("="*40)
        print("1. Thêm mới cán bộ")
        print("2. Tìm kiếm theo họ tên")
        print("3. Hiển thị danh sách (Đã sắp xếp)")
        print("4. Lưu danh sách ra File")
        print("5. Đọc danh sách từ File")
        print("6. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            print("\n-- Chọn loại cán bộ --\n1. Công nhân | 2. Kỹ sư | 3. Nhân viên")
            loai = input("Lựa chọn (1-3): ")
            
            if loai not in ['1', '2', '3']:
                print("Lựa chọn không hợp lệ!")
                continue
                
            try:
                hoten = input("Nhập họ tên: ")
                tuoi = int(input("Nhập tuổi (18-65): "))
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
                
            except ValueError:
                print("-> LỖI: Vui lòng nhập số cho Tuổi hoặc Bậc!")
            except TuoiKhongHopLe as e:
                print(f"-> {e}")
            except BacKhongHopLe as e:
                print(f"-> {e}")

        elif choice == '2':
            ten = input("\nNhập tên cán bộ cần tìm: ")
            quan_ly.timKiem(ten)
            
        elif choice == '3':
            quan_ly.hienthids()
            
        elif choice == '4':
            quan_ly.luu_file()