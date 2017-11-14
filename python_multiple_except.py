try:
    a=10/"things";
except ArithmeticError, StandardError:
    print "Arithmetic Exception"
else:
    print "Successfully Done"