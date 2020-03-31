from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
import requests
import pandas as pd, numpy as np
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
links = ['Your search query links here']

link_to_video = []
options = Options()
options.set_preference('permissions.default.image', 2)
options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
options.headless = True
for link in links:

    browser = webdriver.Firefox(options=options ,executable_path='C:/Users/milos/Downloads/geckodriver.exe')
    browser.get(link)
    time.sleep(6)
    while len(link_to_video) <600:
        soup = bs(browser.page_source, 'html.parser')
        a = soup.find_all('div', id = "contents", class_ = "style-scope ytd-item-section-renderer")[0]
        b = a.find_all('div', class_='text-wrapper style-scope ytd-video-renderer')
        for i in np.arange(0, len(a)):
            try:
                if b[i].a["href"] not in link_to_video:   
                    link_to_video.append(b[i].a["href"])

                print(str(i) + " loop of adding link")
            except:
                continue
        
        browser.execute_script("window.scrollBy(0, 600);")

        time.sleep(2)
        

    

Channel_link = [] 
Title = []
Channel_name = []
Subscribers = []
View_count = []
Likes = []
Dislikes = []
Date = []
for i in link_to_video:
    try:
        source = requests.get('https://youtube.com' + i).text
        soup = bs(source, 'lxml')
        div_s = soup.findAll('div')
        title_source = div_s[1].find('span', class_='watch-title')
        channel_source = div_s[1].find('a', class_="yt-uix-sessionlink spf-link")
        view_counts_source = div_s[1].find(class_='watch-view-count')
        subscribers_source = div_s[1].find('span',
                                       class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count")
        likes_source = div_s[1].find('button',
                                 class_="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-unclicked yt-uix-clickcard-target yt-uix-tooltip")
        dislikes_source = div_s[1].find('button',
                                    class_="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-unclicked yt-uix-clickcard-target yt-uix-tooltip")
        date_source = soup.find("strong", attrs={"class": "watch-time-text"})
        if title_source is None:
            Title.append('None')
        else:
            Title.append(title_source.text.strip())
        if channel_source is None:
            Channel_name.append('None')
            Channel_link.append('None')
        else:

            Channel_name.append(channel_source.text.strip())
            Channel_link.append('https://www.youtube.com' + channel_source.get('href'))
        try:

            if view_counts_source is None:
                View_count.append('None')
            else:
                View_count.append(view_counts_source.text.strip().split()[0])
        except IndexError:
                View_count.append('None')


        if subscribers_source is None:
            Subscribers.append('None')
        else:
            Subscribers.append(subscribers_source.text.strip())

        if likes_source is None:
            Likes.append('None')
        else:
            Likes.append(likes_source.text.strip())

        if dislikes_source is None:
            Dislikes.append('None')
        else:
            Dislikes.append(dislikes_source.text.strip())

        if date_source is None:
            Date.append('None')
        else:
            Date.append(date_source.text)
        print(i)
    except:
        pass

descrption = []
for i in np.arange(0, len(Channel_link)):
    if Channel_link[i] == 'None':
        descrption.append('None')
    else:
        html3 = requests.get(Channel_link[i] + '/about')
        soup3 = bs(html3.text, 'html.parser')
        descrption_source = soup3.find_all('div')[1].pre
        if descrption_source is None:
            descrption.append('None')
        else:
            descrption.append(descrption_source.text)
    print(i)
emails = []
for i in np.arange(0, len(descrption)):

    if descrption[i] == 'None':
        emails.append("None")
    elif not re.findall(r'[\w\.-]+@[\w\.-]+', str(descrption[i])):
        emails.append("None")
    else:
        
        emails.append(list(dict.fromkeys(re.findall(r'[\w\.-]+@[\w\.-]+', str(descrption[i])))))
    print(i)
result = {'Titles': Title, 'Usernames': Channel_name, 'Link to channels': Channel_link,
          'Link to video': link_to_video, 'Number of Views': View_count, 'Likes': Likes, 'Dislikes': Dislikes,
          'Subsrcibers': Subscribers, 'E-mail': emails, 'Description': descrption, 'Date added': Date}
DF = pd.DataFrame(result)


DF.to_excel("output.xlsx")