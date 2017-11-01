print "adding tuple"
data1=(1,2,3,4)
data2=('x','y','z')
data3=data1+data2
print data1
print data2
print data3
print "\n"

print "replicating tuple"
tuple1=(10,20,30);
tuple2=(40,50,60);
print tuple1*2
print tuple2*3
print "\n"

print "tuple slicing"
data1=(1,2,4,5,7)
print data1[0:2]
print data1[4]
print data1[:-1]
print data1[-5:]
print data1
print "\n"

print "make new tuple"
data1=(10,20,30)
data2=(40,50,60)
data3=data1+data2
print data3
print "\n"

print "delete whole tuple"
data=(10,20,'rahul',40.6,'z')
print data
del data      #will delete the tuple data
print data  #will show an error since tuple data is already deleted
print "\n"