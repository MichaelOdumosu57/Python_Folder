print "keys():"
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
print data1.keys()
print "\n"

print "values():"
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
print data1.values()
print "\n"

print "items():"
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
print data1.items()
print "\n"

print "update(dictionary2):"
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
data2={103:'Sanjay'}
data1.update(data2)
print data1
print data2
print "\n"

print "clear():"
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
print data1
data1.clear()
print data1
print "\n"

print "fromkeys(sequence)/ fromkeys(seq,value):"
sequence=('Id' , 'Number' , 'Email')
data={}
data1={}
data=data.fromkeys(sequence)
print data
data1=data1.fromkeys(sequence,100)
print data1
print "\n"

print "copy():"
data={'Id':100 , 'Name':'Aakash' , 'Age':23}
data1=data.copy()
print data1
print "\n"

print "has_key(key):"
data={'Id':100 , 'Name':'Aakash' , 'Age':23}
print data.has_key('Age')
print data.has_key('Email')
print "\n"

print " get(key):"
data={'Id':100 , 'Name':'Aakash' , 'Age':23}
print data.get('Age')
print data.get('Email')
