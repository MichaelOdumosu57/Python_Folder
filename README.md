# python HOW TO

# ASK NO QUESTION, FOR EACH STEP DO IT THE WAY YOU SEE IT !!
# DONT ASK WHY, IF YOU DO IT THE WAY YOU SEE IT YOU WILL ANSWER YOUR OWN QUESION
# THE ONLY WAY TO LEARN IS BY DOING :)
# LINK https://github.com/MichaelOdumosu57/Python_Folder/blob/master/README.md




## to write a function
> remeber the return statement
```python
def my_function(a,b,c,d,e,f):
    print(a + f)
    print(b+c)
    print(d+e)
    return 'what you need to finsih'
# function ends here
```

### to call  a function
if the function have 6 parameters you give it 6 arguments
if the function have 7 parameters you give it 7 arguments
if the function have 12 parameters you give it 12 arguments
```python
my_list = [1,2,3,4,5,6]
function_answer = my_function( *my_list)
print(function_answer)
```



## to make a variable
>  no quotes ,no #, no spaces
> write with only lowercase letters and underscore
> if you see something like this @^$^@ only use it dont write like it
```python
variable = 1 
abc 
my_friend

_sadgsakdgnmsadgk__  
$@%%@%^ = 12
```





## strings 
string - they are for humans to read
these are regular strings
always wrapped in " "
> THEY ARE NOT WORDS, WE CALL THEM 'STUFF'
a string is full of stuff
one "stuff " one string 
two "stuff "   "stuff " two strings
several "stuff "  several strings   
```python

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


## \n is the newline char in python
> that \n would put what ever is after the string on a new line
> FOR REGULAR STRINGS ONLY
```python
# what python
"Step on my feet\n watch your twos"

"Step on my feet"
"watch your twos"
```



### byte strings
they are used for encryption 
encoding, decoding, hashing, ssh lock key lock key
public key private key, key to your house (lmao) all that good stuff
> THEY ARE STRING WITH b AT THE FRONT- THATS HOW YOU WRITE THEM NO QUESTIONS WRITE IT LIKE THAT
> THEY ARE NOT BYTES THEY ARE BYTE STRINGS
> all they are used for is to convert one item to another

> 
```python
my_byte_string = b'this is my password'

your_byte_string = b'this is your password'


import binascii

binascii.b2a_base64(your_byte_string)
b'dGhpcyBpcyB5b3VyIHBhc3N3b3Jk\n'


binascii.a2b_base64(b'dGhpcyBpcyB5b3VyIHBhc3N3b3Jk\n')
b'this is your password'


binascii.b2a_hex(your_byte_string)
b'7468697320697320796f75722070617373776f7264'

binascii.a2b_hex(b'7468697320697320796f75722070617373776f7264')
b'this is your password'
```

### to convert 
```python
your_byte_string = b'this is your password'
str(your_byte_string)
'this is your password'

your_string = 'this is your password'
your_string.encode()
b'this is your password'
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

python38 store.py mimi pizza bathtub sink 

```

### to see user arguments in python
```python
import sys
print(sys.argv)
```

## create a list
```python
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
```python
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
```python
my_list = ['loop','thorough','this','list']
for index in  my_list:
    print(index)
```

### this is how python counts
```python
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
```python
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
```python
car_dictnary = {
    'key':1          ,
    'door':4             ,
    'make':'toyota'         ,
    'model':'SUV'             ,
    'YEAR':['03','04','05']    
}
```


## to  get key from a value 
```python
print(car_dictnary['key']   )
print(car_dictnary['door'])
print(car_dictnary['make'])
print(car_dictnary['model'])
print(car_dictnary['year'])
```



## to loop through dictonary

```python
for keys,val in car_dictnary.items():
    print(keys,val)
#end of loop
```

### to create a client socket
```python
import socket 
HOST = 'listen.runcode.ninja' #name of server here
PORT = 80 #is a port
ADDR = (HOST,PORT)
client_msg  = "My message for the server"  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #connect to  a socket
    s.connect(ADDR)    
    ################################

    client_msg = client_msg + "\n"
    client_msg = client_msg.encode()
    s.send(client_msg)
    server_msg = s.recv(1024)
    server_msg =server_msg.decode()
    print(server_msg)
    # print(msg)
```

## request and response
```python
import requests 

url = 'http://blackjack.runcode.ninja'

modify the url to get different pages or different data from the server 
url = 'http://blackjack.runcode.ninja/bj.php'
url = 'http://blackjack.runcode.ninja/aboutPage'
url = 'http://blackjack.runcode.ninja/adminPage'


website = requests.get(url)
print(website)
"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>VideoOfWorks</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
</head>
<body>
  <app-root></app-root>
</body>
</html>
"""

data_for_website = {
    'choice':'spades',
    'draws':[1,2,3,4],
    'Name':'Harper',
    'Age':27,
    'email':'harperjones@yahoo.com'
}
info = requests.post(url, data=data_for_website)
"""
 {
    'update':true,
    'winner':'false',
    'message': "try-again: says Server",
    'password':" jkewqkqwqrkqwr3241=="
}
"""
```




### requests and response Session
> when you want to steal someones session when they login to their bank acct
```python
import requests 

url = "http://tdbank.com"
sess = requests.Session()
stolen_rich_person_session = sess.get(url)
money = '$0 USD'


while money != '$10000000 USD':
    transfer = {
        'add':'yes',
        'from':'rich man acct #',
        'to':'your account #',
        'type':'external',
        'amnt':'$600',
        'duration':'30 days',
        'frequency':'6 hrs'
    }
    transfer_money = sess.post(url,data = transfer)
"""
money transfer to [YOUR NAME HERE] acct
SUCCESS!!
"""  

sess.close()
```    
    
