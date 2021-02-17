from selenium import webdriver
import subprocess
import dotenv

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
    subprocess.call("sudo docker-compose -f service_installs/invoice_ninja/Dockerfiles/docker-compose.yml up", shell=True)