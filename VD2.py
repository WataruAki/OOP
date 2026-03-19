class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac ):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def hien_thi(self):
        print(f"SieuNhan: {self.ten}, Vu Khi: {self.vu_khi}, Mau Sac: {self.mau_sac}")

A = SieuNhan("Soldier Boy", "Shield", "Camo")
B = SieuNhan("Homelander", "Laser Eyes", "Red and Blue")

def main():
    print("Thong tin SieuNhan A:")
    A.hien_thi()
    print("-" * 25)

    print("Thong tin SieuNhan B:")
    B.hien_thi()
    print("-" * 25)

main()