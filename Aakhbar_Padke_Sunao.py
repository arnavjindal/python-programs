import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch('SAPI.SpVoice')
    speak.Speak(str)

if __name__ == '__main__':
    import requests

    url1 =('https://newsapi.org/v2/top-headlines?country=in&category=technology&sortBy=publishedAt&apiKey=1cb5d20289cb4960b610dc1205b16c55')
    url =('https://newsapi.org/v2/top-headlines?country=in&category=science&sortBy=publishedAt&apiKey=1cb5d20289cb4960b610dc1205b16c55')
    response = requests.get(url)
    response1 = requests.get(url1)
    JS_on = json.loads(response1.text)

    a =response.json()
    for j in range((10)):

        speak(response.json()["articles"][j]["title"])
        time.sleep(0.5)
        speak(f"Next {j+1}st news is:")
    # print(response.text)
    # print(JS_on)
    for i in range(JS_on["totalResults"]):
        # print(i)
        # if i == "article":
        print(JS_on["articles"][i]["title"])
        print(JS_on["articles"][i]["description"])
        print(JS_on["articles"][i])
        speak(JS_on["articles"][i]["title"])
        speak(JS_on["articles"][i]["description"])


        time.sleep(0.5)
        speak("Next news is:")




speak("Thanks for paying attention .. See you tomorrow!!")








#--------------------------------------------------------Harry's code--------------------------------------------------------------------




# Akhbaar padhke sunaao
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")


















