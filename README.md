# Hackernews-Scraper
Scrape hackernews using Scrapy & Python.

## How to use?
1. Star and download/clone this repo.
2. Run `pip3 install scrapy`
3. Run `scrapy crawl hacker-news -o hackernews-data.json`
4. Data will be stored in hackernews-data.json file.

## Global variables to customise
All action is inside `/hackernews/spider/hackernews_spider.py` file. The rest is just a scrapy project template.
1. `PAGINATION_MAX_INDEX`: customise this to change the number of paginated pages you want to scrape.
