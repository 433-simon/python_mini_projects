import random    #random is a built in module

# random.randrange(start,stop) syntax
top_of_range = input("Type a number till the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Please type a number larger than 0 next time")
        quit() 
else :
    print("Please type a number next time")
    quit()

random_number = random.randint(0 , top_of_range)

user_guess = int(input("Enter your guessing number : "))
if user_guess != random_number :
    print("Wrong Guessing!")
else :
    print("Right Guessing!")
print(f"Random number was : {random_number}")



