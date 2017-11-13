import os
import sys
# sys.path.insert(0, './Info')
# os.mkdir("Info")
# obj1 = open("Info/msg1.py","w")
# obj2 = open("Info/msg2.py","w")
# obj3 = open("Info/msg3.py","w")
# obj1.write("def message1():\n   print 'This is message1'")
# obj2.write("def message2():\n   print 'This is message2'" )
# obj3.write("def message3():\n   print 'This is message3'" )
   

import Info

def package_call():
    Info.msg1.message1()
    Info.msg2.message2()
    Info.msg3.message3()