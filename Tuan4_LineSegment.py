import copy
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def printpoint(self):
        print(f'({self.x}, {self.y})')
class LineSegment:
    def __init__(self, * args):
        if len(args)==0:
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0)
        if len(args)==2:
            if isinstance(args[0], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]
        if len(args)==4:
            if isinstance(args[0], int):
                self.__d1 = Point(args[0], args[1])
                self.__d2 = Point(args[2], args[3])
        if len(args)==1:
            if isinstance(args[0], LineSegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)
    
    def __str__(self):
        return "[(%d, %d), (%d, %d)]" % (self.__d1.x,self.__d1.y,self.__d2.x, self.__d2.y)
    
    def get_d1(self):
        return self.__d1
    def get_d2(self):
        return self.__d2
    
l1=LineSegment()
print("Đoạn thẳng l1 có điểm đầu và cuối là:")
l1.get_d1().printpoint()
l1.get_d2().printpoint()

p1, p2 = Point(1,2), Point(3, 4)
l2=LineSegment(p1, p2)
print("Đoạn thẳng l2 có hai đầu mút là:")
l2.get_d1().printpoint()
l2.get_d2().printpoint()

l3=LineSegment(1, 7, 1, 1)
print("Đoạn thẳng l3 có hai đầu mút là:")
l3.get_d1().printpoint()
l3.get_d2().printpoint()

l4=LineSegment(l3)
print("Đoạn thẳng l4 có hai đầu mút là:")
l4.get_d1().printpoint()
l4.get_d2().printpoint()

    
