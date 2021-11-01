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

def get_citations_needed_report(wiki_url):        
    response=requests.get(wiki_url)
    html_text=response.text
    
    cleaned_paragraphs=[]
    soup=BeautifulSoup(html_text,"html.parser")
    body_tag = soup.body
    main_div = body_tag.find("div",id="content")
    sub1_div = main_div.find("div",id="bodyContent")
    sub2_div = sub1_div.find("div",id="mw-content-text")
    sups=sub2_div.find_all("sup")
    text=[]
    for item in sups:
        if item.text=="[citation needed]":
            cleaned_paragraphs.append(item.parent.text)
    for par in cleaned_paragraphs:
        text+=[par]
    for idx, par in enumerate(text,start=1):
        print(f"{idx}: {par}\n")
    return text    

if __name__ =="__main__":
    wiki_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    get_citations_needed_count(wiki_url)
    get_citations_needed_report(wiki_url)