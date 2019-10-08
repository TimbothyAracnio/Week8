# more strings and text

# this is a variable that equals a string with number attached
x = "There are %d types of people" % 3

# this is a variable that is assigned to a string
goodAtMath = "good at math"
# this is a variable that is assigned to a string
badAtMath = "not"

# this is a variable that equals a string with two other variables
y = "Those who are %s and those who are %s" % (goodAtMath, badAtMath)

# this prints a string
print(x)
# this prints a string
print(y)

# this prints a string with a variable
print("I said: %r.:" % x)
# this prints a string with a variable
print("I also said: '%s'." % y)


# this is a boolean variable
hilarious = True
# this is a variable that is assigned to a string
jokeEvaluation = "Isn't that joke so funny?! %r"
print(jokeEvaluation % hilarious)

# this is a variable that is assigned to a string
w = "This is the left side of..."
# this is a variable that is assigned to a string
e = "a string with a right side."

# this prints two strings attached to each other
print(w + e)

# more printing funn

# these print strings
print("Mary had a little lamb,")
print("little lamb,")
print("LITTLE LAMB!")
print("Mary had a little lamb,")
print("It's fleece was white as %s." % 'snow')
print("and everywhere that Mary went,")
print("Mary went,")
print("MARY WENT!")
print("everywhere that Mary went,")

# this prints strings times a specific multiplier
print("." * 10)

# SEVERAL variables that are assigned to strings
end1 = "H"
end2 = "a"
end3 = "m"
end4 = "b"
end5 = "u"
end6 = "r"
end7 = "g"
end8 = "e"
end9 = "r"

# these print several strings attached to each other
print(end1 + end2 + end3,)
print(end4 + end5 + end6 + end7 + end8 + end9)

# theres more =\
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("dig","dag","dug","dog"))
print(formatter % (True, False, True, True))
print(formatter % (formatter,formatter,formatter,formatter))

# why do I use %r instead of %s in the above example?
# so we can use different types of variables