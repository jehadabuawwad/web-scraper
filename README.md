# Web Scraping

##  Scrape a Wikipedia page and record which passages need citations.

A tool for scrape a wikipedia page and collect information about passages need 
for citaions using a speical library in python called beautifulsoup

## Tools Used

* VS Code
* Python
* Poetry
* Jupyter Lab
* Numpy
* Pandas
* ipykernel
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

* [] Scrape a Wikipedia page and record which passages need citations.
    - [] E.g. History of Mexico has a few “citations needed”.
* [] Your web scraper should report the number of citations needed.
* [] Your web scraper should identify those cases AND include the relevant passage.
    - [] E.g. Citation needed for “lorem spam and impsum eggs”
    - [] Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Implementation Notes

* [] Count function must be named get_citations_needed_count
    - [] get_citations_needed takes in a url and returns an integer
* [] Report function must be named get_citations_needed_report
    - [] get_citations_needed_report takes in a url and returns a string
    - [] the string should be formatted with each citation needed on own line, in order found.
* [x] Module must be named scraper.py

## Author

 Jehad Abu Awwad

---

## Webpage used in project

* [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico)

## Pull requests :

## ---- [Link](https://github.com/Jehadabuawwad/web-scraper/pull/1) -----
