class temp:
    def print(*args):
        for i in range(1,len(args)):
            print(args[i],end=" ")
        print()
a=temp()
a.print(10)
a.print(1,2,3,4,5)
