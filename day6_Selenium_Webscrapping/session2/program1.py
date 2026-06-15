# web driver is used to connect with respective browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def function1():
    # initialize the web driver
    driver = webdriver.Chrome("/tmp/chromedriver")

    # visit required url
    driver.get("https://google.co.in")

    # close the driver
    driver.close()


# function1()


def function2():
    driver = webdriver.Chrome("/tmp/chromedriver")
    driver.get("https://google.co.in")
    time.sleep(2)

    # search for an element named input with name=q
    element = driver.find_element(By.NAME, "q")
    time.sleep(2)

    # search for iPhone 15
    element.send_keys("iPhone 15")
    time.sleep(2)

    element.send_keys(Keys.ENTER)
    time.sleep(2)

    driver.close()


# function2()


def function3():
    driver = webdriver.Chrome("/tmp/chromedriver")
    driver.get("https://www.accuweather.com/en/in/pimpri-chinchwad/204843/daily-weather-forecast/204843")

    # wait for 5 seconds till the website is getting loaded
    time.sleep(5)

    # parent = soup.find("div", {"class": "page-content content-module"})
    parent = driver.find_element(By.CLASS_NAME, "page-content")

    # find the division having class "daily-wrapper" in the parent
    # div_elements = parent.find_all("div", {"class": "daily-wrapper"})
    div_elements = parent.find_elements(By.CLASS_NAME, "daily-wrapper")
    print(div_elements)

    # iterate over the div_elements and find the information
    for div in div_elements:

        # find the day
        # span_day = div.find("span", {"class": "dow"})
        span_day = div.find_element(By.CLASS_NAME, "dow")
        day = span_day.text

        # find the date
        # span_date = div.find("span", {"class": "sub"})
        span_date = div.find_element(By.CLASS_NAME, "sub")
        date = span_date.text

        # find the high temperature
        # span_high = div.find("span", {"class": "high"})
        span_high = div.find_element(By.CLASS_NAME, "high")
        high = span_high.text.replace("°", "")

        # find the copy temperature
        # span_low = div.find("span", {"class": "low"})
        span_low = div.find_element(By.CLASS_NAME, "low")
        low = span_low.text.replace("°", "").replace("/", "")

        # find the weather condition
        # div_condition = div.find("div", {"class": "phrase"})
        div_condition = div.find_element(By.CLASS_NAME, "phrase")
        condition = div_condition.text.replace("\n", "").replace("\t", "")

        # find the precipitation
        # div_precip = div.find("div", {"class": "precip"})
        div_precip = div.find_element(By.CLASS_NAME, "precip")
        precipitation = div_precip.text.replace("%", "").replace("\n", "").replace("\t", "")

        print(f"day = {day}, date = {date}, high = {high}, low = {low}, condition = {condition}, precipitation = {precipitation}")

    driver.close()


function3()


def function4():
    driver = webdriver.Chrome("/tmp/chromedriver")
    driver.get("file:///Volumes/Data/Sunbeam/2023/march/dbda/python_r/mar30/code/session2/page1.html")
    time.sleep(2)

    # find the button
    button = driver.find_element(By.ID, "button1")
    button.click()

    time.sleep(2)
    driver.close()


# function4()
