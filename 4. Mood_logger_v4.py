def input_data():
    data = {}
    
    while True:
        name = input("Enter name :").strip().lower()

        if name not in data:
            mood = input("Enter mood :").lower()

            if mood == "sad":
                print("I am here for you !")

            elif mood == "happy":
                print("Awesome ! Keep it up !")

        else:
            print("Last time your mood was",data[name][-1])
            mood = input("How you feeling now :").strip().lower()

            if data[name][-1] == mood and mood == "sad":
                    print("You seem sad lately, can we have a talk ?")
            elif data[name][-1] == mood and mood == "happy":
                    print("You seem happy lately, thats great, enjoy your time")
            elif data[name][-1] == mood:
                print("Your mood is unchanged !")
            else:
                    print("You seem different from last time !")

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
        
    for user,moods in data.items():
        print(user,"→",moods)

input_data()
