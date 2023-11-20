"""
Names: Ella Warnock, Keyaan Gala, Lewis Goldenberg
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 Group Project
"""

import os.path
def readPreferences():
    """Does not take an input. Reads the musicrecplus.txt file and creates it if doesn't exist.
    If it does exist it will then take any existing data in the musicrecplus.txt file and
    convert it into a dictionary called preferences.
    Author:Ella"""
    preferences={}
    if (os.path.isfile("musicrecplus.txt")):
        with open("musicrecplus.txt") as f:
            for line in f:
                [username, singers] = line.strip().split(':')
                singerList=singers.split(',')
                for i in range(len(singerList)):
                    singerList[i] = singerList[i].title()
                preferences[username]=singerList
    else:
                f=open("musicrecplus.txt","w")
                f.close
    return preferences
def ask_name():
    """Takes no inputs. Gives greeting and prompts user to enter their name
    Author:Ella"""
    user_and_prefs=readPreferences()
    name = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ):")
    if name in user_and_prefs:
        menu(name,user_and_prefs)
    else:
        get_preferences(name,user_and_prefs)
def get_preferences(name,preferences):
    """Takes in an artist that user likes. Stores all artists in global list artistsList
    Author:Ella"""
    new_user_prefs = []
    new_preference = input("Enter an artist that you like ( Enter to finish ): ")
    while new_preference != "":
        new_preference = new_preference.strip().title()
        #add new preference to new_user_prefs
        new_user_prefs = new_user_prefs + [new_preference]
        new_preference = input("Enter an artist that you like ( Enter to finish ): ")
    preferences[name] = sorted(new_user_prefs)
    menu(name,preferences)

def menu(name,preferences):
    """Displays options for the user.Once user inputs desired option
    it runs the function associated with the input.
    Once that function is completed, runs in a while loop till save
    and quit option is input
    Author:Lewis"""
    private_preferences = private(name,preferences)
    user_input=input("Enter a letter to choose an option :\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\ns - Show preferences\nq - Save and quit\n")
    while True:
        if user_input == 'e':
            get_preferences(name,preferences)
        if user_input == 'r':
            recommendations(name,private_preferences,preferences)
        if user_input == 'p':
            popularArtists(name,private_preferences, preferences)
        if user_input == 'h':
            howPopular(name,private_preferences, preferences)
        if user_input == 'm':
            mostLikes(name, private_preferences, preferences)
        if user_input == 's':
            show_preferences(name,preferences)
        if user_input == 'q':
            save_quit(name, preferences)
        if user_input not in['e', 'r', 'p', 'h', 'm', 's', 'q']:
            user_input=input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\ns - Show preferences\nq - Save and quit\n")
def howPopular(name, preferences, full_preferences):
    """Does not take an input. Returns how popular the most
    popular artist is using how many recommendations it has been given
    Author:Lewis"""
    singers = []
    seen = {}
    for users in preferences:
        singers = singers + preferences[users]
    for item in singers:
        if item in seen:
            seen[item]+=1
        else: seen[item] = 1
    out = 0
    for item in singers:
        if seen[item] > out:
            out = seen[item]
    if out <= 0:
        print("Sorry , no artists found .")
    else:
        print(out)
    menu(name,full_preferences)
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
        print("No recommendations available at this time .")
        return
    maxMatches = 0
    bestIndex = 0
    for i in range(len(allPrefs)):
        currentMatches = numMatches(prefs, allPrefs[i])
        if currentMatches > maxMatches:
            bestIndex = i
            maxMatches = currentMatches
    if maxMatches == 0:
        print("No recommendations available at this time .")
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
def recommendations(name,preferences,full_preferences):
    """Returns user recommendations
    Author:Ella"""
    allPreferences = []
    for i in preferences:
        allPreferences.append(preferences[i])
    bestUserMatch(full_preferences[name], allPreferences)
    menu(name,full_preferences)
def popularArtists(name, preferences,full_preferences):
    """Does not take an input. Returns the most popular artists
    Author: Keyaan"""

    artist_counts = {}

    for user, user_prefs in preferences.items():
        if user_prefs and '$' not in user_prefs:
            for artist in user_prefs:
                artist_counts[artist] = artist_counts.get(artist, 0) + 1
    if not artist_counts:
        print("Sorry , no artists found .")
        menu(name,full_preferences)
    sorted_artists = sorted(artist_counts.items(), key=lambda x: x[1], reverse=True)
   
    top_artists = sorted_artists[:3]
   
    if top_artists:
        #print("The most popular artist(s) is/are:")
       
        for artist, count in top_artists:
            print(artist)
    else:
        print("Sorry , no artists found .")

    menu(name,full_preferences)
def mostLikes(name, preferences,full_preferences):
    """Does not take an input. Returns the user with the most
    amount of liked artists
    Author: Keyaan"""

    non_private_users = {user: prefs for user, prefs in preferences.items() if not (prefs and prefs[-1] == '$')}

    if not non_private_users:
        print("Sorry , no user found .")
        menu(name,full_preferences)

    max_likes_users = [user for user in non_private_users if len(non_private_users[user]) == max(map(len, non_private_users.values()))]

    #print("The user(s) with the most likes is/are:")
    print("\n".join(sorted(max_likes_users)) if max_likes_users else "Sorry, no user found.")

    menu(name, preferences)
def save_quit(name, preferences):
    """Does not take an input. Saves the users preferences to a .txt file.
    Author:Lewis"""
    f=open("musicrecplus.txt","w")
    for item in preferences:
        newstr = str(preferences[item]).replace("[",":")
        newerstr = newstr.replace("]","")
        newererstr = newerstr.replace(", ",",")
        newerererstr = newererstr.replace("'","")
        f.write(item+newerererstr+"\n")
    f.close()
    quit()
def show_preferences(name,preferences):
    """EXTRA CREDIT: Does not take an input. Shows the user their own preferences.
    Author: Lewis"""
    print(preferences[name])
    menu(name, preferences)
def private(name, preferences):
    """Does not take an input. Takes the data created from preferences (which contains names and singers those names like),
    and creates a new dictionary to be used in the other functions where private names(ones that end in $) are excluded.
    Author:Lewis"""
    private_preferences = {}
    for item in preferences:
        if item[-1] != "$":
            private_preferences[item] = preferences[item]
    return private_preferences
ask_name()
