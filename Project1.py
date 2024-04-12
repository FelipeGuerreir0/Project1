score = 0

Start_play = input("Do you wanna play? ")

if Start_play.lower() != "yes" :
    quit()

print("Ok, let's start")



answer = input("which super-hero is from marvel, Batman or Spiderman? ") .lower()

if answer == "spiderman":
    print("you're correct!")
    score += 1
    print("now u have " + str(score) + (" points"))
else:
    print("that's sounds wrong!")

answer = input("which super-hero wears green, green lantern or Hulk? ") .lower()

if answer == "green lantern":
    print("you're correct!")
    score += 1
    print("now u have " + str(score) + (" points"))
else:
    print("that's sounds wrong!")

answer = input("which super-hero wears an armor, Iron Man or Superman? ") .lower()

if answer == "iron man":
    print("you're correct!")
    score += 1
    print("now u have " + str(score) + (" points"))
else:
    print("that's sounds wrong!")

text = "the game ends, but your score is "
print (text + str(score))
    