print "Adding Lists"
list1=[10,20]
list2=[30,40]
list3=list1+list2
print list3
list1=[10,20]
# list1+30
print list1
print "\n"

print "Replicating lists"
list1=[10,20]
print list1*1
print "\n"

print "List slicing:"
list1=[1,2,4,5,7]
print list1[0:2]
print list1[4]
list1[1]=9
print list1
print "\n"

print "Updating elements in a List:"
data1=[5,10,15,20,25]
print "Values of list are: "
print data1
data1[2]="Multiple of 5"
print "Values of list are: "
print data1
print "\n"

print "Appending elements to a List:"
list1=[10,"rahul",'z']
print "Elements of List are: "
print list1
list1.append(10.45)
print "List after appending: "
print list1
print "\n"

print "Deleting Elements from a List:"
list1=[10,'rahul',50.8,'a',20,30]
print list1
del list1[0]
print list1
del list1[0:3]
print list1
print "\n"
