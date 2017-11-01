import os
# os.mkdir("Info")
obj1 = open("Info/msg1.py","w")
obj2 = open("Info/msg2.py","w")
obj3= open("Info/msg3.py","w")
obj1.write("""def msg1(): print "This is msg1""" )
obj2.write("""def msg2(): print "This is msg2""" )
obj3.write("""def msg3(): print "This is msg3""" )
   
    
import Info
Info.msg1()
Info.msg2()
Info.msg3()