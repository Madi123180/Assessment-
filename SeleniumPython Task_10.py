import time   #imported time library to use time.sleep
from selenium import  webdriver #imported webdriver to launch and execute TC in particular browser
from selenium.webdriver.common.by import By
import os  #imported os library to locate the local files

# created variable
driver = webdriver.Chrome()

#sending request to launch the url in the specified browser using created variable
driver.get("https://www.saucedemo.com/")

#finding Username and Password fields using ID element and entering the values
search = driver.find_element(By.ID, "user-name")
search.send_keys("standard_user")
search = driver.find_element(By.ID, "password")
search.send_keys("secret_sauce")

#Clicking the login button after entering the valid credentials
driver.find_element(By.ID, "login-button").click()

#Req 1:
#fetching title of the webpage
print(driver.title)

#Req 2:
#fetching the currenturl of the webpage
print(driver.current_url)

#Req 3:
#fetching entire content of the webpage
print(driver.page_source)

#creating text file to add extracted content into it
f=open("Webpage_task_11.txt","w")

#writing the extracted content to the newly created file
f.write(driver.page_source)

#opening and reading the content.
f=open("Webpage_task_11.txt")
print(f.read())

#setting sleep time to view the screen clearly
time.sleep(3)

#using quit command to close the browser
driver.quit()

