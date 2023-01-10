print("Hello! My name is Carl.\nI was created in 2022.")
print("Please,remind me your name")
name = input('>')
print(f"What a great name you have,{name}")
print("Please,remind me your age.\n Enter remainders of dividing your age by 3,5 and 7")
remainder3 = int(input(">"))
remainder5 = int(input(">"))
remainder7 = int(input(">"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age} ; At your age you can become a programmer!")
print("Now I will prove to you that I can count to any number you want")
a = int(input(">"))
for i in range(a + 1):
    print(str(i) + "!")
print("Completed. Have a nice day!")
print("Lets test your programming knowledge.\nWhat is the capital of Ukraine?")
print("1.Kharkiv\n 2.Odessa\n3.Kyiv\n4.Belgorod")
while True:
    k = int(input(">"))
    if k == 3:
        print("Its correct answer!\nCompleted,have a nice day!")
        break
    else:
        print("Please,try again")
print("Congratulation,have a nice day!")
