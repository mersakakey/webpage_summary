import requests
from bs4 import BeautifulSoup
import re

# Webページを取得して解析する

def get_html_old(webpage_url):
    html = requests.get(webpage_url)
    soup = BeautifulSoup(html.content, "html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    text=soup.get_text()
    lines= [line.strip() for line in text.splitlines()]

    text="\n".join(line for line in lines if line)

    # HTML全体を表示する
    print(text)
    return(text)

def get_html(webpage_url):
    html = requests.get(webpage_url)
    soup = BeautifulSoup(html.content, "html.parser")

    #print(soup.prettify())
    #contents = soup.find('div', class_="single_article_contents")
    texts_p = [c.get_text() for c in soup.find_all('p')]

    texts_p = [t.replace('\n','') for t in texts_p if re.match('\S', t)]
    text="\n".join(line for line in texts_p if line)

    # HTML全体を表示する
    print(text)
    return text

#get_html("https://qiita.com/keitomatsuri/items/4c848d58ea5f9b3ebe42")
