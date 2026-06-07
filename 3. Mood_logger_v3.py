def input_data():
    data = []
    while True:
        name = input("Enter name :").strip().lower()
        if len(data) == 0:
            mood = input("Enter mood :").lower()
            if mood == "sad":
                print("I am here for you !")
            elif mood == "happy":
                print("Awesome ! Keep it up !")
        else:
            for entry in data:
                if entry["name"]  == name:
                    print("Last time your mood was",entry["mood"])
                    mood = input("How you feeling now :").strip().lower()
                    if entry["mood"] == mood and mood == "sad":
                        print("You seem sad lately, can we have a talk ?")
                    elif entry["mood"] == mood and mood == "happy":
                        print("You seem happy lately, thats great, enjoy your time")
                    else:
                        print("You seem differently since last time !")
                else:
                    mood = input("Enter mood :").lower()

        data.append({"name":name,"mood":mood})    

        while True:
            new = input("New data ? (Y/N) :").lower() 
            if new in ["y","n"]:
                break
            else:
                print("Invalid Choice !")

        if new == "n":
            break
        
    print(data)

input_data()
