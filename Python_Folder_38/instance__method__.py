class x:
    def __init__(self):
        self.counter = 0

    def f(self):
        print('how will I access self')


xf = x.f
while True:
    print(xf())

