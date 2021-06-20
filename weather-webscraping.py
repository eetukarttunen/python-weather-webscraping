# Python Webscraping script to get weather data with only one click (Joensuu area).
# author github @eetukarttunen
from selenium import webdriver
browser = webdriver.Chrome('./chromedriver')

browser.get('https://www.supersaa.fi/suomi/joensuu/')

date  = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/article/h2')
print(date.get_property('innerHTML'))

temperature  = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/article/div[2]/div[1]/div/div[1]/div/span[1]')
print("Lämpötila Joensuussa tällä hetkellä:", temperature.get_attribute('innerHTML'))

wind_speed = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/article/div[2]/div[1]/div/div[1]/div/span[2]/span[1]/span[2]')
print("Tuulen nopeus", wind_speed.get_property('innerHTML'), "m/s")

browser.quit()