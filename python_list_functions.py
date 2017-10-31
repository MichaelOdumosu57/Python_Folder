print "min(list):"
list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
print "Minimum value in List1: ",min(list1)
print "Minimum value in List2: ",min(list2)
print "\n"

print "max(list):"
list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
print "Maximum value in List : ",max(list1)
print "Maximum value in List : ",max(list2)
print "\n"

print " len(list):"
list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
print "No. of elements in List1: ",len(list1)
print "No. of elements in List2: ",len(list2)
print "\n"

print " cmp(list1,list2):"
list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
list3=[101,981,'abcd','xyz','m']
print cmp(list1,list2)
print cmp(list2,list1)
print cmp(list3,list1)
print "\n"

print "list(sequence):"
seq=("abcd",145, 'a')
data=list(seq)
print "List formed is : ",data
print "\n"