import main

obj1 = open("Info/msg1.py","w")
obj2 = open("Info/msg2.py","w")
obj3 = open("Info/msg3.py","w")
obj1.write("def message1():\n   print 'This is message1'")
obj2.write("def message2():\n   print 'This is message2'" )
obj3.write("def message3():\n   print 'This is message3'" )

main.package_call()