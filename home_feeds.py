#[]{}
import requests
from bs4 import BeautifulSoup

USERNAME=str(input("ENTER THE USERNAME HERE"))
PASSWORD=str(input("ENTER THE PASSWORD HERE"))
PROTECTED_URL = 'https://m.facebook.com/home.php?ref_component=mbasic_home_header'

def login(session, email, password):
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)

    assert response.status_code == 302
    return response.cookies


def filter_feeds(feeds):
    feeds_ret=[]
    i=0
    while i!=len(feeds):
        feeds_ret.append(feeds[i])
        if "shared" not in feeds[i]:
            i+=1
        else:
            i+=2
    return feeds_ret            
                


def Home_feeds(soup,filter):
    feeds=[]        
    data=soup.find_all("h3")
    for link in data:
        if link.strong!=None:
            feeds.append(link.text)

    if filter=="filter":
        feeds=filter_feeds(feeds)
    return feeds            

if __name__ == "__main__":

    session = requests.session()
    cookies = login(session, USERNAME, PASSWORD)
    response = session.get(PROTECTED_URL, cookies=cookies,
allow_redirects=False)
    soup=BeautifulSoup(response.text,"html.parser")
    Home_list=Home_feeds(soup,"filter")
    print(Home_list)
    fx=open("facebook_Home_feeds_1.txt","w") #to save the data as the file 
    fx.write("_-_-"*20+"HOME FEEDS"+"_-_-"*20+"\n"*2)
    for i in  Home_list:
        fx.write(i+"\n"+"-----"*30+"\n")

    fx.close()
    fa=open("facebook_Home_feeds_1.txt","r")
    a=fa.read()
    try:
            print(a)
    except UnicodeEncodeError:
        print("UnicodeEncodeError WAS HERE")    
  
