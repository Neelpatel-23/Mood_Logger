import json

def get_response(name,data,mood):
    if name in data:
        last_mood = data[name][-1]

        
        if len(data[name]) >= 2:
            if data[name][-1] ==  "sad" and data[name][-2] == "sad" and mood == "sad":
                print("You've been sad for a while. Want to talk?")
                return
            
        if last_mood == mood and mood == "sad":
                print("You seem sad lately, can we have a talk ?")
        elif last_mood == mood and mood == "happy":
                print("You seem happy lately, thats great, enjoy your time")
        elif last_mood == mood:
            print("Your mood is unchanged !")
        else:
                print("You seem different from last time !")

    else:
        if mood == "sad":
            print("I am here for you !")

        elif mood == "happy":
            print("Awesome ! Keep it up !")


def input_data():
    try:
        with open("mood_data.json","r") as file:
            data = json.load(file)
            
    except FileNotFoundError:
        data = {}
    
    while True:
        name = input("Enter name :").strip().lower()

        if name in data:
            print("Last time your mood was",data[name][-1])
            mood = input("How you feeling now :").strip().lower()
        else:
            mood = input("Enter mood :").strip().lower()

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
    
