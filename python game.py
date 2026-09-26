import random

score = 0

question = "What is the capital of Pakistan?"
answer = "Islamabad"
user_answer = input(question + "")
if user_answer.lower() == answer.lower():
    print("correct")
    score = score + 1
else:
    print("wrong")

question = "How many days are there in a weeks?"
answer = "7"
user_answer = input(question + "")
if user_answer.lower() == answer.lower():
    print("correct")
    score = score + 1
else:
    print("wrong")

question = "Which language are you learning?"
answer = "Python"
user_answer = input(question + "")
if user_answer.lower() == answer.lower():
    print("correct")
    score = score + 1
else:
    print("wrong")

question = "What is 5 + 5?"
answer = "10"
user_answer = input(question + "")
if user_answer.lower() == answer.lower():
    print("correct")
    score = score + 1
else:
    print("wrong")

question = "What color do you get by mixing red and blue?"
answer = "Purple"
user_answer = input(question + "")
if user_answer.lower() == answer.lower():
    print("correct")
    score = score + 1
else:
    print("wrong")
# final score
print("your score is", score, "out of 5")