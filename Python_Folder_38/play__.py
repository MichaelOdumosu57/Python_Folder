

# how to do things in python the fn are more like rxjs which enable data types to be more 
# zip takes 2 list turns them to a dict sum iterates through it and says what should be done w/ it 

xvec = [10, 20, 30]
yvec = [7, 5, 3]
a = sum(x*y for x,y in zip(xvec, yvec))   
print(a)