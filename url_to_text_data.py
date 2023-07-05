import requests
from bs4 import BeautifulSoup
import re

def url_to_text_data(webpage_url):
    html = requests.get(webpage_url)
    soup = BeautifulSoup(html.content, "html.parser")

    # 取得してきたhtmlから本文を抜き出してテキストに変換
    text = [c.get_text() for c in soup.find_all('p')]

    text = [t.replace('\n','') for t in text if re.match('\S', t)]
    treated_text="\n".join(line for line in text if line)

    return treated_text