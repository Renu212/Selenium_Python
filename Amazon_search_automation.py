#import necessary libraries
from selenium import webdriver
from getpass import getpass

#intializing input variables
USERNAME = input("Enter email or mobile number: ")
password = getpass("enter passowrd: ")# used getpass so that typed password cannot be visible in terminal

#invoking browser window
driver= webdriver.Chrome("C:\\Users\\Renuka\\Downloads\\chromedriver_win32\\chromedriver.exe")
#specifiying the page to be opened
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# indicating elements to find by ID
username_textbox= driver.find_element_by_id('ap_email')
username_textbox.send_keys(USERNAME)

continue_button= driver.find_element_by_id('continue')
continue_button.submit()

password_textbox= driver.find_element_by_id('ap_password')
password_textbox.send_keys(password)

login_button= driver.find_element_by_id('signInSubmit')
login_button.submit()

search= driver.find_element_by_id('twotabsearchtextbox')
search.send_keys('drawing art tool kit')

find=driver.find_element_by_id('nav-search-submit-button')
find.submit()


