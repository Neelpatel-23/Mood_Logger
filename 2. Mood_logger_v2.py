def input_data():
    data = []

    while True:
        name = input("Enter Name :").strip()
        mood = input("Enter Mood :").strip()

        if not name or not mood:
            print("Enter Valid Data !")
            continue

        data.append({"name":name,"mood":mood})

        while True:
            new = input("Want to add new data (Y/N) :")
            if new.lower() in ['y','n']:
                break
            print("Invalid Choice !")

        if new.lower() == "n":
            break

    return data

def show_data(data):
    print("----- Mood Log -----")
    for entry in data:
        print(f"{entry['name']} :- {entry['mood']}")

def summary(data):
    happy = sad = others = 0
    for entry in data:
       mood = entry['mood'].lower()
       if mood == "happy":
           happy += 1
       elif mood == "sad":
            sad += 1
       else:
            others += 1
    print("Happy :",happy)
    print("Sad :",sad)
    print("Others :",others)
    
info = input_data()
show_data(info)
summary(info)
