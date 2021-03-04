from API import app
from Services import InvoiceNinja, nextcloud

@app.route('/index')
def index():
    return('Index')

@app.route('/InvoiceNinja/install')
def InvoiceNinjaInstall():
    InvoiceNinja.install()
    print('Invoice Ninja installed')
    return('Invoice Ninja installed')

#This cannot be included yet, as I have no way to process the arguments

@app.route('/InvoiceNinja/setup')
def InvoiceNinjaSetup():
    InvoiceNinja.setup('first_name', 'surname', 'password', 'in.localhost:8081', 'test@email.com')
    print('Invoice Ninja setup complete')
    return('Invoice Ninja setup complete')

@app.route('/Nextcloud/install')
def nextcloudInstall():
    nextcloud.install()
    print('Nextcloud installed')
    return('Nextcloud installed')

@app.route('/Nextcloud/setup')
def nextcloudSetup():
    nextcloud.setup('admin', 'P@$$word', 'localhost:8080')
    print('Nextcloud setup complete')
    return('Nextcloud setup complete')