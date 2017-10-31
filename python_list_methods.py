print "index(object):"
data = [786,'abc','a',123.5]
print "Index of 123.5:", data.index(123.5)
print "Index of a is", data.index('a')
print "\n"

print " count(object):"
data = [786,'abc','a',123.5,786,'rahul','b',786]
print "Number of times 123.5 occured is", data.count(123.5)
print "Number of times 786 occured is", data.count(786)
print "\n"

print " pop()/pop(int):"
data = [786,'abc','a',123.5,786]
print "Last element is", data.pop()
print "2nd position element:", data.pop(1)
print data
print "\n"

print "insert(index,object):"
data=['abc',123,10.5,'a']
data.insert(2,'hello')
print data
print "\n"

print "extend(sequence):"
data1=['abc',123,10.5,'a']
data2=['ram',541]
data1.extend(data2)
print data1
print data2
print "\n"

print "remove(object):"
data1=['abc',123,10.5,'a','xyz']
data2=['ram',541]
print data1
data1.remove('xyz')
print data1
print data2
data2.remove('ram')
print data2
print "\n"

print "reverse():"
list1=[10,20,30,40,50]
list1.reverse()
print list1
print "\n"

print "sort():"
list1=[10,50,13,'rahul','aakash']
list1.sort()
print list1