types_of_people = 10

# Here we put value string the value
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"

# Here we put value string the value
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)

# Here we put value string the value
print(f"I said: {x}")
# Here we put value string the value
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
