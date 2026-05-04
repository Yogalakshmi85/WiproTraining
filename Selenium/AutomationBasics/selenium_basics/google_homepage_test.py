from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = input('Which browser do you want to use')

match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

    case _:
        print('Unknown browser - Not available.\nExecuting with default browser.')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle == 'Google':
    print("Google Homepage loaded - pass")
else:
    print("Google Homepage loaded - Fail")

sleep(3)

driver.quit()
