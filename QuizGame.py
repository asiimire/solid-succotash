print("Welcome to my Computer quiz")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play:)")
score = 0  #this is going to allow us to keep track of how many correct answers we have
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1 #take the value of score and add one to it
else:
    print("incorrect")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")
answer = input("What does ROM stand for? ")
if answer.lower() == "Read Only Memory":
    print("correct")
    score += 1
else:
    print("incorrect")
answer = input("What does MAR stand for? ")
if answer.lower() == " memory address register":
    print("correct")
    score += 1
else:
    print("incorrect")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
print("You got " + str(score) + " Questions correct!") # we use str because score is an int not a str
print("You got " + str(score/5 * 100) + "%")





