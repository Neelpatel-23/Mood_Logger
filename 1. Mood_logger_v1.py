def user_input():
    global data_dict
    data_dict = {}
    while True:
        name = input("Enter your name :")
        mood = input("Enter your mood :")
        data_dict.update({name:mood})
        add = input("Want to add new data (Y/N) :")
        if add.upper() == "N":
            break

def show_data():
    for key,value in data_dict.items():
        print("{",key,":",value,"}")

def summary():
    happy_count = sad_count = other_count = 0
    for key,value in data_dict.items():
        if value.lower() == "happy":
            happy_count += 1
        elif value.lower() == "sad":
            sad_count += 1
        else:
            other_count += 1
    print("Happy :",happy_count)
    print("Sad :",sad_count)
    print("Other :",other_count)

user_input()
show_data()
summary()
