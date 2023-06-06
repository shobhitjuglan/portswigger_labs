from selenium import webdriver

browser= webdriver.Chrome()

browser.get('https://github.com/shobhitjuglan')

#Refreshes the web page
for i in range(10):
    browser.refresh()