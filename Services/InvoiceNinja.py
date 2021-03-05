from selenium import webdriver
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#def login(admin_username, password, url):
    

def install():
    #Download the dockerfile
    subprocess.call("git clone https://github.com/invoiceninja/dockerfiles.git ./service_installs/invoice_ninja/Dockerfiles", shell=True)
    #generate key
    subprocess.call("sudo docker run --rm -it invoiceninja/invoiceninja php artisan key:generate --show >./service_installs/invoice_ninja/app_key.txt", shell=True)
    with open ("./service_installs/invoice_ninja/app_key.txt", "r") as key_file:
        contents=key_file.read()
        key = contents[contents.index("base64"):contents.index("base64")+51]
    print(key)

    #open env file and save as variable
    with open('./service_installs/invoice_ninja/Dockerfiles/env','r') as file:
        env = file.readlines()

    # change the app_key
    env[1] = f'APP_KEY={key}\n'
    # and write everything back
    with open('./service_installs/invoice_ninja/Dockerfiles/env', 'w') as file:
        file.writelines( env )

    

    #open docker-compose file and save as variable
    with open('./service_installs/invoice_ninja/Dockerfiles/docker-compose.yml','r') as file:
        dcompose = file.readlines()

    # change the port
    dcompose[18] = '      - "8081:80"\n'
    # and write everything back
    with open('./service_installs/invoice_ninja/Dockerfiles/docker-compose.yml', 'w') as file:
        file.writelines( dcompose )

    #run it
    subprocess.call('sudo chown -R 1500:1500 service_installs/invoice_ninja/Dockerfiles/docker/app', shell=True)
    subprocess.call("sudo docker-compose -f service_installs/invoice_ninja/Dockerfiles/docker-compose.yml up -d", shell=True)

def setup(first_name, surname, password, url, email):
    browser = webdriver.Firefox()
    browser.get(url + '/setup')

    #Clear cookie form
    browser.find_element_by_xpath('/html/body/div[1]/div/a').click()


    #put url in field
    url_field = browser.find_element_by_name('url')
    url_field.clear()
    url_field.send_keys('http://' +url)

    #click https to disable it
    browser.find_element_by_name('https').click()
    #Submit PDF test
    browser.find_element_by_id('test-pdf').click()
    
    
    
    #wait for db section to load
    WebDriverWait(browser, 1000).until(
        EC.element_to_be_clickable((By.NAME, "db_host"))
    )
    #switch back to main tab, out of pdf
    browser.switch_to.window(browser.window_handles[0])
    
    
    #change DB_host
    db_host_field = browser.find_element_by_name("db_host")
    db_host_field.clear()
    db_host_field.send_keys('db')
    
    #change db
    db_host_field = browser.find_element_by_name('db_database')
    db_host_field.clear()
    db_host_field.send_keys('ninja')

    #manually scroll down to prevent cookie div from covering button
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Submit db test
    browser.find_element_by_id('test-db-connection').click()

    WebDriverWait(browser, 1000).until(
        EC.element_to_be_clickable((By.ID, "test-smtp-connection"))
    )
    #manually scroll down to prevent cookie div from covering button
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Submit email test
    browser.find_element_by_id('test-smtp-connection').click()
    WebDriverWait(browser, 1000).until(
        EC.element_to_be_clickable((By.NAME, "first_name"))
    )

    #manually scroll down to prevent cookie div from covering button
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #fill in user details
    browser.find_element_by_name("first_name").send_keys(first_name)
    browser.find_element_by_name("last_name").send_keys(surname)
    browser.find_element_by_name("email").send_keys(email)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_name('terms_of_service').click()
    browser.find_element_by_name('privacy_policy').click()
    #Submit email test
    #browser.find_element_by_id('test-smtp-connection').click()