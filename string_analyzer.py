user_string = input("Please Enter your string : ")
print(f"Your entered string is : {user_string}")
count_vowel=0
count_consonant = 0
freq = {}
#palindrome 
clean_string = user_string.replace(" ","").lower()
if clean_string == clean_string[::-1] :
    print("It's a palindrome")
else:
    print("Not a palindrome")
#vowel & consonant count
for i in user_string :
    if i.isalpha():
        if i in{'a','e','i','o','u'} :
            count_vowel+=1
        else :
            count_consonant+=1
print(f"Total vowels are : {count_vowel}")
print(f"Total consonants are : {count_consonant}")
# word count
print(f"The total words in the string is {len(user_string)}")
#character frequency
for u in user_string :
    if u in freq:
        freq[u] += 1
    else:
        freq[u] = 1

print(f"The character frequency is {freq}")