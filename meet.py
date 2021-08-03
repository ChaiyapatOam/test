from selenium import webdriver
from bs4 import BeautifulSoup as soup

driver = webdriver.Chrome(r'C:\Users\ADMIN\Desktop\Selenium\chromedriver.exe')

url = 'https://meet.google.com/enb-kcfi-xjz'

driver.get(url)