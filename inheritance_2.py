class A:
    def method(self):
        print("1")

class B(A):
    def method_2(self):
        print("2")
        # return super().method()

class C(B):
    def method_3(self):
        print("3")
        # return super().method_2()

c = C()
c.method_3()
c.method_2()
c.method()