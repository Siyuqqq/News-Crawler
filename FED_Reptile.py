from selenium import webdriver
import re

browser = webdriver.Safari()
url = 'https://www.federalreserve.gov/newsevents/pressreleases.htm'
browser.get(url)

# print(browser.page_source)

string = browser.page_source
title = re.findall(r'item\.title.*?>(.*?)<', string, re.DOTALL)[0].strip()

print(title)
browser.close()
