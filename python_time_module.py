import time
print "time() "
print time.time()
print "\n"

print "asctime(time) "
t = time.localtime()
print time.asctime(t)
print "\n"

print "sleep(time)"
localtime = time.asctime( time.localtime(time.time()) )
print localtime
time.sleep( 10 )
localtime = time.asctime( time.localtime(time.time()) )
print localtime
print "\n"

print "strptime(String str,format f)"
timerequired = time.strptime("26 Jun 14", "%d %b %y")
print timerequired
print "\n"

print "gtime()"
import time
print time.gmtime()
print "\n"

print "mktime()"
t = (2014, 2, 17, 17, 3, 38, 1, 48, 0)
second = time.mktime( t )
print second
print "\n"

print "strftime()"
import time
t = (2014, 6, 26, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
print "\n"