import time
print("This is a quiz! Take it seriously or else you will be punished!(Movie Edition)")
playing = input("Are you ready to play it? ")
score = 0
if playing.lower() != "yes":
    quit()
else:
    for i in range (1,4):
        print(i)
        time.sleep(1)
    print("Let's go!")
answer = input("What year did Interstellar come out? ")
if answer.lower() == "2014":
    print("Correct!")
    score +=1
else:
    print("Incorrect")
   
answer = input("Who is the director of The Wolf of Wallstreet? ")
if answer.lower() == "martin scorsese":
    print("Correct!")
    score +=1
else:
    print("Incorrect")
answer = input("How many years did Boyhood take to film? ")
if answer == "12":
    print("Correct!")
    score +=1
else:
    print("Incorrect")
answer = input("Who has recently won best supportin actor at the Oscars'? ")
if answer.lower() == "sean penn":
    print("Correct!")
    score +=1
else:
    print("Incorrect")
answer = input("What is the most critically acclaimed movie of all time?")
if answer.lower() == "citizen kane":
    print("Correct")
    score +=1
else:
    print("Incorrect")
if score<=1:
   print("You're a poser! Stop watching tiktok movies and dive into real cinema! " + str((score/5)*100)+ "%")
elif score>1 and score<=3:
    print("You're getting there! Try watching more japanese movies! " + str((score/5)*100)+ "%")
else:
   print("You're a true cinephile! Here, a gold star for you: ⭐! " + str((score/5)*100)+ "%")
