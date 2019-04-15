#!/usr/bin/python3.5

import webbrowser
import time
import sys
import os
import subprocess



browsers = input("What browser do you prefer to use? Choose 1 if Firefox or 2 to use Chrome: ")

id = browsers

def browser_open(url, id):
    if sys.platform.startswith('win32') and browsers =="2":
        chrome = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" or "%PROGRAMFILES%\Google\Chrome\Application/chrome.exe %s" or "%PROGRAMFILES(X86)%\Google\Chrome\Application\chrome.exe %s")
        chrome.open_new_tab(url)
    elif sys.platform.startswith('win32') and browsers =="1":
        firefox = webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe %s" or "C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s")
        firefox.open_new_tab(url)
    elif sys.platform.startswith('linux') and browsers == "1":
        #firefox = subprocess.run("firefox")
        firefox = webbrowser.get("firefox")
        firefox.open_new_tab(url)
    elif sys.platform.startswith('linux') and browsers =="2":
        #chrome = subprocess.run("google-chrome")
        chrome = webbrowser.get("google-chrome")
        chrome.open_new_tab(url)




module = input("Enter module num: \n ------------- \n 1 - Target Profile(Facebook) \n 2 - Multiple Target Profiles(Facebook) \n 3 - Detailed search(Facebook) \n 4 - Twitter Module \n ------------- \n ")
if module == "1":
    fbid = input("Enter FB user ID: ")
    num = input("Enter payload: \n [1] - places-visited, [2] - recent-places-visited, [3] - places-checked-in, [4] - places-liked, [5] - pages-liked, \n [6] - photos-by, [7] - photos-liked, [8] - photos-of, [9] - photos-commented, [10] - apps-used, \n [11] - videos, [12] - videos-of, [13] - videos-by, [14] - videos-liked, [15] - videos-commented, \n [16] - events, [17] - events-joined, [18] - stories-by, [19] - stories-commented, [20] - stories-tagged, [21] - groups, \n [22] - employees, [23] - friends, [24] - relatives, [25] - friends/pages-liked, \n OR [0] - search all \n" )
    def userinput(fbid,num):
        if fbid != 0 or len(fbid) > 0:
            print("Well done! We started to work for you :)")
        elif len(fbid) == 0:
            print("You need to enter something!")
            print("Payload set :)")
        elif len(num) == 0:
            print("payload failed!")
        if num == "1":
            payload = "/places-visited"
        elif num == "2":
            payload = "/recent-places-visited"
        elif num == "3":
            payload = "/places-checked-in"
        elif num == "4":
            payload = "/places-liked"
        elif num == "5":
            payload = "/pages-liked"
        elif num == "6":
            payload = "/photos-by"
        elif num == "7":
            payload = "/photos-liked"
        elif num == "8":
            payload = "/photos-of"
        elif num == "9":
            payload = "/photos-commented"
        elif num == "10":
            payload = "/apps-used"
        elif num == "11":
            payload = "/videos"
        elif num == "12":
            payload = "/videos-of"
        elif num == "13":
            payload = "/videos-by"
        elif num == "14":
            payload = "/videos-liked"
        elif num == "15":
            payload = "/videos-commented"
        elif num == "16":
            payload = "/events"
        elif num == "17":
            payload = "/events-joined"
        elif num == "18":
            payload = "/stories-by"
        elif num == "19":
            payload = "/stories-commented"
        elif num == "20":
            payload = "/stories-tagged"
        elif num == "21":
            payload = "/groups"
        elif num == "22":
            payload = "/employees"
        elif num == "23":
            payload = "/friends"
        elif num == "24":
            payload = "/relatives"
        elif num == "25":
            payload = "/friends/pages-liked"

        if num == "all" or num == "0":
            print("Start suffering")
            payloads = ["/places-visited", "/recent-places-visited", "/places-checked-in", "/places-liked", "/pages-liked", '\n'
            "/photos-by", "/photos-liked", "/photos-of", "/photos-commented", "/apps-used", "/videos", "/videos-of", "/videos-by", '\n'
            "/videos-liked", "/videos-commented", "/stories-tagged", "/groups", "/employees", "/friends", "/relatives", "/friends/pages-liked" ]
            for p in payloads:
                time.sleep(10)
                url = "https://www.facebook.com/search/" + fbid + p
                browser_open(url, id)
        url = "https://www.facebook.com/search/" + fbid + payload
        browser_open(url, id)
        #url = "https://www.facebook.com/search/" + fbid + payload
        print(url)

    userinput(fbid, num)
if module == "2":
    #Multiple Target Profiles
    first_target = input("Enter first target: ")
    second_target = input("Enter second target: ")
    target = input("Choose the option you want to use: \n [1] - Common Friends  [2] - Length of Friends  [3] - Common Places  [4] - Common Check-Ins  [5] - Common Likes [6] - Common Photo Tags  [7] - Common Photo Likes \n [8] - Common Photo Comments [9] - Common Video Tags [10] - Common Video Likes  [11] - Common Video Comments  [12] - Common Events  [13] - Common Post Comments  [14] - Common Groups \n")
    def multiple_target_profiles(first_target, second_target):
        if target == "1":
            target_url = "https://www.facebook.com/friendship/" + first_target + "/" + second_target
        elif target == "2":
            target_url = "https://www.facebook.com?" + first_target + "and=" + second_target
        elif target == "3":
            target_url = "https://www.facebook.com/search/" + first_target + "/places-visited/" + second_target + "/places-visited/intersect"
        elif target == "4":
            target_url = "https://www.facebook.com/search/str/" + first_target + "/places-checked-in/" + second_target + "/places-checked-in/intersect"
        elif target == "5":
            target_url = "https://www.facebook.com/search/" + first_target + "/pages-liked/" + second_target + "/pages-liked/intersect"
        elif target == "6":
            target_url = "https://www.facebook.com/search/" + first_target + "/photos-of/" + second_target + "/photos-of/intersect"
        elif target == "7":
            target_url = "https://www.facebook.com/search/" + first_target + "/photos-liked/" + second_target + "/photos-liked/intersect"
        elif target == "8":
            target_url = "https://www.facebook.com/search/" + first_target + "/photos-commented/" + second_target + "/photos-commented/intersect"
        elif target == "9":
            target_url = "https://www.facebook.com/search/" + first_target + "/videos-of/" + second_target + "/videos-of/intersect"
        elif target == "10":
            target_url = "https://www.facebook.com/search/" + first_target + "/videos-liked/" + "/videos-liked/intersect"
        elif target == "11":
            target_url = "https://www.facebook.com/search/" + first_target + "/videos-commented/" + second_target + "/videos-commented/intersect"
        elif target == "12":
            target_url = "https://www.facebook.com/search/" + first_target + "/events/" + second_target + "/events/intersect"
        elif target == "13":
            target_url = "https://www.facebook.com/search/" + first_target + "/stories-commented/" + second_target + "/stories-commented/intersect"
        elif target == "14":
            target_url = "https://www.facebook.com/search/" + first_target + "/groups/" + second_target + "/groups/intersect"
        print(target_url)

        browser_open(target_url, id)
    multiple_target_profiles(first_target, second_target)



if module == "3":
    # Detailed Search
    num = input("[1] - posts about, [2] - keywords, [3] - people that visited, [4] - people that checked in to, [5] - people that like,\n [6] - employees of, [7] - photos-from, [8] - videos-from, [9] - posts-from, [10] - group-members-groupID\n ")
    fbid = input("Enter FB user ID: ")

    def inputdetailed(fbid, num):
        if fbid != 0 or len(fbid) > 0:
            print("Well done! We started to work for you :)")
        elif len(fbid) == 0:
            print("You need to enter something!")
            print("Payload set :)")
        elif len(num) == 0:
            print("payload failed!")
        if num == "1":
            payload = "/stories-keyword"
        elif num == "2":
            payload = "/keywords_posts/intersect/"
        elif num == "3":
            payload = "/visitors/intersect"
        elif num == "4":
            payload = "/users-checked-in/intersect"
        elif num == "5":
            payload = "/likers/intersect"
        elif num == "6":
            payload = "/employees"
        elif num == "7":
            payload = "/photos-in/"
        elif num == "8":
            payload = "/videos-in/"
        elif num == "9":
            payload = "/stories-tagged/"
        elif num == "10":
            payload = "/members"

        url = "https://www.facebook.com/search/str/" + fbid + payload
        print(url)
        browser_open(url, id)
    inputdetailed(fbid, num)

#Twitter
if module == "4":
    option = input("Enter option: [1] - Outgoing Tweets, [2] - Incoming Tweets, [3] - Media posts, [4] - Favorite posts, [5] - First Tweet, \n [6] - Yearly Tweets, [7] - Twitter Analytics, [8] - Twitter Followers, [9] - Twitter Friends, [10] - Historic Bio Changes \n [11] - Profile Details, [12] -  Google Site Search, [13] - Bing Site Search, [14] - Yandex Site Search, [15] - Google Cache Tweets, \n [16] - Google Cache Text, [17] - Twicsy Archive, [18] - Pipl profile, [19] - Additional networks, [20] - Common twitter friends\n ")
    target = input("Enter twitter account: ")
    def common_twitter_friends(target):
        if option == "1":
            target_url = "https://twitter.com/search?f=tweets&q=from%3A" + target + "&src=typd"
        elif option == "2":
            target_url = "https://twitter.com/search?q=to%3A" + target + "&src=typd"
        elif option == "3":
            target_url = "https://twitter.com/" + target + "/media/"
        elif option == "4":
            target_url = "https://twitter.com/login?redirect_after_login=/" + target + "/favorites/"
        elif option == "5":
            target_url = "https://discover.twitter.com/first-tweet#" + target
        elif option == "6":
            target_url = "https://twitter.com/search?f=tweets&q=from%3A" + target + "%20since%3A2015-01-01%20until%3A2015-12-31&src=typd"
        elif option == "7":
            target_url = "https://socialbearing.com/search/user/" + target
        elif option == "8":
            target_url = "https://socialbearing.com/search/followers/" + target
        elif option == "9":
            target_url = "https://socialbearing.com/search/friends/" + target
        elif option == "10":
            target_url = "http://bioischanged.com/" + target
        elif option == "11":
            target_url = "https://foller.me/" + target
        elif option == "12":
            target_url = "https://www.google.com.ua/search?q=site:twitter.com/" + target
        elif option == "13":
            target_url = "http://www.bing.com/search?q=twitter.com/" + target
        elif option == "14":
            target_url = "https://www.yandex.ua/search/?text=https%3A%2F%2Ftwitter.com%2F" + target
        elif option =="15":
            target_url = "https://webcache.googleusercontent.com/search?q=cache:https://twitter.com/" + target
        elif option =="16":
            target_url = "https://webcache.googleusercontent.com/search?q=cache:https://twitter.com/" + target + "&num=1&hl=en&gl=ca&strip=0&vwsrc=1"
        elif option =="17":
            target_url = "http://twicsy.com/u/" + target
        elif option =="18":
            target_url = "https://api.pipl.com/search/v5/?username=" + target + "&key=sample_key"
        elif option =="19":
            target_url = "https://www.google.com.ua/search?q=%22" + target + "%40gmail.com%22OR%22" + target + "%40yahoo.com%22OR%22" + target + "%40hotmail.com%22OR%22" + target + "%40live.com%22OR%22" + target + "%40outlook.com%22OR%22" + target + "%40me.com%22"
        elif option =="20":
            first_target = input('First: ')
            second_target = input('Second: ')
            third_target = input('Third: ')
            target_url = "https://moz.com/followerwonk/compare/" + first_target + "/" + second_target + "/" + third_target + "?op=fl"
        print(target_url)
        browser_open(target_url, id)
    common_twitter_friends(target)
