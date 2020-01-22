#python3! -- quotes.py -- Scrapes a Goodreads quote page for quotes and authors, then stores all quotes to 'quotes.txt' file and stores all authors to 'authors.txt' file.
import requests, bs4
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time

#opens text files to write to
quote_file = open("quotes.txt", "w", encoding="utf-8") 
author_file = open("authors.txt", "w", encoding="utf-8")

# the main url for the request to begin with ...
# Feel free to change this.
url = 'https://www.goodreads.com/work/quotes/7039054-delivering-happiness-a-path-to-profits-passion-and-purpose?page='

# set the safe header for the requests to be used
headers = {
      'Host': 'www.goodreads.com',
      'Connection': 'keep-alive',
      'User-Agent': 'Mozila/5.0 (X11; Windows x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100',
      'Accept': '*/*',
      #https://www.goodreads.com/quotes/tag/knowledge
      'Referer': 'https://www.goodreads.com/quotes',
      'Accept-Language': 'en-US,en;q=0.9'
      }

# Uses requests-html to get our page, then scrapes the page for quotes
# and authors, storing the information to their relevant text files
# the number in RANGE is the total page numbers so if 100 shows
# then it'll crawl to page 100
for i in range(1):
        link = url + str(i+1)
        print(link)
        r = requests.get(link, headers=headers)
        soup = bs4.BeautifulSoup(r.text, features="lxml")
        text_list = soup.find_all("div", class_= "quoteText")
        for text in text_list:
                text = text.text
                quote = text.split("―",1)[0]
                time.sleep(1)
                print(quote)
                quote_file.write(quote)
                author_list = soup.find_all("span", class_= "authorOrTitle")
     #   for author_text in author_list:
      #          author_text = author_text.text
       #         author = author_text.split(",",1)[0]
        #        time.sleep(1)
         #       print(author)
          #      author_file.write(author)
        #requests.close()

        
        print('Scraping post links for: ' + url)
	

print('Scrape complete.')
quote_file.close()
#author_file.close()
