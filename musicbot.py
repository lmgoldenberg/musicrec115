import os.path
def readPreferences():
    preferences={}
    if (os.path.isfile("musicrecplus.txt")):
        with open("musicrecplus.txt") as f:
            for line in f:
                [username, singers] = line.strip().split(':')
                singerList=singers.split(',')
                preferences[username]=singerList
    else:
                f=open("musicrecplus.txt","w")
                f.close
    return preferences
def ask_name():
    user_and_prefs=readPreferences()
    name = input("Name?\n")
    if name in user_and_prefs:
        menu(name,user_and_prefs)
    else:
        get_preferences(name,user_and_prefs)
        
def get_preferences(name,preferences):
    new_user_prefs = []
    new_preference = input("Preferences?")
    while new_preference != "":
        new_preference = new_preference.strip().title()
        #add new preference to new_user_prefs
        new_user_prefs = new_user_prefs + [new_preference]
        new_preference = input("Preferences?")
    preferences[name] = sorted(new_user_prefs)
    print(preferences[name])
    menu(name,preferences)

def menu(name,preferences):
    user_input=input("Enter a letter to choose an option:\n e - Enter preferences\n r - Get recommendations\n p - Show most popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n q - Save and quit\n")
    while True:
        if user_input == 'e':
            get_preferences(name,preferences)
        if user_input == 'r':
            recommendations(name,preferences)
        if user_input == 'p':
            popularArtists(name, preferences)
        if user_input == 'h':
            howPopular(name,preferences)
        if user_input == 'm':
            mostLikes(name, preferences)
        if user_input == 'q':
            save_quit(name, preferences)
            break
        if user_input not in['e', 'r', 'p', 'h', 'm', 'q']:
            user_input=input("Enter a letter to choose an option:\n e - Enter preferences\n r - Get recommendations\n p - Show most popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n q - Save and quit\n")
def howPopular(name, preferences):
    singers = []
    seen = {}
    for users in preferences:
        singers = singers + preferences[users]
    for item in singers:
        if item in seen:
            seen[item]+=1
        else: seen[item] = 1
    for item in singers:
        out = 0
        if seen[item] > out:
            out = seen[item]
    print(out)
    menu(name,preferences)
def numMatches(u1, u2):
    """returns the number of matches of two artists in lists
    Author: Ella"""
    count = 0
    for i in u1:
        if i in u2:
            count += 1
    return count
def bestUserMatch(prefs, allPrefs):
    """Given a list of preferences and a list of lists of preferences,
    returns the one with the most matches
    Author:Ella"""
    if prefs == [] or allPrefs == []:
        print("No recommendations available at this time.")
        return
    maxMatches = 0
    bestIndex = 0
    for i in range(len(allPrefs)):
        currentMatches = numMatches(prefs, allPrefs[i])
        if currentMatches > maxMatches:
            bestIndex = i
            maxMatches = currentMatches
    if maxMatches == 0:
        print("No recommendations available at this time.")
        return
    else:
        count = 0
        for i in allPrefs[bestIndex]:
            if i not in prefs:
                count+=1
                print(i)
        else:
            if count == 0:
                del(allPrefs[bestIndex])
                bestUserMatch(prefs,allPrefs)
def recommendations(name,preferences):
    """Returns user recommendations
    Author:Ella"""
    allPreferences = []
    for i in preferences:
        allPreferences.append(preferences[i])
    bestUserMatch(preferences[name], allPreferences)
    menu(name,preferences)
def popularArtists(name, preferences):
    """Does not take an input. Returns the most popular artists
    Author: Keyaan"""

    artist_counts = {}

    for user, user_prefs in preferences.items():
        if user_prefs and '$' not in user_prefs:
            for artist in user_prefs:
                artist_counts[artist] = artist_counts.get(artist, 0) + 1
    if not artist_counts:
        print("Sorry, no artists found.")
        return
    sorted_artists = sorted(artist_counts.items(), key=lambda x: x[1], reverse=True)
   
    top_artists = sorted_artists[:3]
   
    if top_artists:
        print("The most popular artist(s) is/are:")
       
        for artist, count in top_artists:
            print(artist)
    else:
        print("Sorry, no artists found.")

    menu(name,preferences)
def mostLikes(name, preferences):
    """Does not take an input. Returns the user with the most
    amount of liked artists
    Author:Keyaan"""
    non_private_users = {user: prefs for user, prefs in users.items() if not (prefs and prefs[-1] == '$')}

    if not non_private_users:
        print("Sorry, no user found.")
        return

    max_likes_users = [user for user in non_private_users if len(non_private_users[user]) == max(map(len, non_private_users.values()))]

    print("The user(s) with the most likes is/are:")
    print("\n".join(sorted(max_likes_users)) if max_likes_users else "Sorry, no user found.")
    menu(name,preferences)
def save_quit(name, preferences):
    f=open("musicrecplus.txt","w")
    for item in preferences:
        newstr = str(preferences[item]).replace("[",":")
        newerstr = newstr.replace("]","")
        newererstr = newerstr.replace(", ",",")
        newerererstr = newererstr.replace("'","")
        print(item+newerererstr)
        f.write(item+newerererstr+"\n")
    f.close()
    quit()
ask_name()
