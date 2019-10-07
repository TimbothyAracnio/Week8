# more strings and text

x = "There are %d types of people" % 3

goodAtMath = "good at math"
badAtMath = "not"
y = "Those who are %s and those who are %s" % (goodAtMath, badAtMath)

print(x)
print(y)

print("I said: %r.:" % x)
print("I also said: '%s'." % y)

hilarious = True
jokeEvaluation = "Isn't that joke so funny?! %r"
print(jokeEvaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)