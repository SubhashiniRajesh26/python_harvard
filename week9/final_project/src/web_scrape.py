from bs4 import BeautifulSoup
import requests
import csv
# import pandas as pd

def main():
    source = requests.get('https://coreyms.com').text
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open("web_scrape.csv", 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'video_link'])

    for article in soup.find_all('article'):
    # print(soup.prettify)
        headline = get_article_name(article)
        summary = get_summary(article)
        vd_link = get_link(article)
        csv_writer.writerow([headline, summary, vd_link])
    csv_file.close()

        
def get_article_name(article):
    
    # print(article.prettify())
    headline = article.h2.a.text
    return headline 

def get_summary(article):
    summary = article.find('div', class_='entry-content').p.text
    return summary


def get_link(article):
    try:
        video_link = article.find('iframe', class_='youtube-player')['src']
        # print(article.prettify())
        # print(video_link)
        video_id = video_link.split('/')[4]
        # print(video_id)
        video_id = video_id.split('?')[0]
        # print(video_id)
        yt_link = f'https://youtube.com/watch?v={video_id}'
        return yt_link
    except Exception as e:
        yt_link = None
        return yt_link



main()