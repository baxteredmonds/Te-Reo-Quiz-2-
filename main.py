#06/27/2022
#v26
#Baxter Edmonds
#learning
#import the random libray
import random
#globlals and question list 
score = 0
english = ["horse","friend","amazing","future","green"]
right_answer =["hoiho","hoa","Miharo","tau koroī","karera"]
option_1 =["tane","pukukai","moko","poharu","karaehe "]
option_2 =["aroha","titiro","tipuna","pōmu","oumu"]      

#define a function to generate a question 
def generate_question(english,right_answer,option_1,option_2):
  global score 
  print ("what is the correct word for",english,"in maori")
  #generate a random number to determine the sequence of questions
  random_sequence = random.randint(0,4)
  #separate print statements for readability
  if (random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C",right_answer)
    answer = input().lower()
    if answer == "c":
      print("correct!")
      score += 1 
    
    else:
      print("incorrect")
  
  if (random_sequence == 1):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      print("correct!")
      score += 1 
    else:
      print("incorrect")
  
  if (random_sequence == 2):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      print("correct")
      score += 1 
    else:
      print("incorrect")

  if (random_sequence == 3):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      print("correct")
      score += 1 
    else:
      print("incorrect")

  if (random_sequence == 4):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      print("correct")
      score += 1 
    else:
      print("incorrect")
    #generate 3 questions pulling possible answers from list.
for i in range (0,5):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])
    
  #print the score at the end of the quiz
print(score)