class First(object):
  def __init__(self):
    super(First, self).__init__()
    print("first")
  
class Second(object):
  def __init__(self):
    super(Second, self).__init__()
    print("second")
  
class Third(  Second, First): # the order the Parent parameters matters, if you wanted first printed first, it must go last
  def __init__(self):
    super(Third, self).__init__()
    print("third")
  


