from selenium import webdriver
from subprocess import call 


def login(admin_username, password, url):
    browser = webdriver.Firefox()
    browser.get(url)
    username_field = browser.find_element_by_id('adminlogin')
    username_field.send_keys(admin_username)

    password_field = browser.find_element_by_id('adminpass')
    password_field.send_keys(password)

    login_button = browser.find_element_by_css_selector('.primary')
    login_button.click()

def install():
    call('sudo docker run -d -p 8080:80 --restart unless-stopped nextcloud', shell = True)

