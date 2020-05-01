# python





```

what python
"Step on my feet\n watch your twos"

"Step on my feet"
"watch your twos"
```


## to write a function

```
def my_function(a,b,c,d,e,f):
    print(a + f)
    print(b+c)
    print(d+e)
# function ends here
```

## to call  a function
if the function have 6 parameters you give it 6 arguments
if the function have 7 parameters you give it 7 arguments
if the function have 12 parameters you give it 12 arguments
```
my_list = [1,2,3,4,5,6]
my_function( 1,2,3,4,5,6 )
```

## to make a variable
>  no quotes ,no #, no spaces
> write with only lowercase letters and underscore
> if you see something like this @^$^@ only use it dont write like it
```
variable = 1 
abc 
my_friend

_sadgsakdgnmsadgk__  
$@%%@%^ = 12
```





## strings 
string - they are for humans to read
always wrapped in " "
> THEY ARE NOT WORDS, WE CALL THEM 'STUFF'
a string is full of stuff
one "stuff " one string 
two "stuff "   "stuff " two strings
several "stuff "  several strings   
```

"mystring" 
"cn2r8qo89c 82qhx832rq8yh8uq2   2r33    2r2 w" # string


"adgoawdg" "sadgsdgFfdsFS"
"" "" "" "" " "

head = "1"
tail = "2"

answer = "my boss name is vaquero, my boss is getting a raise"
"$@#%&#^&%$*%(&*^$&@^*&#^%&$$# dasonskmnfkag"
"#@%7%&##$@^dasgASDGasg"
"lol, wyd, txt me ltr, "
```



## to run  a python file 
```
python3 name_of_your_file.py
```

### to add user arguments
> in terminal
> to add more arguments seperate by space 
```
python38 learn.py user_has_to_say



python38 store.py soap shampoo toliet_paper tissue

```

### to see user arguments in python
```
import sys
print(sys.argv)
```

## create a list
```
my_list = ['strings',2,['another','list'],('my','tuple'),3{and:'more',for:'more'}]

a_list =[1,2,3,4,5]

a_list =['string','strings','stuff']
```


### list index
> with a bracket and a num at the end like this
my_list[1]
> num has to be less them anout of items in list
```
a_list =['string','strings','stuff']

a_list[2]  # right
a_list[16] # wrong
```

#### index by slice
> this gives a part of the list
> give another list
> 
```
s_l = ["stuff",1,"a",34,["anohther"],21]

print(s_l[0:1])
print(s_l[0:2])
print(s_l[0:3])
print(s_l[0:4])
print(s_l[0:5])
print(s_l[0:6])

print(s_l[2:3])
print(s_l[2:4])
print(s_l[2:5])
# so you can start and end anywhere in the list

print(s_l[5:len(s_l)])
print(s_l[4:len(s_l)])
print(s_l[4:len(s_l)])
print(s_l[3:len(s_l)])
print(s_l[2:len(s_l)])
print(s_l[1:len(s_l)])
```

## to loop in python
```
my_list = ['loop','thorough','this','list']
for index in  my_list:
    print(index)
```

### this is how python counts
```
my_list = ['loop','thorough','this','list']
counter = 0 
for toys in my_list:
    # print(toys)
    counter += 1
#end of for loop
print (counter)
```

### while loop
when a loop has a reason to stop counting
you need your counter variable
the reason to stop here is "hello strin
```
counter = 0 

my_list = [22,22,22,22,22,22,22,"stopping at next word","hello",22,22,22]
while my_list[counter] != "hello":
    print(my_list[counter])
    counter = counter + 1
#end of while loop
```

## to make a dictionary
key - the left side only string,number,
value, - the right side anything go there
index -  dictonary[key], gives you the value

every key value entry seprate with comma 
every entry looks like this 
> 'key':'value'
```
car_dictnary = {
    'key':1          ,
    'door':4             ,
    'make':'toyota'         ,
    'model':'SUV'             ,
    'YEAR':['03','04','05']    
}
```


## to  get key from a value 
```
print(car_dictnary['key']   )
print(car_dictnary['door'])
print(car_dictnary['make'])
print(car_dictnary['model'])
print(car_dictnary['year'])
```
## to loop through dictonary

```
for keys,val in car_dictnary.items():
    print(keys,val)
#end of loop
```



    
    
    
