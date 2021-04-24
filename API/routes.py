from API import app
from flask import render_template, request, redirect
from Services import InvoiceNinja, nextcloud
import urllib

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



business = {'name': 'P O\'Kane Plastering and Tiling'} #get from config
# The arrays below are placeholder sata. In the finished project they will be read in from a database
jobs = [
    {
        'id':0,
        'customerID':2,
        'address':"address",
        'price':{
            'labour':300.00,
            'materials':300.00,
            'overheads':300.00
            },
        'quote':{
            'labour':300.00,
            'materials':300.00,
            'overheads':300.00
            },
        'date':{'quote':'2020-01-01','start':'2020-01-02','end':'2020-01-03'},
        'status':'Complete',
        'quoteDescription':'"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'
        
    }
]

customers=[{
        'firstname':'John',
        'lastname':'smith',
        'phone':'07500123123',
        'id':0
        },
           {
        'firstname':'John12',
        'lastname':'smith',
        'phone':'07500123123',
        'id':1
        },
           {
        'firstname':'John123',
        'lastname':'smith',
        'phone':'07500123123',
        'id':2
        },
           {
        'firstname':'John124',
        'lastname':'smith',
        'phone':'07500123123',
        'id':3
        },
           {
        'firstname':'John125',
        'lastname':'smith',
        'phone':'07500123123',
        'id':4
        }]

services=[{
    'name':'Nextcloud',
    'url':'http:localhost:8080',
    'description':'Dropbox equivalent',
    'port':8080,
    'status':'running',
    'id':0
    },{
    'name':'Invoice Ninja',
    'url':'http:localhost:8081',
    'description':'Finances',
    'port':8081,
    'status':'off',
    'id':1
}]


@app.route('/form', methods=['GET','POST'])
def form():
    print(request)
    if request.method== 'POST':
        print(request.form)

    return redirect(request.referrer)


@app.route('/')
@app.route('/jobs')
def jobView():
    return render_template('index.html', title='Home', business=business, jobs=jobs, customers=customers)


@app.route('/jobs/<jobID>')
def jobDetailView(jobID):
   
    job=jobs[int(jobID)]
    return render_template('jobDetails.html', business=business, job=job, customer=customers[job['customerID']])

@app.route('/customers/<customerID>')
def customerDetailView(customerID):
    return render_template('customerDetail.html', business=business, jobs=jobs, customer=customers[int(customerID)])

@app.route('/customers')
def customerView():
    return render_template('customers.html', business=business, jobs=jobs, customers=customers)

@app.route('/services')
def serviceView():
    for service in services:
        service['status']=serviceStatus(int(service['id']))
    return render_template('services.html', services=services, business=business)
            

@app.route('/services/<serviceID>')
def serviceDetailView(serviceID):
    service=services[int(serviceID)]
    service['status']=serviceStatus(int(serviceID))
    print(service['status'])
    return render_template('serviceDetail.html', service=service, business=business)


def serviceStatus(serviceID):
    url="http://localhost:" + str(services[serviceID]['port'])
    try:
        statusCode = urllib.request.urlopen(url).getcode()
        if statusCode == 200:
            statusCode = 'Running'
    except:
        statusCode='Error'

    return statusCode