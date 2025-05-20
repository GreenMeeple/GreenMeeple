# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'https://greenmeeple.github.io/archives/'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'} 

def addIntro(f):
	txt = '''<p align="center"><img src="https://github.com/greenmeeple/greenmeeple/blob/output/github-contribution-grid-snake.svg"/></p>
<p align="center"> M.Sc Cybersecurity at Saarland University, B.Eng Information Engineering at CUHK. </p>  
<p align="center"> Cybersecurity Analyst, focus on LLM security. Experienced in C++, Python, and Full Stack Development </p>  
<p align="center"><a href="https://greenmeeple.github.io/about/resume.pdf" align="center">Click here to check my personal CV</a></p>''' 

	f.write(txt)

def addProjectInfo(f):
	txt ='''
### Projects and Repos

- [MensaarLecker](https://github.com/GreenMeeple/MensaarLecker) A fully automated scraper and static website for the Saarbrücken Mensa, powered by Python, Selenium, Google Sheets, and GitHub Actions.
- [udsfahrplan](https://github.com/GreenMeeple/uds-fahrplan) A lightweight Telegram bot designed for Saarland University students
- [hafas-bitmask-calculator](https://github.com/GreenMeeple/hafas-bitmask-calculator) A simple web-based tool to help you decode and encode bitmasks used by the HAFAS API.
- [hexo-zhruby](https://github.com/GreenMeeple/hexo-zhruby) A Hexo Tag plugin developed using Node.js
- [Azul_Test](https://github.com/xindoo/eng-practices-cn) A C++ program based on a boardgame Azul by Michael Kiesling.
- [More Projects](https://github.com/GreenMeeple?tab=repositories)''' 
	f.write(txt) 

from lxml import etree
import urllib3

def addBlogInfo(f):
    http = urllib3.PoolManager(num_pools=5, headers=headers)
    resp = http.request('GET', blogUrl)
    resp_tree = etree.HTML(resp.data.decode("utf-8"))

    # Select all articles in the timeline
    articles = resp_tree.xpath(".//div[@class='timeline']/article")
    f.write("\n### Personal Blog\n")

    cnt = 0
    for article in articles:
        if cnt >= 5:
            break

        # Extract title
        title_list = article.xpath(".//p[@class='title']/a/text()")
        if not title_list:
            print("Skipping an entry due to missing title")
            continue
        title = title_list[0].strip()

        url_list = article.xpath(".//p[@class='title']/a/@href")
        if not url_list:
            print("Skipping an entry due to missing URL")
            continue
        url = url_list[0].strip()

        if not url.startswith("http"):
            url = f"https://greenmeeple.github.io{url}"

        item = f'- [{title}]({url})\n'
        f.write(item)
        cnt += 1

    f.write('\n[More Posts](https://greenmeeple.github.io/)\n')

if __name__=='__main__':
	f = open('README.md', 'w+',encoding='utf-8')
	addIntro(f)
	f.write('<table align="center"><tr>\n')
	f.write('<td valign="top" width="33%">\n')
	addProjectInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="33%">\n')
	addBlogInfo(f)
	f.write('\n</td>\n')
	f.write('</tr></table>\n')
	f.close 
