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

# which should I use on a regular basis?
# probably %r, but it is good to use the others to be specific

# why does %r sometimes give me single quotes around things
# I'm not sure

# this is a variable that is assigned to a string
days = "Mon Tue Wed Thu Fri Sad"
# this is a variable that is assigned to a string; the \n are like new lines
months = "\nJanett\nFebil\nMargrette\nAproval... which I don't have\nMay I go to the re-\n\nNO!\n\nJunction function whats your runction\nJulie\nAugh... why wont it work?\nSeptiguat\nOctopus\nNovice\nDecades of men"


print("These are the Days: ", days)
print("These are the Months: ", months)

print("""
or 7?
what about 7?
will it work?
I don't know,
only my typing speed will tell...
.
.
AHA!!! I knew it!
You CAN do 7!
""")

numbers = """
1
2
3
4
5
6
7
8
9"""

# analize the following
print("I count my defecation, here: %r" % numbers)
print("I count my urination, here: %s" % numbers)

# escape sequences.. whatever that means
thingOne = "Thing One: \twatch me move!"
thingTwo = "Thing Two: watch me \\ split!"
thingThree = "Thing Three: watch me \n crush \n the \n souls \n of \n puny \n children."
print("Our story starts in a Dr. Suess book that has been corupted: ")

print(thingOne)
print(thingTwo)
print(thingThree)

# what do these do?
# \\
print("These adds a \\ where if you normally put one it wouldn't show up")

# \'
print("This adds a \' where if you normally put one it wouldn't show up")

# \"
print("This adds a \" where if you normally put one it wouldn't show up")

# \a
print("apparently it's supposed to make a \a bell noise but it didn't happen for me")

# \b
print("This removes the previous character\b")

# \f
print("this I think adds\fa space, but I looked it up and it says it makes a formfeed")

# \n
print("This makes \n a new line")

# \N{name}
print("this adds Emojis!!! \N{face with tears of joy}")

# \r
print(" This \r Removes all characters before it")

# \t
print("This \t creates a tab!")

# \uxxxx
print("this \u041b is a 16-bit hex value that makes symbols")

# \Uxxxxxxxx
print("this \U000001a9 is a 32-bit hex value that makes symbols")

# \v
print("the cow jumped \v over the moon")

# \ooo
print("Prints an Ascii \105")

# \xhh
print("Prints a hexidecimal \x21 ")

# what does this do?

# It makes a twirly thing
while False:
    for i in ["/", "-", "\\", "|"]:
        print("%s\r" % i, end='')

# This lets you make inputs and can print them!!! =D
# age = input("How old are you?")
# height = input("how tall are you?")

# prints the inputs
# print("So, you are %s years old and %s tall." % (age, height))

print("\n\n\n\n\n\n")

# ask 4 more questions and answer them

# Can I make a user and password?
user = input("Username: ")
if user == "Panda123":
    password = input("Password: ")
    if password == "password":
        print("Hello Panda123!")
    else:
        print("Incorrect password.")

else:
    print("This user does not exist.")
# yes!


# Can I use any emoji?
# print("\N{pile of poop}")
# no

# (filler question) what does the fox say?
# ...

# Can I just get onto the story? I'm tired and have a lot of homework
# sure
# yay!


# The story!!!
char = "cat"

def nameOpt():
    char = input("What would you like your characters name to be?: ")
    nameOption = input("You would like your character to be named %r? \n(y/n) " % char)
    if nameOption == "n":
        nameOpt()
    elif nameOption == "y":
        print("\n\n\nAlright %s lets begin the story!\n" % char)
    else:
        print("I don\'t speak that coding language")
        nameOpt()

print("\n\n\n\n\n\n\n\n")

print("Welcome to the \"create your own adventure\" adventure!\n")
nameOpt()
print("It was a Dark and stormy night")




