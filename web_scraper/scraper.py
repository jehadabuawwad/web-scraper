import requests   
from bs4 import BeautifulSoup

def get_citations_needed_count(wiki_url):
    counter=0
    response=requests.get(wiki_url)
    html_text=response.text
    
    soup=BeautifulSoup(html_text,"html.parser")
    body_tag = soup.body
    main_div = body_tag.find("div",id="content")
    sub1_div = main_div.find("div",id="bodyContent")
    sub2_div = sub1_div.find("div",id="mw-content-text")
    sups=sub2_div.find_all("sup")
    
    for item in sups:
        if item.text=="[citation needed]":
            counter+=1
    print(f"Counts of Paragraphs need citations is {counter}")
    return counter