


username = ""


def start_game():
    global username
    print("Welcome to your very own interactive Paw Patrol Adventure Bay game.")
    username = input("Enter your name: ")
    place_chooser()




def place_chooser():
    choice = input(f"Hi {username}, choose where you would like to explore: Barkingburg, Foggy Bottom, or Katies Pet Parlor: ").lower()
    if choice == "barkingburg":
        barkingburg()
    elif choice == "foggy bottom":
        foggybottom()
    elif choice == "katies pet parlor":
        katies_pet_parlor()
    else:
        print("That isn't an option. Please pick from the three choices listed above.")
        place_chooser()




def katies_pet_parlor():
    print()
    print("Welcome to Katie's Pet Parlor! I am Ryder and I have chosen you to help me with this mission.\n"
        "Katie's cat has climbed onto the roof, and Skye isn't able to get her down.\n"
        "She says we have to answer 3 riddles of hers and then she will agree to coming down.\n"
        "For each question you have three tries to answer.\n"
        "We need your quick thinking on this mission. Please hurry!")
    katies_q1(3)




def katies_q1(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q1 = input("10 copycats were sitting in a car. One jumped out. How many are left? ").lower()
    if "zero" in q1 or "0" in q1 or "none" in q1:
        print("Hissssss, you got this question right, here is the next question: ")
        katies_q2(3)
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        katies_q1(attempts)




def katies_q2(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q2 = input("I'm found in socks, scarves, and mittens. I'm found in the paws of playful kittens. What am I? ").lower()
    if "yarn" in q2 or "wool" in q2:
        print("Oh no, you got it right again! I'm not coming down. Don't get this next one right!")
        katies_q3(3)
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        katies_q2(attempts)




def katies_q3(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q3 = input("How many lives does a cat have? ").lower()
    if "nine" in q3 or "9" in q3 or "nine lives" in q3 or "nine lives" in q3 or "9 lives" in q3:
        print(f"I am a cat of my word, sadly I will have to come down. Good job, I now declare you to be an honorary member of the Paw Patrol, {username}!")
        print("You have completed your mission.")
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        katies_q3(attempts)






def barkingburg():
   print()
   print("Welcome to barkingburg,  isn't it just stunning. \n Sadly, we aren't here for a pleasant trip, we are here for a mission. I ryder have chosen you because of your impressive skill sets, and your smarts. \n Someone has stolen the princesses tiara! It is your duty to find it for the princess. She is depending on you. \n This may seem like a daunting quest, but don't worry, we know where the crown is. This is because it has a secret location tracker hidden in one of the diamonds.")
   print("The tracker shows that she is in the vault room, which is an enclosed room. ")
   print()
   print ("The bad news is that the vault room is locked, and to open it you have to answer three very difficult riddles. \n You only have 3 tries per question, use them wisely. Once you do, the room will open.")
   print ("The riddle will be displayed on the vault door, by a projector. ")
   print("Let's go")
   print()
   print("You run to the vault room, huffing and puffing. You are nervous, but you are ready to the princess her crown back.")
   print()
   print("You see the question, and ryder tells you, 'here is your first question, on behalf of the Paw Patrol, I believe in you.'")
   barkingburg_q1(3)
  




#TODO complete barkingburg, questions, and wirte an ending message, and finish some of the story line, for guidance look at the document you made.


def barkingburg_q1(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q1 = input("What can be broken before it can be used").lower()
    if "egg" in q1 or "egg" in q1 or "egg" in q1 or "egg" in q1:
       print("Wow! You got this question right, read the next question: ")
       barkingburg_q2(3)
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        barkingburg_q1(attempts)




def barkingburg_q2(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q2 = input("What can run but can't walk?").lower()
    if "water" in q2 or "river" in q2 or "ocean" in q2:
        print ("Awesome, you got it right again! Only one more to go")
        barkingburg_q3(3)
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        barkingburg_q2(attempts)




def barkingburg_q3(attempts):
    if attempts == 0:
       print("You've run out of attempts! Let's try a different mission.")
       place_chooser()
       return
    q3 = input("You are worried because as you read the riddle, you hear a scary and menacing voice say, 'this riddle is the hardest of them all, you will never guess it. Mwhahahahaha' \n What goes up and down but never moves?").lower()
  
    if "stairs" in q3 or "staircase" in q3 or "steps" in q3:
       print(f"The vault door swings open, and reveals… sweetie, the princesses beloved dog. \n 'Sweetie?' Ryder asked curiously. 'What are you doing here!' You stand there utterly confused, but you manage to ask, 'Why did you steal the Princesses crown. In response sweetie lowers her head ashamed and says, 'I didn't want her to be a princess and I thought without her crown she couldn't be the princess.' \n Ryder says. ' Well, thanks to username here, we were able to stop you.' 'I admit', says sweetie, 'that was pretty impressive of you.'" )
       print()
       print(f"Ryder picks sweetie up, and passes you the crown to keep safe, and you proudly walk back to the princess, and return the crown to her. She is overjoyed, and praises you, while reprimanding sweetie. She whispers something to Ryder, and then ryder says, 'Good job username, you have completed your mission, and with the Princess of Barkingburg's blessing, I, pronounce you an official honorary member of the Paw Patrol!'")
       print()
       print(f"We are all so proud of you, and we thank you for your service!")


    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        barkingburg_q3(attempts)






def foggybottom():
    print( "Welcome to Foggy Bottom. Mayor Humdinger wants to take over Adventure Bay, " 
         "and what you need to do to stop him is to prevent his boat from picking him up so he can't cross into Adventure Bay.")
    print()   
    print("\nYou see Wally in the sea, and since Wally's owner is Cap'n Turbot who is steering the ship, he can tell him to stop the boats. "
         "\n Wally says he will only complete your request if you get im 3 squid pieces. You run to the nearest fish market to get Wally his treats but you realize you don't have any money on you."
         "\nSince the shop owner is kind, he offers to give you the squid if you answer 3 riddles with 3 tries for each riddle."
         "\nIf you get them correct, he will give you the squid!")
    foggy_q1(3)




def foggy_q1(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q1 = input("How do you make an octopus laugh?").lower()
    if "10" in q1 or "ten" in q1 or "tickles" in q1 or "tentacles" in q1:
        print("Wow! You got this question right, here is the next question: ")
        foggy_q2(3)
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        foggy_q1(attempts)


def foggy_q2(attempts):
    if attempts == 0:
       print("You've run out of attempts! Let's try a different mission.")
       place_chooser()
       return
    q2 = input("What has hands but cannot clap?").lower()
    if "clock" in q2 or "watch" in q2:
       print ("You got it right again!")
       foggy_q3(attempts)
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        foggy_q2(attempts)




def foggy_q3(attempts):
    if attempts == 0:
       print("You've run out of attempts! Let's try a different mission.")
       place_chooser()
       return
    q3 = input("What has keys, but can't open any doors? ").lower()
    if "piano" in q3 or "keyboard" in q3 or "grand" in q3:
       print(f"That's impressive! I really didn't think you would get. Here is the octopus leg. Go give it Wally quickly!")
       print("You run to give it wally, and he happily eats it, and swims to captain turbot.\n You wonder how you will know if wally tells captain turbot to turn the boat around, but then you see the boat turn around, and cruise of away from Foggybottom.")
       print("Ryder comes up to you and tells you, 'Good job, You have completed your mission we are all very proud of you. \n We now declare you an honorary member of the paw patrol.' ")
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of attempts! Let's try a different mission.")
            place_chooser()
            return
        print(f"Sorry, you got that wrong! You only have {attempts} more attempt(s) on this question!")
        foggy_q3(attempts)




start_game()



