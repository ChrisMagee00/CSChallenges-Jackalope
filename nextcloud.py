from selenium import webdriver

browser = webdriver.Firefox()

def login(admin_username, password, url):
    browser.get(url)
    username_field = browser.find_element_by_id('adminlogin')
    username_field.send_keys(admin_username)

    password_field = browser.find_element_by_id('adminpass')
    password_field.send_keys(password)

    login_button = browser.find_element_by_css_selector('.primary')
    login_button.click()

    