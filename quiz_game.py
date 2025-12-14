print("Welcome user to my game!")
playing = input("Would you like to play game ? ")
if playing.lower() == "no" :
    print("Game Ended!")  
else :
    print("Congratulations! You have entered the quiz 🎊")
ques = input("Ready for ques 1st : ")
if ques.lower() == "yes" :
    print("Let's start :) ")
    
score = 0

answer = input("What does CPU stands for ? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score += 1  
else :
    print("Incorrect :( ")

answer_2 = input("Who is t he brain of Computer ? ")
if answer_2.lower() == "cpu" :
    print("Correct!")
    score += 1
else :
    print("Incorrect :( ")

answer_3 = input("Who invented computer ? ")
if answer_3.lower() == "charles babbage" :
    print("Correct!")
    score += 1
else :
    print("Incorrect :( ")

answer_4 = input("What does GPU stands for ? ")
if answer_4.lower() == "graphics processing unit" :
    print("Correct!")
    score += 1
else :
    print("Incorrect :( ")

answer_5 = input("What does RAM stands for ? ")
if answer_5.lower() == "random access memory" :
    print("Correct!")
    score += 1
else :
    print("Incorrect :( ")

answer_6 = input("What does PSU stands for ? ")
if answer_6.lower() == "power supply unit" :
    print("Correct!")
    score += 1
else :
    print("Incorrect :( ")

answer_7 = input("What does GUI stands for ? ")
if answer_7.lower() == "graphics user interface" :
    print("Correct!")
    score += 1
else :
    print("Incorrect :( ")

answer_8 = input("What does CLI stands for ? ")
if answer_8.lower() == "command line interface" :
    print("Correct!")
    score += 1
else :
    print("Incorrect :( ")

answer_9 = input("What does ROM stands for ? ")
if answer_9.lower() == "read only memory" :
    print("Correct!")
    score += 1
else :
    print("Incorrect :( ")

answer_10 = input("What does CD stands for ? ")
if answer_10.lower() == "compact disk" :
    print("Correct!")   
    score += 1
else :  
    print("Incorrect :( ")
print("Hurray you have finished the quiz🎊")
final = input("Want to see your score 👀 ?")
if final.lower() == "yes" :
    print(score)

print(f"Your final score is {score}. Thank you for Playing")
