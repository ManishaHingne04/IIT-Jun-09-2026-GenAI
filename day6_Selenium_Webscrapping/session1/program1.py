# import the bs4 library
from bs4 import BeautifulSoup


html = """
<html>
    <head>
        <title>page1</title>
    </head>
    <body>
        <h1>my website</h1>
        <h2>menu1</h2>
        <p>this is paragraph 1</p>
        <p>this is paragraph 2</p>
        <p>this is paragraph 3</p>

        <h2>Languages</h2>        
        <ul>
            <li>C</li>
            <li>C++</li>
            <li>Python</li>
            <li>Java</li>
            <li>JavaScript</li>
        </ul>
    </body>
</html>
"""


def function1():
    # create a soup
    soup = BeautifulSoup(html, "html.parser")

    # find the "my website" from the html source
    # find the h1 from soup
    element = soup.find("h1")
    print(f"info = {element.text}")

    # find "menu1" from html source
    element = soup.find("h2")
    print(f"info = {element.text}")


# function1()


def function2():
    # create a soup
    soup = BeautifulSoup(html, "html.parser")

    # find the paragraph (<p>)
    # element = soup.find("p")
    # print(f"info = {element.text}")

    # find the paragraphs (<p>)
    elements = soup.find_all("p")
    for element in elements:
        print(f"info = {element.text}")


# function2()


def function3():
    # create a soup
    soup = BeautifulSoup(html, "html.parser")

    # find the languages from html source
    elements = soup.find_all("li")
    for element in elements:
        print(f"language = {element.text}")


function3()
