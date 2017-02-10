
# [PyNet Python + Ansible] - Class9 / Writing Reusable Code



##1. Create a directory called mytest with three Python modules world.py, simple.py, whatever.py.

     ###a. These three files should each have a function that prints a statement when called
     ###b. Use the __name__ technique to separate executable code from importable code. Each module should contain executable code.

```
applied_python)[cdeluna@ip-172-30-0-7 ~]$ ls
ANSIBLE  ansible-hosts  applied_python  creds.yml  DJANGOX  group_vars  JUNIPER  napalm-ansible  PyNetACert
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ mkdir mytest
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ ls
ANSIBLE  ansible-hosts  applied_python  creds.yml  DJANGOX  group_vars  JUNIPER  mytest  napalm-ansible  PyNetACert
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ ls
ANSIBLE  ansible-hosts  applied_python  creds.yml  DJANGOX  group_vars  JUNIPER  mytest  napalm-ansible  PyNetACert
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ cd mytest/
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ ls
world.py
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ ls
simple.py  whatever.py  world.py
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ python simple.py
This is the executable part of the code for module simple.py!
This is simple as 3.14159265359
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ pip install cowpy
You are using pip version 6.0.8, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
Collecting cowpy
  Downloading cowpy-1.0.1.tar.gz
Installing collected packages: cowpy
  Running setup.py install for cowpy
    changing mode of build/scripts-2.7/cowpy from 664 to 775
    changing mode of /home/cdeluna/applied_python/bin/cowpy to 775
Successfully installed cowpy-1.0.1
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ python whatever.py 
This is the executable part of the code for module whatever.py!
Would you like to add a new word? no
 ______________________________________________________ 
< ('The king', 'spies on', 'my mom', 'for a disease.') >
 ------------------------------------------------------ 
  o
   o   \_\_    _/_/
    o      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ python whatever.py 
This is the executable part of the code for module whatever.py!
Would you like to add a new word? yes
Please enter a singular noun.Copernicus
 __________________________________________________________ 
< ('My mom', 'configures', 'copernicus', 'for a disease.') >
 ---------------------------------------------------------- 
  o
   o   \_\_    _/_/
    o      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ 
```


     ###c. Verify that you are NOT able to import ./mytest 


```
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ ls
ANSIBLE  ansible-hosts  applied_python  creds.yml  DJANGOX  group_vars  JUNIPER  mytest  napalm-ansible  PyNetACert
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ python
Python 2.7.12 (default, Sep  1 2016, 22:14:00)
[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import mytest
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named mytest
>>> import whatever
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named whatever
>>>
```

##2. Make mytest a package.

    ###a. In the __init__.py file import each of the functions in world.py, simple.py, whatever.py.
    ###b. Test out your package from the Python interpreter shell. Make sure you can invoke your three functions using both 'import mytest' and 'from mytest import func1, func2, func3'. Once again do this from the directory containing ./mytest.

```
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ ls
ANSIBLE  ansible-hosts  applied_python  creds.yml  DJANGOX  group_vars  JUNIPER  mytest  napalm-ansible  PyNetACert
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ ls -al mytest/
total 40
drwxrwxr-x  2 cdeluna cdeluna 4096 Feb  9 21:38 .
drwx------ 14 cdeluna cdeluna 4096 Feb  9 21:27 ..
-rw-rw-r--  1 cdeluna cdeluna  367 Feb  9 21:38 __init__.py
-rw-rw-r--  1 cdeluna cdeluna  507 Feb  9 21:38 __init__.pyc
-rw-rw-r--  1 cdeluna cdeluna  900 Feb  9 21:00 simple.py
-rw-rw-r--  1 cdeluna cdeluna 1040 Feb  9 21:38 simple.pyc
-rw-rw-r--  1 cdeluna cdeluna 2661 Feb  9 21:41 whatever.py
-rw-rw-r--  1 cdeluna cdeluna 2696 Feb  9 21:28 whatever.pyc
-rw-rw-r--  1 cdeluna cdeluna 1020 Feb  9 20:58 world.py
-rw-rw-r--  1 cdeluna cdeluna 1138 Feb  9 21:38 world.pyc
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ python
Python 2.7.12 (default, Sep  1 2016, 22:14:00)
[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import mytest
>>> mytest.func1()
This is the importable part of the code!
Today your number is 824415
824415
>>> mytest.func2()
This is simple as 3.14159265359
>>> mytest.func3()
Would you like to add a new word? yes
Please enter a singular noun. Faraday
 ______________________________________________________________________________
< ('A cat with rabies', 'meets with', 'superman', 'because the sky is green.') >
 ------------------------------------------------------------------------------
  o
   o   \_\_    _/_/
    o      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
('A cat with rabies', 'meets with', 'superman', 'because the sky is green.')
>>> from mytest import func1, func2, func3
>>> func1()
This is the importable part of the code!
Today your number is 328139
328139
>>> func2()
This is simple as 3.14159265359
>>> func3()
Would you like to add a new word? no
 ____________________________________________________________________
< ('A sloth', 'configures', 'your homie', 'for no apparent reason.') >
 --------------------------------------------------------------------
  o
   o   \_\_    _/_/
    o      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
('A sloth', 'configures', 'your homie', 'for no apparent reason.')
>>>
>>>
>>> exit
```



##3. Add a __all__ variable to your __init__.py file.

Test out __all__ using 'from mytest import *'. Verify that you can directly execute func1(), func2(), func3(). Once again do this from the directory containing ./mytest.


Works as expected

```
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ pwd
/home/cdeluna
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ python
Python 2.7.12 (default, Sep  1 2016, 22:14:00)
[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mytest import *
>>> func1()
This is the importable part of the code!
Today your number is 44649
44649
>>> func2()
This is simple as 3.14159265359
>>> func3()
Would you like to add a new word? no
 _________________________________________________________________________________________________________
< ('This cool guy my gardener met yesterday', 'gives', 'your homie', 'to be able to make toast explode.') >
 ---------------------------------------------------------------------------------------------------------
  o
   o   \_\_    _/_/
    o      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
('This cool guy my gardener met yesterday', 'gives', 'your homie', 'to be able to make toast explode.')
>>>



##4. Create a class MyClass in world.py.

    ###a. This class should require that three variables be passed in upon initialization.
    ###b. Write two methods associated with this class 'hello' and 'not_hello'. Have both these methods print a statement that uses all three of the initialization variables.

```
>python world.py
This is the executable part of the code for module world.py!
This is the importable part of the code!
Today your number is 145628
145628
Enter value for variable a: thunder
Enter value for variable b: sky
Enter value for variable c: lightning
 ______________________________
< Hello thunder sky lightning! >
 ------------------------------
     o
      o  (__)
         (\/)
  /-------\/
 / | 666 ||
*  ||----||
   ~~    ~~
None
 ________________________________
< Goodbye thunder sky lightning! >
 --------------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (xx)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
None


```



##5. Write a child class MyChildClass of MyClass. This child class should override the 'hello' method and print a different statement.

```
>python world.py
This is the executable part of the code for module world.py!
This is the importable part of the code!
Today your number is 369213
369213
Enter value for variable a: winter
Enter value for variable b: fall
Enter value for variable c: summer
 ___________________________
< Hello winter fall summer! >
 ---------------------------
  \
   \ ,   _ ___.--'''`--''//-,-_--_.
      \`"' ` || \\ \ \\/ / // / ,-\\`,_
     /'`  \ \ || Y  | \|/ / // / - |__ `-,
    /\@"\  ` \ `\ |  | ||/ // | \/  \  `-._`-,_.,
   /  _.-. `.-\,___/\ _/|_/_\_\/|_/ |     `-._._)
   `-'``/  /  |  // \__/\__  /  \__/ \
        `-'  /-\/  | -|   \__ \   |-' |
          __/\ / _/ \/ __,-'   ) ,' _|'
         (((__/(((_.' ((___..-'((__,'
None
 _____________________________
< Goodbye winter fall summer! >
 -----------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (xx)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
None
 _______________
< Hello summer! >
 ---------------
     o   ^__^
      o  (..)\_______
         (__)\       )\/\
          U  ||----w |
           ||     ||
None

```



##6. Optional bonus question -- have MyChildClass augment the __init__() method. In other words, the child class should do something additional in the __init__() method yet still call its parent class __init__().

```
>python world.py
This is the executable part of the code for module world.py!
This is the importable part of the code!
Today your number is 583352
583352
Enter value for variable a: some
Enter value for variable b: stupid
Enter value for variable c: thing
 __________________________
< Hello some stupid thing! >
 --------------------------
  \            .    .     .
   \      .  . .     `  ,
    \    .; .  : .' :  :  : .
     \   i..`: i` i.i.,i  i .
      \   `,--.|i |i|ii|ii|i:
           U@@U\.'\@\@\@\@\@\@`.||'
           \__/(\@\@\@\@\@\@\@\@\@\@)'
                (\@\@\@\@\@\@\@\@)
                `YY~~~~YY'
                 ||    ||
None
 ____________________________
< Goodbye some stupid thing! >
 ----------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (xx)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
None
Printing new_hello method
 _____________
< Hello some! >
 -------------
   o         __------~~-,
    o      ,'            ,
          /               \
         /                :
        |                  '
        |                  |
        |                  |
         |   _--           |
         _| =-.     .-.   ||
         o|/o/       _.   |
         /  ~          \ |
       (____\@)  ___~    |
          |_===~~~.`    |
       _______.--~     |
       \________       |
                \      |
              __/-___-- -__
             /            _ \
None
Printing new_random method
92
None

```


##7. Modify your PYTHONPATH such that the directory containing ./mytest is now on your PYTHONPATH. Verify this in sys.path.

Note error in updating $PATH vs $PYTHONPATH

```
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ echo $PATH
/home/cdeluna/applied_python/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/aws/bin:/home/cdeluna/.local/bin:/home/cdeluna/bin
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ pwd
/home/cdeluna
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ cd mytest/
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ ls
__init__.py  __init__.pyc  simple.py  simple.pyc  whatever.py  whatever.pyc  world.py  world.pyc
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ pwd
/home/cdeluna/mytest
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ PATH=$PATH:/home/cdeluna/mytest
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ echo $PATH
/home/cdeluna/applied_python/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/aws/bin:/home/cdeluna/.local/bin:/home/cdeluna/bin:/home/cdeluna/mytest
(applied_python)[cdeluna@ip-172-30-0-7 mytest]$ cd ..
(applied_python)[cdeluna@ip-172-30-0-7 ~]$ cd PyNetACert/week9
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ vi test.py
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ ls
mytest  test.py
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ python test.py
Traceback (most recent call last):
  File "test.py", line 1, in <module>
    import mytest
ImportError: No module named mytest
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ echo $PATH
/home/cdeluna/applied_python/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/aws/bin:/home/cdeluna/.local/bin:/home/cdeluna/bin:/home/cdeluna/mytest
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ echo $PYTHONPATH
/home/cdeluna/DJANGOX/djproject/
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ PYTHONPATH=$PYTHONPATH:/home/cdeluna/mytest
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ echo $PYTHONPATH
/home/cdeluna/DJANGOX/djproject/:/home/cdeluna/mytest
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ python test.py
Traceback (most recent call last):
  File "test.py", line 1, in <module>
    import mytest
ImportError: No module named mytest
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ PYTHONPATH=$PYTHONPATH:/home/cdeluna/
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ echo $PYTHONPATH
/home/cdeluna/DJANGOX/djproject/:/home/cdeluna/mytest:/home/cdeluna/
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ python test.py
Function 1 from mytest package
This is the importable part of the code!
Today your number is 845836
845836
Function 2 from mytest package
This is simple as 3.14159265359
None
Function 3 from mytest package
Would you like to add a new word? summer
 ________________________________________________________________________
< ('A dude', 'meows on', 'a cat with rabies', 'for no apparent reason.') >
 ------------------------------------------------------------------------
  o
   o   \_\_    _/_/
    o      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
('A dude', 'meows on', 'a cat with rabies', 'for no apparent reason.')
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ pwd
/home/cdeluna/PyNetACert/week9
(applied_python)[cdeluna@ip-172-30-0-7 week9]$

```


##8. Update the __init__.py file and the __all__ variable to include MyClass.

Completed

##9. Write a Python script in a different directory (not the one containing mytest).

    ###a. Verify that you can import mytest and call the three functions func1(), func2(), and func3().
    ###b. Create an object that uses MyClass. Verify that you call the hello() and not_hello() methods.

```
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ python test.py
Function 1 from mytest package
This is the importable part of the code!
Today your number is 629879
629879
Function 2 from mytest package
This is simple as 3.14159265359
None
Function 3 from mytest package
Would you like to add a new word?
 __________________________________________________
< ('My mom', 'treats', 'a dude', 'to make a pie.') >
 --------------------------------------------------
  o
   o   \_\_    _/_/
    o      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
('My mom', 'treats', 'a dude', 'to make a pie.')


Class MyClass
<mytest.world.MyClass object at 0x7fa570a31850>
 _________________________
< Hello some other thing! >
 -------------------------
  o
     o
                  _ _
       | \__/|  .~    ~.
       /.. `./      .'
      {o__,   \    {
        / .  . )    \
        `-` '-' \    }
       .(   _(   )_.'
      '---.~_ _ _|
None
 ___________________________
< Goodbye some other thing! >
 ---------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (xx)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
None
(applied_python)[cdeluna@ip-172-30-0-7 week9]$ pwd
/home/cdeluna/PyNetACert/week9
(applied_python)[cdeluna@ip-172-30-0-7 week9]$

```


This was fun and informative!  Thx!
