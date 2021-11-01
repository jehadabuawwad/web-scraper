# Web Scraping

##  Scrape a Wikipedia page and record which passages need citations.

A tool for scrape a wikipedia page and collect information about passages need 
for citaions using a speical library in python called beautifulsoup

## Tools Used

* VS Code
* Python
* Poetry
* requests
* beautifulsoup
* flake8
* black 

---

## Getting Started

Clone this repository to your local machine.

```python
$ git clone https://github.com/Jehadabuawwad/web-scraper.git
```

Once downloaded, activate your virtual environment and run by 
```python 
poetry install
poetry shell

```

The poetry tools will automatically install any dependencies. Before running the application

Unit testing is included in the Jupyter Notebook

## Feature Tasks and Requirements

* [x] Scrape a Wikipedia page and record which passages need citations.
    - [x] E.g. History of Mexico has a few “citations needed”.
* [x] Your web scraper should report the number of citations needed.
* [x] Your web scraper should identify those cases AND include the relevant passage.
    - [x] E.g. Citation needed for “lorem spam and impsum eggs”
    - [x] Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Implementation Notes

* [x] Count function must be named get_citations_needed_count
    - [x] get_citations_needed takes in a url and returns an integer
* [x] Report function must be named get_citations_needed_report
    - [x] get_citations_needed_report takes in a url and returns a string
    - [x] the string should be formatted with each citation needed on own line, in order found.
* [x] Module must be named scraper.py

## User Acceptance Tests

* [x] verify that correct count of citations needed is calculated
* [x] verify that preceding passage

## Author

 Jehad Abu Awwad

---

## Webpage used in project

* [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico)

## Pull requests :

## ---- [Link](https://github.com/Jehadabuawwad/web-scraper/pull/1) -----
