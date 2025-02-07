""" x = 3
y = float(3)
print(x,y) """

values = [1,2.23,5,7,2,30,15]
""" print(values)
for i in values:
    print(i) """

""" print(values[0])
print(values[6]) """

"test"
["t","e","s","t"]

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

#Challenge When you use input(), the program stops and asks you to type something in. Once you type something and press Enter, it stores what you typed as a string (a piece of text).
#Madlibs Project

""" sentence = input("enter a sentence:")
words = sentence.split()
count = len(words)
print(count) """

#Madlib Project:
""" a = input("enter verb1:")
b = input("enter verb2:")
c = input("enter noun1:")
d = input("enter noun2:")
e = input("enter a number:")
f = input("enter a celebrity:")
g = input("enter noun3:")

Madlib = print(f"As {c} was {a} to {d}, he saw {f}, {b} at {g} and asked to them to pick a number and {f} picked {e}, afterwards they went their own separate way")
print(Madlib) """

#Challenge 2:

number = input("Enter a Number:")

#Notes:
""" def login(password):
    #if state evaluates to true do next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect password")
login("secret") """

def temp(x)
    if x >=80:
        print("too hot")
    elif x > 60:
        print("nice")
    else:
        print("too cold")
x = int(input("what da temp"))
temp(x)
