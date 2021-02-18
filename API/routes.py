from API import app
from Services import InvoiceNinja, nextcloud

@app.route('/index')
def index():
    return('Index')

@app.route('/invoiceNinja/Install')
def InvoiceNinjaInstall():
    InvoiceNinja.install()
    print('Invoice Ninja installed')
    return('Invoice Ninja installed')
