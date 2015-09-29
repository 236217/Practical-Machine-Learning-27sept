string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

###################################### ASKING FOR INPUT AND STORING IT IN VARIABLE ###########################
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

########## 3 WAYS TO CRAETE STRING###############
'Alpha'
"Bravo"
str(3)
########### STRING METHOD ############
len("Charlie")
"Delta".upper()
"Echo".lower()
######## PRINTING SCREEN ############
print "Foxtrot"

####### ADVANCED PRINTING TECHNIQUES ########
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)

###### importing date time format ##########
from datetime import datetime

#################################
from datetime import datetime
now =  datetime.now()
current_year = now.year
current_month=now.month
current_day=now.day
print "today datetime info %s _%s _ %s" % (current_year,current_month,current_day)

##############################
from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute,now.second)
############### CONTROL FLOW #################
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()
#############COMPARATORS##############
Equal to (==)
Not equal to (!=)
Less than (<)
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=)
#######################################
AND , OR , NOT

TRUE AND FALSE : FALSE
TRUE OR FALSE : TRUE
TRUE AND NOT TRUE : TRUE
NOT TRUE MEANS FALSE

#######################################
not is evaluated first;
and is evaluated next;
or is evaluated last.
Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.
################Conditional Statement Syntax- IF ELSE ###########################
answer = "Left"
if answer == "Left":
    print " you are awesome!!"
	
############# if else inside function #####################
def using_control_once():
    if 2==2:
        return "Success #1"
	else :
		return "abhishek"

def using_control_again():
    if 3<5:
        return "Success #2"

print using_control_once()
print using_control_again()

###########	IF -ELIF-ELSE ########################
def greater_less_equal_5(answer):
    if answer == 4:
        return 1
    elif answer==5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


	
