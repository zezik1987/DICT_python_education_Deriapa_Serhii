import random
friends = {}
name_input = None
number = 0
try:
    number = int(input("Enter the number of friends joining (including you):\n >"))
except ValueError:
    exit("No one is joining for the party")
if number <= 0:
    exit("No one is joining for the party")

for key in range(int(number)):
    name_input = input("Enter the name of every friend (including you),each on a new line:\n >")
    friends.setdefault(name_input, 0)

total_amount = int(input("Enter the total amount:\n >"))
friends_lucky = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: \n>")
try:
    if friends_lucky == "yes":
        name_lucky = random.choice(list(friends.keys()))
        print(name_lucky, "is the lucky one!")
        number -= 1
        for values in friends:
            amount = total_amount / number
            friends[values] = round(amount, 2)
        friends[name_lucky] = 0
    elif friends_lucky == "no" or friends_lucky != "no":
            print("\nNo one is going to be lucky")
            for values in friends:
                amount = total_amount / number
                friends[values] = round(amount, 2)
except ValueError:
    print(friends)
print(friends)
