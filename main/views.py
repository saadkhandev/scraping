import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('http://coreyms.com').text

# Print all page
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
# Print one article
# article = soup.find('article')
# print(article)

# Print all article
for article in soup.find_all('article'):

    # Print specific a tag
    headline = article.h2.a.text
    print(headline)

    # Print article summary
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:

        # Grab youtube video source
        vid_source = article.find('iframe', class_='youtube-player')['src']
        # print(vid_source)

        # Grab video id
        vid_id = vid_source.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # print(vid_id)

        # Youtube link
        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
