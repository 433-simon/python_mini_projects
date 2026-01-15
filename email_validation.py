email = input("Please enter your valid email address : ")
print(f"your email address : {email}")
if " " in email :
    print("Invalid because of spaces")
elif '@' not in email :
    print("Invalid : no @ found")
elif '.' not in email :
    print("Invalid : no . found")
elif email.startswith('@') or email.endswith('@') :
    print("Invalid : '@' at wrnog position")
elif email.count("@") != 1:
    print("Invalid: email must contain exactly one '@'")
elif email.index("@") > email.rindex("."):
    print("Invalid email: improper domain")
else :  
    print("Valid Email address")