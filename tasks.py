from os import read
import requests
import wikipedia
import pywhatkit as kit
import pywhatkit
from email.message import EmailMessage
import smtplib
from datetime import datetime
import random
import pytz
import time
import os
import subprocess as sp

paths = {
    "notepad": "C:\\Program Files\\Notepad++\\notepad++.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe",
}


def open_camera():
    sp.run("start microsoft.windows.camera:", shell=True)


def open_notepad():
    os.startfile(paths["notepad"])


def open_cmd():
    os.system("start cmd")


def open_calculator():
    sp.Popen(paths["calculator"])


def current_time():
    t = time.localtime()
    now_time = time.strftime("%H:%M:%S", t)
    print("Your time is: ", now_time, "in Hour/Minute/Second format")


def timezone_time():
    req_timezone = input("Enter the timezone in this format Continent/Country -\n")
    tz_world = pytz.timezone(req_timezone)
    datetime_world = datetime.now(tz_world)
    print(
        tz_world,
        "time is:",
        datetime_world.strftime("%H:%M:%S"),
        "in Hour/Minute/Second format",
    )


def shutdown():
    cntdwn = input("After How many seconds shall system shutdown? \n")
    pywhatkit.shutdown(cntdwn)


def cncl_shutdown():
    pywhatkit.cancel_shutdown()


def find_my_ip():
    ip_address = requests.get("https://api64.ipify.org?format=json").json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=3)
    return results


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly("+91{number}", message)


def open_whatsapp():
    pywhatkit.open_web()
    if pywhatkit.open_web() is True:
        print("Whatsapp Web is opened")
    else:
        print("Sorry,there was some issue in opening Whatsapp Web")


def take_screenshot():
    file_name = input("What should I save file as? \n")
    pywhatkit.take_screenshot(file_name, 2)
    print("Screenshot is taken and saved as", file_name)


def convert_ascci_art(source_path, target_path):
    kit.image_to_ascii_art(source_path, target_path)
    print("Image converted to ASCII Art and saved as", target_path)


def send_email(receiver_address, subject, message):
    useremail = input("Please input your EMAIL Address-\n")
    password = input("Please input your EMAIL password-\n")
    try:
        email = EmailMessage()
        email["To"] = receiver_address
        email["Subject"] = subject
        email["From"] = useremail
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(useremail, password)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_latest_news():
    news_api_key = input(
        "Please signup for NEWSAPI in https://newsapi.org/register and enter the API key -\n"
    )
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}&category=general"
    ).json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


def get_weather_report(city):
    openweather_app_id = input(
        "Please signup for OpenWeatherMap API  in https://home.openweathermap.org/users/sign_in and enter the API key -\n"
    )
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_app_id}&units=metric"
    ).json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_trending_movies():
    tmdb_api_key = input(
        "Please signup for The Movie Database (TMDB) API  in https://www.themoviedb.org/signup and enter the API key -/n"
    )
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={tmdb_api_key}"
    ).json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]


def get_random_joke():
    headers = {"Accept": "application/json"}
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res["slip"]["advice"]
