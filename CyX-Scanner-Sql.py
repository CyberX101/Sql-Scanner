#Cyber_Max
#CyX-Team
#CyX-Devs
import requests
from time import sleep
from bs4 import BeautifulSoup
import sys
import webbrowser
import os
from urllib.parse import urljoin
os.system('clear')
#color 
red = '\033[31m'
green = '\033[32m'

CyX = (f'''{red}

   _____     __   __   _____                                             _ 
  / ____|    \ \ / /  / ____|                                           | |
 | |    _   _ \ V /  | (___   ___ __ _ _ __  _ __   ___ _ __   ___  __ _| |
 | |   | | | | > <    \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| / __|/ _` | |
 | |___| |_| |/ . \   ____) | (_| (_| | | | | | | |  __/ |    \__ \ (_| | |
  \_____\__, /_/ \_\ |_____/ \___\__,_|_| |_|_| |_|\___|_|    |___/\__, |_|
         __/ |                                                        | |  
        |___/                                                         |_|  




{green}@CyberX10

''')
print(CyX)
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" 
def get_forms(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")
def form_details(form):
    detailsOfForm = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({
            "type": input_type, 
            "name" : input_name,
            "value" : input_value,
        })
    detailsOfForm['action'] = action
    detailsOfForm['method'] = method
    detailsOfForm['inputs'] = inputs
    return detailsOfForm
def vulnerable(response):
    errors = {"quoted string not properly terminated", 
              "unclosed quotation mark after the charachter string",
              "you have an error in you SQL syntax" 
             }
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False
def CyX_Scanner_Sql(url):
    forms = get_forms(url)
    print(f"{green}[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        details = form_details(form)
        
        for i in "\"'":
            data = {}
            for input_tag in details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag['name']] = input_tag["value"] + i
                elif input_tag["type"] != "submit":
                    data[input_tag['name']] = f"test{i}"
            print(url)
            form_details(form)

            if details["method"] == "post":
                res = s.post(url, data=data)
            elif details["method"] == "get":
                res = s.get(url, params=data)
            if vulnerable(res):
                print(f"{red}[+] SQL injection attack vulnerability in link: ", url )
            else:
                print(f"{green}[+] No SQL injection attack vulnerability detected")
                break
if __name__ == "__main__":
    url_Target = input(f'{red}Enter Website To Scan : ')
    CyX_Scanner_Sql(url_Target)

Cyx = input('Do you want to follow our channel on Telegram ? (y/n)')
if Cyx == 'y':
    webbrowser.open("https://t.me/CyX_Security")
elif Cyx == 'n':
    print('(#_#)')
    exit()
    


