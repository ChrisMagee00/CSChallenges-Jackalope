from selenium import webdriver
from subprocess import call 

#Nextcloud is a single docker image, and one command is enough to run and execute that image
def install():
    call('sudo docker run -d -p 8080:80 --restart unless-stopped nextcloud', shell = True)
    
#This sets up  nextcloud on its first launch
def setup(admin_username, password, url):
    #open a Selenium browser at the nextcloud page
    browser = webdriver.Firefox()
    browser.get(url)
    
    #fill in the username
    username_field = browser.find_element_by_id('adminlogin')
    username_field.send_keys(admin_username)

    #fill in password
    password_field = browser.find_element_by_id('adminpass')
    password_field.send_keys(password)

    #Click the button to submit
    login_button = browser.find_element_by_css_selector('.primary')
    login_button.click()