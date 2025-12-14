print("Welcome to password strength checker🥳")
greet = input("Please enter your password : ")
print(f"Your entered password : {greet}")
# score = 0    
has_upper = False
has_lower = False
has_digit = False
has_char = False
strength = len(greet)
if strength == 8 :
    # score += 1  
    print("Length is perfect")
elif strength > 8 :
    print("Your length is too long")
else :
    print("Length is too short")
    
for ch in greet :
    if ch.isupper() == True :
        # score += 1
        has_upper = True 

    if ch.islower() == True :
        # score += 1
        has_lower = True
    
    if ch.isdigit() == True :
        # score += 1
        has_digit = True

    if ch.isalnum() == False :
        # score += 1
        has_char = True
print(f"Special character : {has_char} , Having digit :{has_digit} , Having lower character:{has_lower} , Having upper character: {has_upper} , The length :{strength}")

#Final score calculation
score = 0
if has_upper: score += 1
if has_lower: score += 1
if has_digit: score += 1
if has_char: score += 1
if strength >= 8: score += 1
if score == 5:
    print("Your password is strong🔥")
elif 3 <= score <= 4:
    print("Your password is medium🙌")
else:
    print("Your password is weak🤨")   

        
print("\nPassword Analysis:")
print(f"Uppercase   : {has_upper}")
print(f"Lowercase   : {has_lower}")
print(f"Digit       : {has_digit}")
print(f"Special char: {has_char}")
print(f"Length      : {strength}")

