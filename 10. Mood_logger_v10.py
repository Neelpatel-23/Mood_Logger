import json
from datetime import datetime
import matplotlib.pyplot as plt

emotion_score = {
    "excited":3,
    "happy":2,
    "grateful":2,
    "calm":1,
    "relaxed":1,
    
    "okay":0,
    "fine":0,
    "alright":0,
    
    "tired":-1,
    "sad":-2,
    "angry":-2,
    "stressed":-2,
    "anxious":-2
    }

response_messages = {
    "sad":"I am here for you !",
    "happy":"Awesome ! Keep it up !",
    "angry":"Take a deep breath. Want to share what's bothering you ?",
    "stressed":"Seems like you're stressed. Try to relax a bit.",
    "tired":"You should get some rest.",
    }

same_mood_messages = {
    "sad":"You seem sad lately. Can we have a talk ?",
    "happy":"You seem happy lately. That's great. Enjoy your time.",
    "angry":"You seem too angry lately. Try to meditate.",
    "stressed":"You seem stressed lately. I suggest you to go hang out for few moments.",
    "tired":"You seem too tired lately. Please go to sleep.",
    }

streak_messages = {
    "sad":"You've been feeling sad for {} times. Want to talk?",
    "happy":"You've been consistently happy ! That's great !",
    "angry":"You've been very furious lately ! Please stay calm !",
    "stressed":"You've been feeling stressed for a long time ! I am worried about you !",
    "tired":"You've been consistently tired ! You will fall ill !",
    }

def normalize_mood(mood):
    mood = mood.lower().strip().split()

    for word in mood:
        if word in emotion_score:
            return word
    return "unknown"

def calculate_score(moods):
    total = 0
    for mood in moods:
        total += emotion_score.get(mood,0)
    return total

def analyze_user(name,data):
    moods = []
    for record in data[name]:
        moods.append(record["mood"])
    total = calculate_score(moods)
    avg = total / len(moods)

    print(f"\n--- Emotional Insight Of {name.capitalize()} ---")

    if avg >= 1:
        print("You are generally feeling positive. Keep it up !")
    elif avg <= -1:
        print("You've been emotionally low lately. Take care of yourself.")
    else:
        print("Your emotions seem balanced.")

    print("Average Mood Score :",round(avg,2))

    most_common = max(set(moods), key = moods.count)
    print("Most Frequent Mood :",most_common.capitalize())
    
def get_streak(data,name,mood):
    count = 0
    for record in reversed(data[name]):
        if record["mood"] == mood:
            count += 1
        else:
            break
    return count

def get_response(name,data,mood):
    if name in data:
        last_mood = data[name][-1]["mood"]

        streak = get_streak(data,name,last_mood)

        if mood == last_mood:
            streak += 1
        else:
            streak = 1
        
        if streak >= 3 and mood in streak_messages:
            if "{}" in streak_messages[mood]:
                print(streak_messages[mood].format(streak))
            else:
                print(streak_messages[mood])
            return
        
        if last_mood == mood:
            if mood in same_mood_messages:
                print(same_mood_messages[mood])
            else: 
                print("Your mood is unchanged !")
        else:
                print("You seem different from last time !")

    else:
        if mood in response_messages:
            print(response_messages[mood])
        else:
            print("Thanks for sharing how you feel.")

def dashboard(name,data):

    moods = []
    for record in data[name]:
        moods.append(record["mood"])

    freq = {}
    for mood in moods:
        freq[mood] = freq.get(mood,0) + 1

    positive = ["excited","happy","grateful","calm","relaxed"]
    neutral = ["okay","fine","alright"]
    negative = ["sad","angry","stressed","anxious","tired"]

    positive_count = neutral_count = negative_count  = 0

    for mood in moods:
        if mood in positive:
            positive_count += 1
        elif mood in neutral:
            neutral_count += 1
        elif mood in negative:
            negative_count += 1

    total_entries = len(moods)

    positive_percentage = round(positive_count / total_entries * 100,2)
    neutral_percentage = round(neutral_count / total_entries * 100,2)
    negative_percentage = round(negative_count / total_entries * 100,2)

    latest_record = data[name][-1]

    print(f"\n--- Dashboard of {name.capitalize()} ---")
    
    print("Total Entries :",total_entries)

    print("Positive :",positive_count)
    print("Neutral :",neutral_count)
    print("Negative :",negative_count)

    print("Positive Percentage :",positive_percentage)
    print("Neutral Percentage :",neutral_percentage)
    print("Negative Percentage :",negative_percentage)

    print("Latest Mood :",latest_record["mood"].capitalize())
    print("Time :",latest_record["time"])

    print("\nMood Frequency")
    for mood, count in freq.items():
        print(mood.capitalize(), ":", count)

    colors = []
    for mood in freq.keys():
        if mood in positive:
            colors.append("green")
        elif mood in neutral:
            colors.append("blue")
        elif mood in negative:
            colors.append("red")
        else:
            colors.append("gray")
    
    plt.bar([mood.capitalize() for mood in freq.keys()], freq.values(), color = colors)
    plt.title(f"Mood Frequency - {name.capitalize()}")
    plt.xlabel("Moods →")
    plt.ylabel("Count →")
    plt.yticks(range(0,max(freq.values()) + 5))
    plt.show()

    sizes = []
    labels = []
    pie_colors = []
    
    if positive_count > 0:
        sizes.append(positive_count)
        labels.append("Positive")
        pie_colors.append("green")
    if neutral_count > 0:
        sizes.append(neutral_count)
        labels.append("Neutral")
        pie_colors.append("blue")
    if negative_count > 0:
        sizes.append(negative_count)
        labels.append("Negative")
        pie_colors.append("red")
    plt.pie(sizes,labels = labels, colors = pie_colors, autopct = "%1.1f%%")
    plt.title(f"Emotion Distribution - {name.capitalize()}")
    plt.show()
    
def input_output():
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
            print("Last time your mood was",data[name][-1]["mood"])
            while True:
                mood = normalize_mood(input("How you feeling now :"))
                if mood == "":
                    print("Invalid Mood !")
                else:
                    break
        else:
            while True:
                mood = normalize_mood(input("Enter mood :"))
                if mood == "":
                    print("Invalid Mood !")
                else:
                    break

        get_response(name,data,mood)

        record = {
            "mood":mood,
            "time":datetime.now().strftime("%d %b %Y | %I:%M %p")
            }
        
        if name in data:
            data[name].append(record)
        else:
            data[name] = [record]

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
    for user,records in data.items():
        print(f"\n{user.capitalize()}")
        for record in records:
            print(record["mood"].capitalize(),"→",record["time"])

    for user in data:
        analyze_user(user, data)
        dashboard(user, data)

input_output()
