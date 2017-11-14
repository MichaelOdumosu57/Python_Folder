    learning python

    Python Applications
        can be used with web, mobile, video, embed

    Python programming
        interactive mode
            type python into CMD and you go into the REPL
        script mode
            make your py file and send it to the cmd using python [file_name].py
        
        or use interactive GUI to do both

    Python Variables
        you do not need to give variables a type in python
        
        -Python assignments
            single assign
                [identifier_name]= [value]
            
            multiple assign
                [identifier_name]= [identifier_name]= ... [value]

            Assigning multiple values to multiple variables:
                [identifier_name], [identifier_name]... = [value], [value] ...

            
            Tokens
                Tokens can be defined as a punctuator mark, reserved words and each individual word in a statement.
                Token is the smallest unit inside the given program.
                There are following tokens in Python:
                
                Keywords.
                Identifiers.
                Literals.
                Operators.

            Tuples:
                like list but closed in parenthese and cant be changed

                tuple = ([value],[value] ...);
                but you can do this
                
                tuple + tuple_other = ([all_value_1st],[all_value_2nd]);

            Dictionary:
                key value pair

                [identifier] = {"[key]":[value],"[key]":[value]}
                [identifier].dict ();

                [identifier].keys() returns keys in square bracket
                [identifier].values() returns values in square bracket

        Python Keywords

            True	    False	None	and	        as
            asset	    def	    class	continue	break
            else	    finally	elif	del	        except
            global	    for	    if	    from	    import
            raise	    try	    or  	return	    pass
            nonlocal	in	    not	    is	        lambda

        Python Identifiers

            An identifier is a long sequence of characters and numbers.
            No special character except underscore ( _ ) can be used as an identifier.
            Keyword should not be used as an identifier name.
            case sensitive
            First character of an identifier can be character, underscore ( _ ) but not digit
    
        Python Literals
            
            Literals can be defined as a data that is given in a variable or constant.

            -String literals:
                single line
                    [identifier] = '[string]'
        
                mutiple line
                    [identifier] = '[string] \
                    [complete_string]'

                    [identifier] =  """[string]
                    [string] """

            -Numeric literals
                Int(signed integers) -- no fraction
                Long(long integers) -- number must be followed by L
                    [number]L
                float(floating point) -- can have fraction
                Complex(complex) -- a +bj a real, b imaginary
            
            -Boolean literals:
                called none
                None is used to specify to that field that is not created. It is also used for end of lists in Python.

            -Literal Collections.
                lists, tuples and dictionary

                what makes python lists a list
                    List contain items of different data types. Lists are mutable i.e., modifiable.
                    The values stored in List are separated by commas(,) and enclosed within a square brackets([]). We can store different type of data in a List.
                    Value stored in a List can be retrieved using the slice operator([] and [:]).
                    The plus sign (+) is the list concatenation and asterisk(*) is the repetition operator.

                    if you put a decimal ITS unix python will output the nearest decimal to 10 places

                file python_list.py

        Python Operators
            -Arithmetic Operators

                Operators	Description
                //	Perform Floor division(gives integer value after division)
                +	To perform addition
                -	To perform subtraction
                *	To perform multiplication
                /	To perform division
                %	To return remainder after division(Modulus)
                **	Perform exponent(raise to power)

            -Relational Operators
                Operators	Description
                <	Less than
                >	Greater than
                <=	Less than or equal to
                >=	Greater than or equal to
                ==	Equal to
                !=	Not equal to
                <>	Not equal to(similar to !=)

            -Assignment Operators
                Operators	Description
                =	Assignment
                /=	Divide and Assign
                +=	Add and assign
                -=	Subtract and Assign
                *=	Multiply and assign
                %=	Modulus and assign
                **=	Exponent and assign
                //=	Floor division and assign

            -Logical Operators:
                Operators	Description
                and	Logical AND(When both conditions are true output will be true)
                or	Logical OR (If any one condition is true output will be true)
                not	Logical NOT(Compliment the condition i.e., reverse)

            -Membership Operators:
                Membership Operators:

                Operators	Description
                in	Returns true if a variable is in sequence of another variable, else false.
                not in	Returns true if a variable is not in sequence of another variable, else false.

                file : python_membership.py

            -Identity Operators:
                Operators	Description
                is	Returns true if identity of two operands are same, else false
                is not	Returns true if identity of two operands are not same, else false.
        
                file: python_identity.py

        Python Comments
                
                -single line
                    # This is single line comment.


                -multi line
                    ''''' This
                            Is
                            Multipline comment'''


        Python if statement
                
                if([condition]):
                    [statements]

        Python if else
        
    
            if(condition):  False
                statements
            else:   True
                statements

        Python nested if

            
            a=10
            if a>=20:
                print "Condition is True"
            else:
                if a>=15:
                    print "Checking second value"
                else:
                    print "All Conditions are false"


        "no else if in python like that i thnink"

        Python for loop

            for [variable] in [sequence]:


            -nested loops
            you can say
                for i in range(1,6):
                    for j in range (1,i+1):
                        print j,
                    print i

            
        Python while loop

            while ([expression]):
                    Body


        Python break

            [loop]:
            
                [condition] (optional)
                break

        Python continue

            [loop]:
            
                [condition] (optional)
                    continue

                [code]

        if it met the conditional it would stop at that and go to the top of the loop again

        Python pass

            [loop]
            
                [condition]
                pass
                
            [code]

        here it would keep the looping until the the condition was met, then exexute the code allowed by pass


        Python Strings
            -accessing strings

                    str = "PYTHON"
                    str[0]=  'P' =str[-6]
                    str[1]=  'Y' = str[-5]
                    str[2] = 'T' = str[-4]  ,
                    str[3] = 'H' = str[-3]
                    str[4] = 'O' = str[-2]  ,
                    str[5] = 'N' = str[-1].
                    
                    forward and backward indexing

            file : python_access_string.py

            -Python Strings Operators

                --Basic Operators:
        
                    ---String Concatenation Operator :(+)

                        "str1" + "str2" = "str1str2"
                        must be same type or you can get an errorS

                    ---Replication Operator: (*)


                        [number] * "str" = "str..."[number of times]


                --Membership Operators

                    two type in and not in

                    >>> str1="javatpoint"
                    >>> str2='sssit'
                    >>> str3="seomount"
                    >>> str4='java'
                    >>> st5="it"
                    >>> str6="seo"
                    >>> str4 in str1
                    True
                    >>> str5 in str2
                    >>> st5 in str2
                    True
                    >>> str6 in str3
                    True
                    >>> str4 not in str1
                    False
                    >>> str1 not in str4
                    True

            --Relational Operators:
        
                All the comparison operators i.e., (<,><=,>=,==,!=,<>) are also applicable to strings. The Strings are compared based on the ASCII value or Unicode(i.e., dictionary Order).

            --Slice Notation:

                <string_name>[startIndex:endIndex],
                    section from start index to end
                <string_name>[:endIndex],
                    section from start of string to end
                <string_name>[startIndex:]
                    section from start index to end of string

        -String Functions and Methods:
capitalize()	It capitalizes the first character of the String.
count(string,begin,end)	Counts number of times substring occurs in a String between begin and end index.
endswith(suffix ,begin=0,end=n)	Returns a Boolean value if the string terminates with given suffix between begin and end.
find(substring ,beginIndex, endIndex)	It returns the index value of the string where substring is found between begin index and end index.
index(subsring, beginIndex, endIndex)	Same as find() except it raises an exception if string is not found.
isalnum()	It returns True if characters in the string are alphanumeric i.e., alphabets or numbers and there is at least 1 character. Otherwise it returns False.
isalpha()	It returns True when all the characters are alphabets and there is at least one character, otherwise False.
isdigit()	It returns True if all the characters are digit and there is at least one character, otherwise False.
islower()	It returns True if the characters of a string are in lower case, otherwise False.
isupper()	It returns False if characters of a string are in Upper case, otherwise False.
isspace()	It returns True if the characters of a string are whitespace, otherwise false.
len(string)	len() returns the length of a string.
lower()	Converts all the characters of a string to Lower case.
upper()	Converts all the characters of a string to Upper Case.
startswith(str ,begin=0,end=n)	Returns a Boolean value if the string starts with given str between begin and end.
swapcase()	Inverts case of all characters in a string.
lstrip()	Remove all leading whitespace of a string. It can also be used to remove particular character from leading.
rstrip()	Remove all trailing whitespace of a string. It can also be used to remove particular character from trailing.

        file: python_functions_string.py
        
    Python Lists
        1).Python lists are the data structure that is capable of holding different type of data.
        
        2).Python lists are mutable i.e., Python will not create a new list if we modify an element in the list.
        
        3).It is a container that holds other objects in a given order. Different operation like insertion and deletion can be performed on lists.
        
        4).A list can be composed by storing a sequence of different type of values separated by commas.
        
        5).A python list is enclosed between square([]) brackets.
        
        6).The elements are stored in the index basis with starting index as 0.
        
        ex
            data1=[1,2,3,4];
            data2=['x','y','z'];
            data6=['abhinav',10,56.4,'a'];
        
        --Accessing Lists
            <list_name>[index]
            
            file python_access_list.py
            
        --Elements in a Lists
            list do foward and backward indexing however sometimes some lists
            objects are very large and have to be stored in another memory location
            
        --List Operations:
            
            ---Adding Lists: Lists can be added by using the concatenation operator(+) to join two lists.
            
            ---Replicating lists:

             It can be performed by using '*' operator by a specific number of time.
             
             ---List slicing:A subpart of a list can be retrieved on the basis of index. This subpart is known as list slice.
             
        --Other Operations:
            ---Updating elements in a List:
                <list_name>[index]=<value>
                
            ---Appending elements to a List: #appends at end
                <list_name>.append(item)
                
            --- Deleting Elements from a List:
                del statement can be used to delete an element from the list. It can also be used to delete all items from startIndex to endIndex.
        file: python_list_operations.py
                
        --Functions and Methods of Lists
            ---List functions
                min(list)	Returns the minimum value from the list given.
                max(list)	Returns the largest value from the given list.
                len(list)	Returns number of elements in a list.
                cmp(list1,list2)	Compares the two list.
                    Explanation: If elements are of the same type, perform the comparison and return the result. If elements are different types, check whether they are numbers.
                    
                    If numbers, perform comparison.
                    If either element is a number, then the other element is returned.
                    Otherwise, types are sorted alphabetically .
                    If we reached the end of one of the lists, the longer list is "larger." If both list are same it returns 0.
                list(sequence)	Takes sequence types and converts them to lists.
                
            ---List methods
                index(object)	Returns the index value of the object.
                count(object)	It returns the number of times an object is repeated in list.
                pop()/pop(index)	Returns the last object or the specified indexed object. It removes the popped object.
                insert(index,object)	Insert an object at the given index.
                extend(sequence)	It adds the sequence to existing list.
                remove(object)	It removes the object from the given List.
                reverse()	Reverse the position of all the elements of a list.
                sort()	It is used to sort the elements of the List.
    -Python Tuple
    
    data=(10,20,'ram',56.8)
    data2="a",10,20.9
    data
    (10, 20, 'ram', 56.8)
    data2
    ('a', 10, 20.9)
    
    If Parenthesis is not given with a sequence, it is by default treated as Tuple.
    
        -empty tuple
            tuple1=()
    
        -single value tuple
            Tuple1=(10,)
    
        -nested tuple
            tupl1='a','mahesh',10.56
            tupl2=tupl1,(10,20,30)
            ('a', 'mahesh', 10.56)
            (('a', 'mahesh', 10.56), (10, 20, 30))
    
        -Accessing Tuple
            file: python_access_tuple.html
      
        -Elements in a Tuple
            Data=(1,2,3,4,5,10,19,17)
            Data[0]=1=Data[-8] ,
            Data[1]=2=Data[-7] ,
            Data[2]=3=Data[-6] ,
            Data[3]=4=Data[-5] ,
            Data[4]=5=Data[-4] ,
            Data[5]=10=Data[-3],
            Data[6]=19=Data[-2],
            Data[7]=17=Data[-1]
    
        -Tuple Operations
            
            --Adding Tuple:Tuple can be added by using the concatenation operator(+) to join two tuples.
            --Replicating Tuple:Replicating means repeating. It can be performed by using '*' operator by a specific number of time.
            --Tuple slicing:A subpart of a tuple can be retrieved on the basis of index. This subpart is known as tuple slice.
    
        -Other Operations:
        
            --Updating elements in a tuple:
                cant do that but you can make new tuples by concatenating them
                
            --Deleting elements from Tuple:
                cant but delete whole tuple
                if you do cant print again because  print data  will show an error since tuple data is already deleted
                
            file: python_tuple_operations.py
        -Functions of Tuple
            min(tuple)	Returns the minimum value from a tuple.
            max(tuple)	Returns the maximum value from the tuple.
            len(tuple)	Gives the length of a tuple
            cmp(tuple1,tuple2)	Compares the two Tuples.
            tuple(sequence)	Converts the sequence into tuple.
            file: python_tuple_functions.py
            
        -Why Use Tuple?
            Processing of Tuples are faster than Lists.
            It makes the data safe as Tuples are immutable and hence cannot be changed.
            Tuples are used for String formatting.
            
    -Python Dictionary
        Dictionary is an unordered set of key and value pair.
        data={100:'Ravi' ,101:'Vijay' ,102:'Rahul'}
        print data
        
        -Accessing Values
            file: python_access_dict.py
            
        -Updation: all values can be changed
            file : python_update_dict.py
            
        -Deletion:
            syntax
            del  [key]
            can delete whole dict but show an error while printing
            file : python_delete_dict.py
            
        --Functions and Methods
            ---functions
            len(dictionary)	Gives number of items in a dictionary.
            cmp(dictionary1,dictionary2)	Compares the two dictionaries.
              If, dictionary1 == dictionary2, returns 0.
              dictionary1 < dictionary2, returns -1.
              dictionary1 > dictionary2, returns 1.

            str(dictionary)	Gives the string representation of a string.
            file :python_functions_dict.py
            
            ----methods
            keys()	Return all the keys element of a dictionary.
            values()	Return all the values element of a dictionary.
            items()	Return all the items(key-value pair) of a dictionary.
            update(dictionary2)	It is used to add items of dictionary2 to first dictionary.
            clear()	It is used to remove all items of a dictionary. It returns an empty dictionary.
            fromkeys(sequence,value1)/ fromkeys(sequence)	It is used to create a new dictionary from the sequence where sequence elements forms the key and all keys share the values ?value1?. In case value1 is not give, it set the values of keys to be none.
            copy()	It returns an ordered copy of the data.
            has_key(key)	It returns a boolean value. True in case if key is present in the dictionary ,else false.
            get(key)	Returns the value of the given key. If key is not present it returns none.
            
            file: python_methods_dict.py
            
    -Python Functions
        there are built in and user-defined functions
        
        -Defining a Function:
            def [ function_name]([parameters]):
                
        -Invoking a Function:
            [ function_name]([parameters]):
                
        file: python_define_invoke_function.py
        
        -return Statement:
            return value,none or end the function
            file: python_return_function.py
            
        -Argument and Parameter:
            argument is in the function call
            parameter is in the function definition
            
            --Passing Parameters
                ---Positional/Required Arguments:
                    function call statement must match the number and order of arguments
                    def sum(a,b):
                                "Function having two parameters"
                             c=a+b
                                  print c
                      
                    sum(10,20)
                                
                ---Default Arguments
                    parameter already has value
                    #Function Definition
                    def msg(Id,Name,Age=21):
                                "Printing the passed value"
                                print Id
                             print Name
                             print Age
                             return
                    #Function call
                    msg(Id=100,Name='Ravi',Age=20)
                    msg(Id=101,Name='Ratan') #age here will be default 21
                    
                ---Keyword Arguments:
                    if parameter and type are same order does not matter
                    
            --Anonymous Function:
                Anonymous Functions are the functions that are not bond to name.
                Anonymous Functions are created by using a keyword "lambda".
                Lambda takes any number of arguments and returns an evaluated expression.
                Lambda is created without using the def keyword.
                            
                lambda arg1,args2,args3,?,argsn :expression
                    #Function Definiton
                    square=lambda x1: x1*x1
                      
                    #Calling square as a function
                    print "Square of number is",square(10)
                                
                ---the difference between normal and anomyomous is that anomyous does not need def and when calling does not need  a return in order to return
    
            --Scope of Variable:
                ---local variable
                    variable declared inside function body
                    
                ---global variable
                    declared outside body
                    
    -Python File i/o
        --print statement:
            if actual expresison
            print "[expresison]"
            if variable
            print [expresison]
            
        --Input from Keyboard:
            ---input(); it evaluates what you put in mathematical equation
            input("Expression")
            
            ---raw_input(): it takes your input and converts it to a string
                string is default else it has to be typecasted
                
                file: python_typecast_input.py
                
        --File Handling:
            ---File Operations
                ----to open  a file
                    obj=open(filename , mode , buffer)
                        filename: name of file as a string
                        mode: read = r write = w (For overwrite) append = a
                ---- to close a file
                        obj.close()
                        
                ---- writing to a file
                     obj.write(str)
                     
                ---- reading from a file
                     obj.read(value)
                        number of bytes to be read, if no value, reads to the end of the
                        file
                        
                file: python_read_write_file.py
                    
        --Attributes of File:
            ---Mode	Returns the mode in which file is being opened.
r	It opens in Reading mode. It is default mode of File. Pointer is at beginning of the file.
rb	It opens in Reading mode for binary format. It is the default mode. Pointer is at beginning of file.
r+	Opens file for reading and writing. Pointer is at beginning of file.
rb+	Opens file for reading and writing in binary format. Pointer is at beginning of file.
w	Opens file in Writing mode. If file already exists, then overwrite the file else create a new file.
wb	Opens file in Writing mode in binary format. If file already exists, then overwrite the file else create a new file.
w+	Opens file for reading and writing. If file already exists, then overwrite the file else create a new file.
wb+	Opens file for reading and writing in binary format. If file already exists, then overwrite the file else create a new file.
a	Opens file in Appending mode. If file already exists, then append the data at the end of existing file, else create a new file.
ab	Opens file in Appending mode in binary format. If file already exists, then append the data at the end of existing file, else create a new file.
a+	Opens file in reading and appending mode. If file already exists, then append the data at the end of existing file, else create a new file.
ab+	Opens file in reading and appending mode in binary format. If file already exists, then append the data at the end of existing file, else create a new file.
                    
        --Methods for file handling:
            #There is a module "os" defined in Python that provides various functions which are used to perform various operations on Files. To use these functions 'os' needs to be imported.
Method	Description
rename()	It is used to rename a file. It takes two arguments, existing_file_name and new_file_name.
    ex.
        os.rename(existing_file_name, new_file_name)
        
remove()	It is used to delete a file. It takes one argument. Pass the name of the file which is to be deleted as the argument of method.
    ex.
        os.remove(file_name)
mkdir()	It is used to create a directory. A directory contains the files. It takes one argument which is the name of the directory.
    ex.
        os.mkdir("file_name")
chdir()	It is used to change the current working directory. It takes one argument which is the name of the directory.
    ex.
        os.chdir("file_name")
getcwd()	It gives the current working directory.
        ex.
            os.getcwd()
rmdir()	It is used to delete a directory. It takes one argument which is the name of the directory. but the directory must be empty first
    ex.
        os.rmdir("directory_name")
tell()	It is used to get the exact position in the file.

    file: python_methods_file.py
    

    -Python Modules
        good for reusability and categorization
        --importing a modules
            single
            import [file_name], [file_name] ... #file name is a module here
            
            multiple
            import file_name],  [file_name] ...
            
            --- to make one
                place code, classes and functions in a file
                
            ---to use
                [module].[functional].[exectutable_name]([parameters]...)
                
            ---Using from.. import statement: #when you do not need all of the
                from [module] import [needed_action_code]
                file: python_from_import_module.py
                
            ---To import whole module:
                from [module] import *
                
        --Built in Modules in Python:
            ---math module
            
            
Function	Description
ceil(n)	Returns the next integer number of the given number
sqrt(n)	Returns the Square root of the given number.
exp(n)	Returns the natural logarithm e raised to the given number
floor(n)	Returns the previous integer number of the given number.
log(n,baseto)	Returns the natural logarithm of the number.
pow(baseto, exp)	Returns baseto raised to the exp power.
sin(n)	Returns sine of the given radian.
cos(n)	Returns cosine of the given radian.
tan(n)	Returns tangent of the given radian.

Constants	Descriptions
Pi	Returns constant ? = 3.14159...
ceil(n)	Returns constant e= 2.71828...

            --file: python_math.py
            ---random module
random()	It returns a random number between 0.0 and 1.0 where 1.0 is exclusive.
randint(x,y)	It returns a random number between x and y where both the numbers are inclusive.
            --file :python_random.py
            
        --Package

            A Package is simply a collection of similar modules, sub-packages etc..
            to do
                1) Create the directory:
                
                import os
                os.mkdir("Info")
                2) Place different modules in package: (Save different modules inside the Info package)
                
                msg1.py
                
                def msg1():
                    print "This is msg1"
                msg2.py
                
                def msg2():
                    print "This is msg2"
                msg3.py
                
                def msg3():
                    print "This is msg3"
                3) Create __init__.py file:
                
                from msg1 import msg1
                from msg2 import msg2
                from msg3 import msg3
                4)Import package and use the attributes:
                
                import Info
                Info.msg1()
                Info.msg2()
                Info.msg3()
                
        --directory: python_package
        # learn how to write python to file properly, hint doesn't matter if its all string just need proper format
        #when making calls to modules, the information in the file must be written in the file, before they are called through package reference, or Python 2.6.2 will not see them because it runs the functions in the given module before writing to them
        
    -Python exception handling
        ZeroDivisionError: Occurs when a number is divided by zero.
        NameError: It occurs when a name is not found. It may be local or global.
        IndentationError: If incorrect indentation is given.
        IOError: It occurs when Input Output operation fails.
        EOFError: It occurs when end of file is reached and yet operations are being performed
        
        --Exception Handling:
            work as a switch, does certain things if malicious code occurs
            try:
                malicious code
            except Exception1:
                execute code
            except Exception2:
                execute code
            ....
            ....
            except ExceptionN:
                execute code
        
            except Exception1,Exception2,Exception3,..,ExceptionN
                execute this code in case any Exception of these occur.
            else:
                In case of no exception, execute the else block code.
            
            once the exception is completed, python continues to the next code block in the sequence
                
            file: python_except_basic.py
                  python_all_exception.py
                  python_multiple_except.py
                  
        --Finally Block:
            if user wants something executed regardless of execption results
            try:
                Code
            finally:
                code which is must to be executed.
                
            python_finally_except.py
            
        --Raise Exception
            your own custom exception
            ---syntax
                raise [Exception_class]([value])
                except [Exception_class] as [variable]
                # variable stores the value of the exception
            file:python_raise_exception.py
                
        --Custom exception class
            user defined exception
            class [exception class](Exception):
                [init function]
                
            try:
                raise [exception class]([arguments for __init__ ])
            except  [exception class] as [variable]:
                do things
                
            repr()
            is used when return class values of objects, but returning it regularly seems to work just fine
            file: python_custom_exception.py
            
    -Python Date and Time
    
        --Retrieve Time
            import time;
            localtime = time.localtime(time.time())
            epoch = time.time()
            print "Current Time is :", localtime
            print "the epoch is:", epoch
            #time() returns the number of seconds ever since 12:00 am , January 1,1970.
            #local time returns an object with data containing the exact time that it is right now
            
            Attribute	Description
            tm_year	Returns the current year
            tm_mon	Returns the current month
            tm_mday	Returns the current month day
            tm_hour	Returns the current hour.
            tm_min	Returns the current minute
            tm_sec	Returns current seconds
            tm_wday	Returns the week day
            tm_yday	Returns the year day.
            tm_isdst	It returns -1,0 or 1.
            
            file: python_retrieve_time.py
            
        --Formatted Time
        
            use time.asctime() in order to do the formatting
            
        --time module:

            Methods	                Description
            time()	                Returns floating point value in seconds since epoch i.e.,12:00am, January 1,                        1970
            asctime(time)	        It takes the tuple returned by localtime() as parameter. It returns a 24                            character string.
            sleep(time)	             The execution will be stopped for the given interval of time.
            strptime(String,format)	It returns an tuple with 9 time attributes. It receives an String of date and a                     format, which are registed as casting
            
            
            
            %a	weekday name.
            %b	month name
            %c	date and time
            %e	day of a month
            %m	month in digit.
            %n	new line character.
            %S	second
            %t	tab character
            
            gtime()/gtime(sec)	    It returns struct_time which contains 9 time attributes. In case seconds are not                     specified it takes current second from epoch.
            mktime()	            Returns second in floating point since epoch.
            strftime(format)/strftime(format,time)	Returns time in particular format. If time is not given, current                                     time in seconds is fetched.
            
        --Calendar
            its own python module
            
            ---calendar module
            
                Methods	                        Description
                prcal(year)	                    Prints the whole calendar of the year.
                firstweekday()	                Returns the first week day. It is by default 0 which specifies                                  Monday
                isleap(year)	                Returns a Boolean value i.e., true or false. True in case given year                             is leap else false.
                monthcalendar(year,month)	    Returns the given month with each week as one list.
                leapdays(year1,year2)	        Return number of leap days from year1 to year2
                prmonth(year,month)	            Print the given month of the given year
            
            

        
            
            
            