# Exercises for chapter 3:

# Name: Steve Gallagher



# EXERCISE 3.1



# Error message------->NameError: name 'repeat_lyrics' is not defined



# EXERCISE 3.2



# The program still runs normally.



# EXERCISE 3.3



def right_justify(s):
    stringlength = len(s)
    print "The length of the string is: ", stringlength
    numberofspaces = 70 - stringlength
    print "The number of blank spaces needed is: ", numberofspaces
    print (" " * numberofspaces) + s


right_justify('This is a test string')



# EXERCISE 3.4



    #1.



def do_twice(f):
    f()
    f()

def print_a_string():
    print "This is my test string."


do_twice(print_a_string)




    #2.



def do_twice(f,m):
    f(m)
    f(m)

def print_a_string(m):
    print m


do_twice(print_a_string, "This is my test string.")




    #3.



def print_twice(x):
    print x
    print x


print_twice("This is my test string.")




    #4.



def do_twice(f,m):
    f(m)
    f(m)

def print_twice(m):
    print m
    print m

do_twice(print_twice, "spam")



    #5.



def do_four(f,m):
    do_twice(f,m)
    do_twice(f,m)

def do_twice(f,m):
    f(m)
    f(m)

def print_twice(m):
    print m
    print m

do_four(print_twice,"This is a test string.")



# EXERCISE 3.5



    #1.


def gridprint():
    print "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+"

def spacerprint():
    print "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|"

def quadruple(f):
    f()
    f()
    f()
    f()

gridprint()
quadruple(spacerprint)
gridprint()
quadruple(spacerprint)
gridprint()



    #2.


def gridpiece():
    print "+", "-", "-", "-", "-",

def spacerpiece():
    print "|", " ", " ", " ", " ",

def quadruplegrid(f):
    f()
    f()
    f()
    f()
    print "+"

def quadruplespacer(g):
    g()
    g()
    g()
    g()
    print "|"

def row():
    quadruplegrid(gridpiece)
    quadruplespacer(spacerpiece)
    quadruplespacer(spacerpiece)
    quadruplespacer(spacerpiece)
    quadruplespacer(spacerpiece)

row()
row()
row()
row()
quadruplegrid(gridpiece)


