import functions_of
import functions_on
from datetime import datetime
import pytz
from info import opening_text, paths
import random

import os
import subprocess as sp
import pprint

def greet_user():
    """Greets the user according to the time"""
    username = input("May I have your name please? \n")
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        print("Good Morning Mr.", (username), ".I am AVA. ")
    elif (hour >= 12) and (hour < 16):
        print("Good Afternoon Mr.", (username), ".I am AVA. ")
    elif (hour >= 16) and (hour < 24):
        print("Good Evening Mr.", (username), ".I am AVA. ")


def take_user_input():
    query = input("How may I assist you? \n")
    if not "exit" in query or "stop" in query:
        print(random.choice(opening_text))
    else:
        hour = datetime.now().hour
        if hour >= 21 and hour < 6:
            print("Good night sir, take care!")
        else:
            print("Have a good day sir!")
        exit()
    return query


if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input()
        if "open camera" in query:
            open_camera()
        elif "open calculator" in query:
            open_calculator()
        elif "open command prompt" in query:
            open_cmd()
        elif "open notepad" in query:
            open_notepad()
        elif "time" in query:
            current_time()
        elif "timezone" in query:
            req_timezone = input("Enter the timezone-/n")
            timezone_time()
        elif 'ip address' in query:
            ip_address = find_my_ip()
            print('Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            print('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            print("According to Wikipedia, {results}")
            
        elif 'youtube' in query:
            print('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            print('What do you want to search on Google, sir?')
            question = take_user_input().lower()
            search_on_google(question)

        elif "send whatsapp message" in query:
            number = input("On what number should I send the message sir? /n Enter the number: ")
            print("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            print("I've sent the message sir.")

        elif "send an email" in query:
            useremail=input("Please input your EMAIL Address-/n")
            password = input("Please input your EMAIL password-/n")
            receiver_address = input(""On what email address do I send sir? Enter email address: ")
            print("What should be the subject sir?")
            subject = take_user_input().capitalize()
            print("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                print("I've sent the email sir.")
            else:
                print("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            print("Hope you like this one sir")
            joke = get_random_joke()
            print(joke)
            
        elif "advice" in query:
            print("Here's an advice for you, sir")
            advice = get_random_advice()
            pprint(advice)

        elif "trending movies" in query:
            openweather_app_id = input("Please signup for OpenWeatherMap API  in https://home.openweathermap.org/users/sign_in and enter the API key -/n")
            print("Some of the trending movies are: {get_trending_movies()}")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            news_api_key = input("Please signup for NEWSAPI in https://newsapi.org/register and enter the API key -/n")
            print("I'm reading out the latest news headlines, sir")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            print("Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            print("The current temperature is {temperature}, but it feels like {feels_like}")
            print("Also, the weather report talks about {weather}")
            
        else:
            print("Sorry, I could not understand you Sir.")
            query = "None"
        
