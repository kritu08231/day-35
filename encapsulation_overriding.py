class A:
    def print(self):
        print("a")
class B(A):
    def print(self):
        print("b")
class C(B):
    def print(self):
        print("c")

b=C()
b.print()
