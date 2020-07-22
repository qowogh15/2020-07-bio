class c:
    def __init__(self):
        print("클래스 c인스턴스생성")
        self.name = "ccc"
        self.age = 0

    def say_hi(self):
        print("hi")

    def add_age(self,n:int):
        self.age +=n

    def __str__(self):
        return "__str__"
    def __repr__(self):
        return "__repr__"
    
    def __abs__(self):
        print("__abs__")
    def __len__(self):
        print("__len__")

    def __add__(self,other):
        return self.age + other.age


