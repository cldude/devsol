from selenium import webdriver
import os
driver=webdriver.Chrome()
driver.get("http://www.google.com")

class sample:
    def __init__(self):
        pass


def hello(user):
    print "Hello "+ user


def main():
    hello('harsha')

if __name__=="__main__":
    main()
else:
    "somebody else running the prog"

