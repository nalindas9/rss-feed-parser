# rss-feed-parser

[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/nalindas9/rss-feed-parser/blob/master/LICENSE)

## About
RSS Feed Parser that calls a URL every 1 hour and scrapes the news data and saves it to a CSV file. Currently scrapes this [url](https://www.yahoo.com/news/rss/),
[webpage](https://www.yahoo.com/news/).

## Output

https://user-images.githubusercontent.com/44141068/157387720-42a434ff-b4eb-4ed6-a6e2-ebdac6f873b8.mp4

## System and library requirements

- Ubuntu==18.04.5 LTS
- Python==3.6.9
- beautifulsoup4==4.10.0
- pandas==1.1.5
- requests==2.27.1

## How to Run
1. Clone this repo. <br>
2. Navigate into the folder `rss-feed-parser` <br>
3. Create and activate [Virtual Environment](https://docs.python.org/3/library/venv.html) <br>
4. Upgrade pip using `python -m pip install --upgrade pip`.
5. Install requirements.txt using command `pip install -r requirements.txt`
6. To run the code, from the terminal, run the command `python3 main.py` <br>
7. You should see the csv files being saved into the `news` folder in the current directory.



