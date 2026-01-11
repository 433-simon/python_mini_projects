print("Welcome to Number Analyzer!")
number = int(input("Enter your number : "))
print(f"your number is : {number}")

#Prime Number:
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2,number):
        if number % i == 0 :
            is_prime= False
            break
if is_prime :
    print("It's a Prime Number")
else:
    print("It's not a prime Number")

# ArmStrong Number
temp = number
rev = 0
digits = len(str(number))

while temp > 0:
    digit = temp % 10
    rev += digit ** digits
    temp //= 10

# print(rev)
if number == rev :
    print("It's an Armstrong Number")
else :
    print("It's not an Armstrong Number")

#palindrome
reve = 0
num = number
digit = 0
while num > 0:
    digit = num%10 
    num = num//10
    reve = reve * 10 + digit
    # print(reve)
if number == reve :
    print("It's a palindrome")
else :
    print("It's not a palindrome")

#sum of digits 
numb = number
sum = 0
digit = 0
while numb > 0:
     digit = numb%10
     numb = numb//10
     sum = digit+sum
# print(sum)
print(f"Sum of digits are : {sum}")

# Number of digits
num_str = number
count= str(num_str)
print(f"The total number of digits are : {len(count)}")