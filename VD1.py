import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def nhap(self):
        self.x = float(input("Nhap x: "))
        self.y = float(input("Nhap y: "))

    def hien(self):
        print(f"Point({self.x}, {self.y})")

    def doi_xung_qua_O(self):
        return Point(-self.x, -self.y)
    
    def khoang_cach_den_O(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def khoang_cach(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
A = Point(3, 4)

B = Point(0, 0)
print("Nhập toạ độ điểm B:")
B.nhap()
print("Toạ độ điểm B: " , end="")
B.hien()
print("-"*25)

C = B.doi_xung_qua_O()
print("Tọa độ điểm C (đối xứng B qua O): ", end="")
C.hien()
print("-" * 25)

d_BO = B.khoang_cach_den_O()
print(f"Khoảng cách từ B đến O: {d_BO:.2f}")
print("-" * 25)

d_AB = A.khoang_cach(B)
print(f"Khoảng cách từ A đến B: {d_AB:.2f}")

if __name__ == "__main__":
    # 1. Tạo điểm A(3, 4) và hiển thị tọa độ
    A = Point(3, 4)
    print("Tọa độ điểm A: ", end="")
    A.hien_thi()
    print("-" * 25)

    # 2. Tạo điểm B từ bàn phím
    B = Point()
    print("Nhập tọa độ điểm B:")
    B.nhap()
    print("Tọa độ điểm B: ", end="")
    B.hien_thi()
    print("-" * 25)

    # 3. Tạo điểm C đối xứng với B qua gốc O
    C = B.doi_xung_qua_O()
    print("Tọa độ điểm C (đối xứng B qua O): ", end="")
    C.hien_thi()
    print("-" * 25)

    # 4. Tính khoảng cách từ B đến O
    d_BO = B.khoang_cach_den_O()
    print(f"Khoảng cách từ B đến O: {d_BO:.2f}")
    print("-" * 25)

    # 5. Tính khoảng cách từ A đến B
    d_AB = A.khoang_cach(B)
    print(f"Khoảng cách từ A đến B: {d_AB:.2f}")