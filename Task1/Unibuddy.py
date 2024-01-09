'''---Psuedo Code---
1. Get user info: Name, Age, Faculty, Degree Subject
2. Print Customised message for user based on above info
3. Offer options for more info , direct to resources.
'''
faculties  = ['Science', 'Arts','Modern Languages', 'History']
subjects = {"Science": ["Chemistry", "Physics", "Biology","Engineering", "Medicine"],
            "Arts":["Drawing","Sculpture","Theatre"],
            "Modern Languages": ["French, Spanish, German, Mandarin, Russian"],
            "History":["Ancient History", "Modern History"]}

print('''Welcome to UniBuddy, I am a chat bot designed to help orientate you in your early stages here.
      First, I'm going to gather some of your info so I can assist you''')



while True:
    try:
        user_name = str(input("Please enter your name: ")).capitalize()
        user_age = int(input("Please enter your name in years: "))

        print(f"Hi {user_name}! It's nice to meet you")

        if user_age <= 18:
              print(f"That's very young to be starting Univeristy {user_name}, congratulations!")
        elif user_age >25:
              print("It's nice to welcome a more mature student")
        break     
    except ValueError:
        print("Your age wasn't recognised. Please try again")

print("Our faculties currently supported by Unibuddy are: ")
print(faculties)


while True:
    user_faculty = str(input("Please enter your university faculty: "))

    if user_faculty == 'Science':
            print(f"For the {user_faculty} faculty, the subjects we currently offer are: {subjects["Science"]}")
            break
    elif user_faculty == 'Arts':
            print(f"For the {user_faculty} faculty, the subjects we currently offer are: {subjects["Arts"]}")
            break
    elif user_faculty == 'Modern Languages':
            print(f"For the {user_faculty} faculty, the subjects we currently offer are: {subjects["Modern Languages"]}")
            break
    elif user_faculty == 'History':
            print(f"For the {user_faculty} faculty, the subjects we currently offer are: {subjects["History"]}")
            break
    else: 
        print("The faculty you entered is not recognised, please enter a supported faculty")
    

user_subject = str(input("Please enter the subject you are studying: "))

