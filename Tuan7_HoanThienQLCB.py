import json
import csv
class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def get_ho_ten(self):
        return self.ho_ten  

    def __str__(self):
        return f"Họ tên: {self.ho_ten} | Tuổi: {self.tuoi} | Giới tính: {self.gioi_tinh} | Địa chỉ: {self.dia_chi}"

    def to_dict(self):
        return {
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi
        }

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    def __str__(self):
        return f"[Công nhân] {super().__str__()} | Bậc: {self.bac}"
    
    def to_dict(self):
        data = super().to_dict()
        data.update({"loai": "CongNhan", "bac": self.bac})
        return data
    
class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def __str__(self):
        return f"[Kỹ sư] {super().__str__()} | Ngành đào tạo: {self.nganh_dao_tao}"
    
    def to_dict(self):
        data = super().to_dict()
        data.update({"loai": "KySu", "nganh_dao_tao": self.nganh_dao_tao})
        return data
    
class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def __str__(self):
        return f"[Nhân viên] {super().__str__()} | Công việc: {self.cong_viec}"
    
    def to_dict(self):
        data = super().to_dict()
        data.update({"loai": "NhanVien", "cong_viec": self.cong_viec})
        return data
    
class QuanLiCanBo:
    def __init__(self):
        self.danh_sach = {}
        self.FILE = "canbo.json"
        self.load_from_json()

    def doc_csv(self, filename = 'canbo.csv'):
        try:
            with open(filename, "r", encoding = "utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if not row or len(row) < 6: continue
                    ho_ten, tuoi, gioi_tinh, dia_chi, loai, extra = row

                    tuoi = int(tuoi)

                    if loai == "CongNhan":
                        cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, int(extra))
                    elif loai == "KySu":
                        cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, extra)
                    elif loai == "NhanVien":
                        cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, extra)
                    else:
                        continue

                    self.danh_sach[ho_ten] = cb
                print(f"Đã đọc từ CSV: {filename}.")
                self.save_to_json()
        except FileNotFoundError:
            print(f"[Lỗi] không tìm thấy file {filename}.")
        except ValueError:
            print(f"[Lỗi] sai định dạng dữ liệu trong file CSV {filename}.")
        except Exception:
            print(f"[Lỗi hệ thống] {filename}.")

    def them_can_bo(self, cb):
        self.danh_sach[cb.get_ho_ten()] = cb
        print(f"Đã thêm cán bộ: {cb.get_ho_ten()}.")
        self.save_to_json()

    def xoa_can_bo(self, ho_ten):
        if ho_ten in self.danh_sach:
            del self.danh_sach[ho_ten]
            print(f"Đã xóa cán bộ: {ho_ten}")
            self.save_to_json()
        else:
            print(f"Không tìm thấy cán bộ: {ho_ten} để xoá.")
    
    def tim_kiem_theo_ten(self, ho_ten):
        ket_qua = [cb for ten, cb in self.danh_sach.items() if ho_ten.lower() in ten.lower()]
        if ket_qua:
            print (f"\n--- KẾT QUẢ TÌM KIẾM CHO '{ho_ten}' ---")
            for cb in ket_qua:
                print(cb)
        else:
            print(f"Không tìm thấy cán bộ nào khớp tên: {ho_ten}.")

    def tim_theo_loai(self, loai_can_tim):
        ket_qua = [cb for cb in self.danh_sach.values() if type(cb).__name__ == loai_can_tim]
        if ket_qua:
            print(f"\n--- DANH SÁCH CÁN BỘ LOẠI '{loai_can_tim.upper()}' ---")
            for cb in ket_qua:
                print(cb)
        else:
            print(f"Không tìm thấy cán bộ nào thuộc loại: {loai_can_tim}.")
    def hien_top_3_cao_nhat(self):
        cong_nhan_list = [cb for cb in self.danh_sach.values() if isinstance(cb, CongNhan)]

        cong_nhan_list.sort(key=lambda x: x.bac, reverse=True)

        print("\n--- TOP 3 CÔNG NHÂN CAO BẬC NHẤT ---")
        for cb in cong_nhan_list[:3]:
            print(cb)

    def hien_thi_danh_sach(self):
        if not self.danh_sach:
            print("\nDanh sách hiện đang trống.")
            return
        else:
            print("\n--- DANH SÁCH CÁN BỘ (Sắp xếp theo Tên ABC) ---")
            for cb in self.danh_sach.values():
                print(cb)

    def save_to_json(self):
        try:
            data_to_save = [cb.to_dict() for cb in self.danh_sach.values()]
            with open(self.FILE, "w", encoding="utf-8")as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"[Lỗi lưu file JSON] {e}")

    def load_from_json(self):
        try:
            with open(self.FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.danh_sach.clear()
                for item in data:
                    loai = item.get("loai")
                    if loai == "CongNhan":
                        cb = CongNhan(item["ho_ten"], item["tuoi"], item["gioi_tinh"], item["dia_chi"], item["bac"])
                    elif loai == "KySu":
                        cb = KySu(item["ho_ten"], item["tuoi"], item["gioi_tinh"], item["dia_chi"], item["nganh_dao_tao"])
                    elif loai == "NhanVien":
                        cb = NhanVien(item["ho_ten"], item["tuoi"], item["gioi_tinh"], item["dia_chi"], item["cong_viec"])
                    else:
                        continue
                    self.danh_sach[cb.get_ho_ten()] = cb
        except FileNotFoundError:
            print(f"[Lỗi] không tìm thấy file JSON: {self.FILE}. Bắt đầu với danh sách trống.")
        except Exception as e:
            print(f"[Lỗi đọc file JSON] {e}")

def main():
    qlcb = QuanLiCanBo()

    while True:
        print("\n" + "="*40)
        print(" HỆ THỐNG QUẢN LÝ CÁN BỘ")
        print("="*40)
        print("1. Đọc danh sách từ file CSV")
        print("2. Thêm mới cán bộ")
        print("3. Xoá cán bộ theo tên")
        print("4. Tìm kiếm theo họ tên cán bộ")
        print("5. Tìm kiếm theo loại cán bộ")
        print("6. Hiển thị top 3 cán bộ có bậc cao nhất")
        print("7. Hiển thị toàn bộ danh sach cán bộ")
        print("0. Thoát")
        print("="*40)

        try:
            choice = input("Lựa chọn của bạn:")

            if choice == '1':
                file_name = input("Nhập tên file CSV (mặc định 'canbo.csv'): ").strip()
                if not file_name: file_name = 'canbo.csv'
                qlcb.doc_csv(file_name)
            elif choice == '2':
                loai = input("Nhập loại cán bộ (1. CongNhan| 2. KySu| 3. NhanVien): ").strip()
                if loai not in ['1', '2', '3']:
                    print("Lựa chọn không hợp lệ!")
                    continue
                ho_ten = input("Nhập họ tên: ")
                tuoi = int(input("Nhập tuổi: "))
                gioi_tinh = input("Nhập giới tính: ")
                dia_chi = input("Nhập địa chỉ: ")

                if loai == '1':
                    bac = int(input("Nhập bậc (1-10): "))
                    cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
                if loai == '2':
                    nganh_dao_tao = input("Nhập ngành đào tạo: ")
                    cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao)
                if loai == '3':
                    cong_viec = input("Nhập công việc: ")
                    cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec)
                
                qlcb.them_can_bo(cb)
            
            elif choice == '3':
                ho_ten = input("Nhập họ tên cán bộ cần xoá: ")
                qlcb.xoa_can_bo(ho_ten)

            elif choice == '4':
                ho_ten = input("Nhập họ tên cán bộ cần tìm: ")
                qlcb.tim_kiem_theo_ten(ho_ten)

            elif choice == '5':
                loai = input("Nhập loại cán bộ cần tìm (CongNhan/KySu/NhanVien): ")
                qlcb.tim_theo_loai(loai)
            
            elif choice == '6':
                qlcb.hien_top_3_cao_nhat()
            
            elif choice == '7':
                qlcb.hien_thi_danh_sach()

            elif choice == '0':
                print("Thoát chương trình. Dữ liệu đã được tự động lưu!")
                break

            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng dữ liệu.")

        except Exception as e:
            print(f"Lỗi hệ thống: {e}")

if __name__ == "__main__":
    main()






