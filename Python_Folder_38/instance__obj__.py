class x:
    def __init__(self):
        self.counter = 0


x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter