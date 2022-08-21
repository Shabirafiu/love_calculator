print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lowercase_string = combined_names.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

love = l + o + v + e


love_score = int(str(true) + str(love))

if (love_score < 10 ) or (love_score > 90) :
    print(f"YOUR LOVE SCORE IS {love_score},YOU ARE COMPARTABLE LIKE COKE AND MENTOS")
elif (love_score >= 40 ) and (love_score <= 50):
    print(f"YOUR LOVE SCORE IS {love_score}, YOU ARE ALRIGHT TOGETHER")
else:
    print(f"Your love score is {love_score}")


