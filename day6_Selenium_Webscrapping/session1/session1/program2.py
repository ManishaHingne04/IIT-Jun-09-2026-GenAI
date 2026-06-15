from bs4 import BeautifulSoup


def function1():
    # read the html source from a file
    file = open("./file1.html", "r")
    data = file.read()

    # create a soup
    soup = BeautifulSoup(data, "html.parser")

    # find the h1 element
    element = soup.find("h1")
    print(f"info = {element.text}")

    file.close()


# function1()


def function2():
    file = open("./file1.html", "r")
    data = file.read()

    # create soup
    soup = BeautifulSoup(data, "html.parser")

    # find cdac information

    # find the div for cdac which has got a class "cdac"
    div = soup.find('div', {"class": "cdac"})
    p_elements = div.find_all("p")
    for p in p_elements:
        print(p.text)

    file.close()


# function2()


def function3():
    file = open("./file2.html", "r")
    data = file.read()

    # create soup
    soup = BeautifulSoup(data, "html.parser")

    # find all minimum temperatures per hour
    div = soup.find("div", {'class': "min"})

    # find all li items
    li_elements = div.find_all("li")
    for li in li_elements:
        # values = li.text.split(":")
        # print(f"temperature at {values[0]} is {values[1].replace(' ', '')}")

        values = li.text.split(": ")
        print(f"temperature at {values[0]} is {values[1]}")

    file.close()


# function3()


def function4():
    # read the contents of file
    file = open("index.html", "r")
    data = file.read()
    file.close()

    # create a new file to store the info
    file = open("weather.csv", "w")

    # write the header
    file.write("day,date,high,low,condition,precipitation\n")

    # create the soup
    soup = BeautifulSoup(data, "html.parser")

    # find the parent of all the divs (having class = page-content content-module"
    parent = soup.find("div", {"class": "page-content content-module"})

    # find the division having class "daily-wrapper" in the parent
    div_elements = parent.find_all("div", {"class": "daily-wrapper"})

    # iterate over the div_elements and find the information
    for div in div_elements:

        # find the day
        span_day = div.find("span", {"class": "dow"})
        day = span_day.text

        # find the date
        span_date = div.find("span", {"class": "sub"})
        date = span_date.text

        # find the high temperature
        span_high = div.find("span", {"class": "high"})
        high = span_high.text.replace("°", "")

        # find the copy temperature
        span_low = div.find("span", {"class": "low"})
        low = span_low.text.replace("°", "").replace("/", "")

        # find the weather condition
        div_condition = div.find("div", {"class": "phrase"})
        condition = div_condition.text.replace("\n", "").replace("\t", "")

        # find the precipitation
        div_precip = div.find("div", {"class": "precip"})
        precipitation = div_precip.text.replace("%", "").replace("\n", "").replace("\t", "")

        print(f"day = {day}, date = {date}, high = {high}, low = {low}, condition = {condition}, precipitation = {precipitation}")
        file.write(f"{day},{date},{high},{low},{condition},{precipitation}\n")

    file.close()


# function4()


def function5():
    import pandas as pd

    df = pd.read_csv("weather.csv")
    print(df.columns)
    print(df)


function5()

# https://chromedriver.chromium.org/downloads
# https://github.com/mozilla/geckodriver/releases
