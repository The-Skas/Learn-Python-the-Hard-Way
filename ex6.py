#The variable 'x' is assigned a string containing '%d'
#which is number formatter.
x = "There are %d types of people." % 10

binary = "binary"
do_not = "don't"
#The variable 'y' is assigned a string containing the variables:
# binary , do_not. which are strings

y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#This line uses the %r formatter, which places quotes around the string.
print "I said: %r." % x
#This %s formatter has single quots placed around it, doing the same job as %r.
print "I also said: '%s'." %y

hilarious = False
#There doesnt seem to be a different in %s, or %r when it comes to displaying boolean data.
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w+e