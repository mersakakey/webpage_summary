import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

def get_html(webpage_url):
    html = requests.get(webpage_url)
    soup = BeautifulSoup(html.content, "html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    text=soup.get_text()
    lines= [line.strip() for line in text.splitlines()]

    text="\n".join(line for line in lines if line)

    # HTML全体を表示する
    return(text)

#print(get_html("https://yumarublog.com/python/lxml/"))