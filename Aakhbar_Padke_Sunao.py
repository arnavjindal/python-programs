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



#--------------------------------------------------------Alok's code--------------------------------------------------------------------
#--------------------------------------------------------It gives link for more reading --------------------------------------------------------------------

import requests
import json
from win32com.client import Dispatch
def speak(string):
    speak=Dispatch('SAPI.spVoice')
    speak.speak(string)

url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=XXXXXXXXXX')
data=requests.get(url=url)
india=data.json()
print(india['articles'][0]['description'])
for i in range(20):
    print(i,india['articles'][i]['source']['name'])


no=int(input("choose newspaper name"))
speak(india['articles'][no]['title'])
print("for more ",india['articles'][no]['url'])
speak(india['articles'][no]['content'])
speak(india['articles'][no]['description'])






#--------------------------------------------------------Avinash's code--------------------------------------------------------------------
#--------------------------------------------------------It shows the news Computer is reading sideways ------------------------------------------
#--------------------------------------------------------Better code till now--------------------------------------------------------------------


import requests
import json
import time
from win32com.client import Dispatch

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)

data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=YourAPIKEY")

result = data.json()
print(result['status'])
# print(result)

news = result['articles']

speak("Welcome to the CodeWithHarry News Channel")
speak("Here are the top ten news of the awesome country India")
speak("So our first news is ")
for i  in range(0,10):
    print(i)
    print(news[i]['description'])
    speak(news[i]['description'])
    if i>=9:
        break
    time.sleep(2)
    if i == 8:
        speak("So our last news for today is ")
    else:
        speak("Moving To Our next news")


speak("Thanks for listening ! Have a nice day")
speak("Keep coding")
