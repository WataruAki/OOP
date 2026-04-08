from abc import ABC, abstractmethod
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Giá {gia} không hợp lệ")

class HangHoa:
    def __init__(self, ma, ten, nsx, gia):
        self.__ma, self.__ten, self.__nsx = ma, ten, nsx
        self.gia = gia
    @property
    def ma_hang(self):return self.__ma
    @property
    def ten_hang(self):return self.__ten
    @property
    def gia(self):return self.__gia
    @gia.setter
    def gia(self, v):
        if v < 0:
            raise GiaKhongHopLe(v)
        self.__gia = v
    
    @abstractmethod
    def loai_hang(self): pass
    def inTTin(self):
        return (f"[{self.loai_hang()}] {self.__ma}"
                f" | {self.__ten} | {self.__gia:,.0f}đ")
    def __str__(self):return self.inTTin()
    def __eq__(self, o): return self.__ma == o.__ma
    def __lt__(self, o): return self.__gia < o.__gia
    def __hash__(self): return hash(self.__ma)

class HangDienMay(HangHoa):
        def __init__(self, ma, ten, nsx, gia, bh, dap, cs):
            super().__init__(ma, ten, nsx, gia)
            self.bh, self.dap, self.cs = bh, dap, cs
        def loai_hang(self): return "Điện máy"
        def inTTin(self):
            return (f"{super().inTTin()}"
                    f" | BH: {self.bh}th"
                    f" | Đáp: {self.dap}V | CS: {self.cs}W")
        
    #Demo

ds = [HangDienMay("DM001", "Tủ lạnh", "Samsung", 15000000, 24, 220, 500),
          
    ]
for sp in sorted(ds):
        print(sp)

with open("kho.txt", "w")as f:
        for sp in sorted(ds):
            f.write(repr(sp) + "\n")

