import os

print "rename():"
os.rename('mno.txt','pqr.txt')
print "\n"

print "remove():"
os.remove('mno.txt')
print "\n"

print "mkdir()"
os.mkdir("new")
print "\n"

print "chdir()"
os.chdir("new")
print "\n"

print "getcwd()"
print os.getcwd()
print "\n"

print "rmdir()"
os.rmdir("new")
print "\n"