class Demo:
    def __new__(cls, *args):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("__self__ called")


object = Demo()
