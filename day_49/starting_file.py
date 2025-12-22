from selenium import webdriver
#Accessing the web page
URL = "https://appbrewery.github.io/gym/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
