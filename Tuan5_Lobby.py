class Lobby:
    def __init__(self, area):
        self.area = area
        print(f"Lobby ({self.area}m^2) được tạo.")

    def __del__(self):
        print(f"Lobby ({self.area}m^2) bị hủy.")

class Bathroom:
    def __init__(self, floor):
        self.floor = floor
        print(f"Bathroom (tầng {self.floor}) được tạo.")

    def __del__(self):
        print(f"Bathroom (tầng {self.floor}) bị hủy.")

class VisitorCenter:
    def __init__(self, name):
        self.name = name
        print(f"Xây dựng {name}...")

        self.lobby = Lobby(300)
        self.bathroom = [Bathroom(i) for i in range(1, 4)]

    def __del__(self):
        print(f"Huỷ {self.name} -> mọi thành phần bị huỷ theo.")


vc = VisitorCenter("Bảo tàng lịch sử Quân Đội Nhân Dân Việt Nam")
del vc