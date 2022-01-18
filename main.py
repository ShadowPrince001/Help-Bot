from functions_on import (
    find_my_ip,
    get_latest_news,
    get_random_advice,
    get_random_joke,
    get_trending_movies,
    get_weather_report,
    play_on_youtube,
    search_on_google,
    search_on_wikipedia,
    send_email,
    send_whatsapp_message,
    open_whatsapp,
    take_screenshot,
    convert_ascci_art,
    shutdown,
    cncl_shutdown,
)
from functions_of import (
    open_calculator,
    open_camera,
    open_cmd,
    open_notepad,
    current_time,
    timezone_time,
)
from datetime import datetime
import pytz
from info import opening_text, paths
import random
import requests
import wikipedia
import pywhatkit as kit
import pywhatkit

import os
import subprocess as sp


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
        query = " " + take_user_input() + " "
        
        if "open camera" in query:
            open_camera()
            
        elif "open calculator" in query:
            open_calculator()
            
        elif "open command prompt" in query:
            open_cmd()
            
        elif "open notepad" in query:
            open_notepad()
            
        elif " time " in query:
            current_time()
            
        elif " timezone " in query:
            timezone_time()
            
        elif "ip address" in query:
            ip_address = find_my_ip()
            print("Your IP Address is", str(ip_address))

        elif " shutdown " in query:
            shutdown()

        elif " cancel shutdown " in query:
            cncl_shutdown()

        elif "wikipedia" in query:
            search_query = input(
                "What do you want to search on Wikipedia, sir?\n"
            ).lower()
            results = search_on_wikipedia(search_query)
            print("According to Wikipedia,", str(results))

        elif "youtube" in query:
            video = input("What do you want to play on Youtube, sir?\n").lower()
            play_on_youtube(video)

        elif "search on google" in query:
            question = input("What do you want to search on Google, sir?\n").lower()
            search_on_google(question)

        elif " send whatsapp message " in query:
            number = input(
                "On what number should I send the message sir? \n Enter the number: "
            )
            message = input("What is the message sir?").lower()
            send_whatsapp_message(number, message)
            print("I've sent the message sir.")

        elif "open whatsapp" in query:
            open_whatsapp()

        elif "screenshot" in query:
            take_screenshot()

        elif "ascii" in query:
            source_path = input("Enter path of image:")
            target_path = input("Enter where to save of ASCII Art:")
            convert_ascci_art(source_path, target_path)

        elif "send an email" in query:
            receiver_address = input(
                "On what email address do I send sir? Enter email address: "
            )
            subject = input("What should be the subject sir?\n").capitalize()
            message = input("What is the message sir?\n").capitalize()
            if send_email(receiver_address, subject, message):
                print("I've sent the email sir.")
            else:
                print(
                    "Something went wrong while I was sending the mail. Please check the error logs sir."
                )

        elif "joke" in query:
            print("Hope you like this one sir")
            joke = get_random_joke()
            print(joke)

        elif "advice" in query:
            print("Here's an advice for you, sir")
            advice = get_random_advice()
            print(advice)

        elif "trending movies" in query:

            print("Some of the trending movies are: {get_trending_movies()}")
            print(*get_trending_movies(), sep="\n")

        elif "news" in query:
            print("I'm reading out the latest news headlines, sir")
            print(*get_latest_news(), sep="\n")

        elif "weather" in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            print("Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            print(
                "The current temperature is {temperature}, but it feels like {feels_like}"
            )
            print("Also, the weather report talks about {weather}")

        else:
            print("Sorry, I could not understand you Sir.")
            query = "None"
