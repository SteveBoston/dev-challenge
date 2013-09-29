# Exercises for chapter 2:

# Name: Steve Gallagher



# EXERCISE 2.1



# Python reads numbers whose first digit is 0 as base 8 numbers (with integers 0-7 allowed), 
# and then displays their base 10 equivalents.



# EXERCISE 2.2



# 5---------------> displays the number 5
# x = 5-----------> assigns the value "5" to the variable "x". Does not display anything.
# x + 1-----------> displays the sum of 5 and 1------>6.

# The script evaluates x + 1, but does not display a result. Changing the last line to "print x + 1"
# makes the script display "6"



# EXERCISE 2.3



width = 17 
height = 12.0
delimeter = '.'

#1. width/2 ---------> 8 (Floor Division-answer is an integer)
#2. width/2.0--------> 8.5 (Floating Point Division- answer is a float)
#3. 1 + 2 * 5--------> 11 (integer)
#4. delimeter * 5----> '.....' (string)



# EXERCISE 2.4



#1. (4/3.0)*(math.pi)*(5**3)------>523.5987755982989

#2.   bookcount = 60
    # shipping = 3 + (bookcount-1) * .75
    # bookprice = 24.95 * .6
    # totalbookprice = bookprice * bookcount
    # totalbookprice + shipping-------------------->945.4499999999999 (round to $945.45)

#3 	  (8 * 60) + 15---------> 495 (easy pace in seconds per mile)
	# 495 * 2---------------> 990 (total time in seconds at easy pace)
	# (7 * 60) + (15)-------> 435 (tempo pace in seconds per mile)
	# 435 * 3---------------> 1305 (total time in seconds at tempo pace)
	# 1305 + 990------------> 2295 (total time in seconds)
	# divmod (2295, 60)-----> (38, 15)---------> 38:15 (total time in minutes)
	# 7:30:15 am
