import json
import csv
import os

# ================= KHOỞI TẠO CÁC LỚP =================
class CanBo:
    def __init__(self, hoten, tuoi, gioitinh, diachi):
        # Sử dụng 1 dấu gạch dưới (_) cho protected attributes để dễ kế thừa
        self.__hoten = hoten
        self.__tuoi = tuoi
        self.__gioitinh = gioitinh
        self.__diachi = diachi
  
    def get_hoten(self):
        return self.__hoten

    def inTTin(self):
        print(f'Họ và tên: {self.__hoten} - {self.__gioitinh} - {self.__tuoi} tuổi')
        print(f'Địa chỉ: {self.__diachi}')

    def to_dict(self):
        return {
            "hoten": self.__hoten,
            "tuoi": self.__tuoi,
            "gioitinh": self.__gioitinh,
            "diachi": self.__diachi
        }

class CongNhan(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="", bac=0):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.__bac = bac if 0 < bac <= 10 else 0

    def get_bac(self):
        return self.__bac

    def inTTin(self):
        super().inTTin()
        print(f'Bậc của công nhân: {self.__bac}')

    def to_dict(self):
        data = super().to_dict()
        data.update({"loai": "CongNhan", "bac": self.__bac})
        return data

class KySu(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="", nganhdaotao=""):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self._nganhdaotao = nganhdaotao

    def inTTin(self):
        super().inTTin()
        print(f'Ngành đào tạo: {self._nganhdaotao}')

    def to_dict(self):
        data = super().to_dict()
        data.update({"loai": "KySu", "nganhdaotao": self._nganhdaotao})
        return data

class NhanVien(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="", congviec=""):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self._congviec = congviec

    def inTTin(self):
        super().inTTin()
        print(f'Công việc: {self._congviec}')

    def to_dict(self):
        data = super().to_dict()
        data.update({"loai": "NhanVien", "congviec": self._congviec})
        return data

# ================= LỚP QUẢN LÝ =================
class QuanLyCanBo:
    def __init__(self):
        # Yêu cầu 2: Lưu danh sách vào dict với key là họ tên
        self.danhsach = {}
        self.json_file = 'canbo.json'
        # Tự động tải dữ liệu từ JSON khi khởi tạo nếu có
        self.load_from_json()

    # Yêu cầu 1: Đọc dữ liệu từ file CSV
    def doc_csv(self, filename='canbo.csv'):
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row or len(row) < 6: continue
                    hoten, tuoi, gioitinh, diachi, loai, extra = row
                    
                    tuoi = int(tuoi) # Có thể gây ra ValueError nếu không phải số
                    
                    if loai == 'CongNhan':
                        cb = CongNhan(hoten, tuoi, gioitinh, diachi, int(extra))
                    elif loai == 'KySu':
                        cb = KySu(hoten, tuoi, gioitinh, diachi, extra)
                    elif loai == 'NhanVien':
                        cb = NhanVien(hoten, tuoi, gioitinh, diachi, extra)
                    else:
                        continue
                    
                    self.danhsach[hoten] = cb
            print(f"[Thành công] Đã đọc dữ liệu từ {filename}.")
            self.save_to_json() # Tự động lưu JSON
        except FileNotFoundError:
            print(f"[Lỗi] Không tìm thấy file {filename}.")
        except ValueError:
            print("[Lỗi] Sai định dạng dữ liệu trong file CSV (Ví dụ: Tuổi/Bậc không phải là số).")
        except Exception as e:
            print(f"[Lỗi hệ thống]: {e}")

    # Yêu cầu 2: Thêm, xóa, tìm kiếm
    def them_can_bo(self, cb):
        self.danhsach[cb.get_hoten()] = cb
        print(f"[Thành công] Đã thêm cán bộ: {cb.get_hoten()}")
        self.save_to_json()

    def xoa_can_bo(self, hoten):
        if hoten in self.danhsach:
            del self.danhsach[hoten]
            print(f"[Thành công] Đã xóa cán bộ: {hoten}")
            self.save_to_json()
        else:
            print("[Thông báo] Không tìm thấy cán bộ để xóa.")

    def tim_theo_ten(self, hoten):
        # Tìm kiếm tương đối (chứa chuỗi)
        ket_qua = [cb for ten, cb in self.danhsach.items() if hoten.lower() in ten.lower()]
        if ket_qua:
            print(f"\n--- KẾT QUẢ TÌM KIẾM TÊN '{hoten}' ---")
            for cb in ket_qua:
                cb.inTTin()
                print("-" * 25)
        else:
            print("[Thông báo] Không tìm thấy cán bộ khớp tên.")

    def tim_theo_loai(self, loai_can_tim):
        ket_qua = [cb for cb in self.danhsach.values() if type(cb).__name__ == loai_can_tim]
        if ket_qua:
            print(f"\n--- DANH SÁCH {loai_can_tim.upper()} ---")
            for cb in ket_qua:
                cb.inTTin()
                print("-" * 25)
        else:
            print(f"[Thông báo] Không có cán bộ nào thuộc loại {loai_can_tim}.")

    def in_top_3_bac_cao_nhat(self):
        # Lọc ra các công nhân
        cong_nhan_list = [cb for cb in self.danhsach.values() if isinstance(cb, CongNhan)]
        # Sắp xếp giảm dần theo bậc
        cong_nhan_list.sort(key=lambda x: x.get_bac(), reverse=True)
        
        print("\n--- TOP 3 CÔNG NHÂN CÓ BẬC CAO NHẤT ---")
        for cb in cong_nhan_list[:3]:
            cb.inTTin()
            print("-" * 25)

    def hien_thi_danh_sach(self):
        if not self.danhsach:
            print("[Thông báo] Danh sách hiện đang trống.")
            return
        print("\n--- DANH SÁCH TOÀN BỘ CÁN BỘ ---")
        for cb in self.danhsach.values():
            cb.inTTin()
            print("-" * 25)

    # Yêu cầu 3: Load và Save JSON
    def save_to_json(self):
        try:
            data_to_save = [cb.to_dict() for cb in self.danhsach.values()]
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"[Lỗi lưu JSON]: {e}")

    def load_from_json(self):
        if not os.path.exists(self.json_file):
            return
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.danhsach.clear()
                for item in data:
                    loai = item.get("loai")
                    if loai == "CongNhan":
                        cb = CongNhan(item['hoten'], item['tuoi'], item['gioitinh'], item['diachi'], item['bac'])
                    elif loai == "KySu":
                        cb = KySu(item['hoten'], item['tuoi'], item['gioitinh'], item['diachi'], item['nganhdaotao'])
                    elif loai == "NhanVien":
                        cb = NhanVien(item['hoten'], item['tuoi'], item['gioitinh'], item['diachi'], item['congviec'])
                    else:
                        continue
                    self.danhsach[cb.get_hoten()] = cb
        except Exception as e:
            print(f"[Lỗi đọc JSON]: {e}")

# ================= CLI MENU =================
def main():
    ql = QuanLyCanBo()
    
    while True:
        print("\n" + "="*40)
        print(" HỆ THỐNG QUẢN LÝ CÁN BỘ (JSON/CSV AUTO)")
        print("="*40)
        print("1. Đọc dữ liệu từ file CSV")
        print("2. Thêm cán bộ thủ công")
        print("3. Xóa cán bộ theo tên")
        print("4. Tìm kiếm theo họ tên")
        print("5. Tìm kiếm theo loại (CongNhan/KySu/NhanVien)")
        print("6. Hiển thị top 3 cán bộ bậc cao nhất")
        print("7. Hiển thị toàn bộ danh sách")
        print("0. Thoát chương trình")
        
        try:
            choice = input("Nhập lựa chọn của bạn: ").strip()
            
            if choice == '1':
                file_name = input("Nhập tên file CSV (Mặc định 'canbo.csv'): ").strip()
                if not file_name: file_name = 'canbo.csv'
                ql.doc_csv(file_name)
                
            elif choice == '2':
                loai = input("Chọn loại (1. Công nhân | 2. Kỹ sư | 3. Nhân viên): ").strip()
                if loai not in ['1', '2', '3']:
                    print("[Lỗi] Lựa chọn không hợp lệ!")
                    continue
                    
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
                    
                ql.them_can_bo(cb)
                
            elif choice == '3':
                ten = input("Nhập chính xác họ tên cần xóa: ")
                ql.xoa_can_bo(ten)
                
            elif choice == '4':
                ten = input("Nhập tên cần tìm: ")
                ql.tim_theo_ten(ten)
                
            elif choice == '5':
                loai = input("Nhập loại cần tìm (CongNhan/KySu/NhanVien): ").strip()
                ql.tim_theo_loai(loai)
                
            elif choice == '6':
                ql.in_top_3_bac_cao_nhat()
                
            elif choice == '7':
                ql.hien_thi_danh_sach()
                
            elif choice == '0':
                print("Đã thoát chương trình. Dữ liệu đã được tự động lưu vào JSON.")
                break
            else:
                print("[Lỗi] Vui lòng chọn từ 0 đến 7.")
                
        # Bắt toàn bộ lỗi phát sinh trong quá trình nhập liệu (ví dụ: nhập chữ vào phần yêu cầu nhập số)
        except ValueError:
            print("[Lỗi] Bạn đã nhập sai định dạng dữ liệu. Vui lòng nhập số ở các trường Tuổi/Bậc.")
        except Exception as e:
            print(f"[Lỗi không xác định]: {e}. Chương trình vẫn tiếp tục chạy.")

if __name__ == "__main__":
    main()