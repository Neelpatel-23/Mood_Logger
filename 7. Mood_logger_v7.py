import json

def get_streak(data,name,mood):
    count = 0
    for record in reversed(data[name]):
        if record == mood:
            count += 1
        else:
            break
    return count

def get_response(name,data,mood):
    if name in data:
        last_mood = data[name][-1]

        streak = get_streak(data,name,last_mood)

        if mood == last_mood:
            streak += 1
        else:
            streak = 1
        
        if streak >= 3:
            if mood == "sad":
                print(f"You've been feeling sad for {streak} times. Want to talk?")
                return
            elif mood == "happy":
                print("You've been consistently happy ! That's great !")
                return
            elif mood == "angry":
                print("You've been very furious lately ! Please stay calm !")
                return
            elif mood == "stressed":
                print("You've been feeling stressed for long time ! I am worried about you !")
                return
            elif mood == "tired":
                print("You've been consistently tired ! You will fall ill !")
                return
                        
        if last_mood == mood:
            if mood == "sad":
                print("You seem sad lately. Can we have a talk ?")
            elif mood == "happy":
                    print("You seem happy lately. That's great. Enjoy your time.")
            elif mood == "angry":
                    print("You seem too angry lately. Try to meditate.")
            elif mood == "stressed":
                    print("You seem stressed lately. I suggest you to go hangout for few moments.")
            elif mood == "tired":
                    print("You seem too tired lately. Please go to sleep.")
            else: 
                print("Your mood is unchanged !")
        else:
                print("You seem different from last time !")

    else:
        if mood == "sad":
            print("I am here for you !")

        elif mood == "happy":
            print("Awesome ! Keep it up !")

        elif mood == "angry":
            print("Take a deep breath. Want to share what's bothering you ?")

        elif mood == "stressed":
            print("Seems like you're stressed. Try to relax a bit.")

        elif mood == "tired":
            print("You should get some rest.")

        else:
            print("Thanks for sharing how you feel.")

def input_data():
    try:
        with open("mood_data.json","r") as file:
            data = json.load(file)
            
    except FileNotFoundError:
        data = {}
    
    while True:
        while True:
            name = input("Enter name :").strip().lower()
            if name == "":
                print("Invalid Name !")
            else:
                break

        if name in data:
            print("Last time your mood was",data[name][-1])
            while True:
                mood = input("How you feeling now :").strip().lower()
                if mood == "":
                    print("Invalid Mood !")
                else:
                    break
        else:
            while True:
                mood = input("Enter mood :").strip().lower()
                if mood == "":
                    print("Invalid Mood !")
                else:
                    break

        get_response(name,data,mood)
        
        if name in data:
            data[name].append(mood)
        else:
            data[name] = [mood]

        while True:
            new = input("New data ? (Y/N) :").lower() 
            if new in ["y","n"]:
                break
            else:
                print("Invalid Choice !")

        if new == "n":
            break
        
    with open("mood_data.json","w") as file:
        json.dump(data,file,indent=4)

    print("\n--- Data Stored ---")
    for user,moods in data.items():
        print(user,"→",moods)

input_data()
