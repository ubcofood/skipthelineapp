from flask import *
import pyrebase

config = {
   "apiKey" : "AIzaSyA4av3lN5gUTSXLSMuBQeigqOZuQiz5fjo",
    "authDomain": "pythontrial-151b6.firebaseapp.com",
    "databaseURL": "https://pythontrial-151b6-default-rtdb.firebaseio.com",
    "projectId": "pythontrial-151b6",
    "storageBucket": "pythontrial-151b6.appspot.com",
    "messagingSenderId": "749934275221",
    "appId": "1:749934275221:web:ff9e8d5201675414ff499c"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

storage = firebase.storage()

db = firebase.database()

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/view')
def view():
    return render_template('view.html')

@main.route('/login') 
def login():
    return render_template('login.html')

@main.route('/logincustomer', methods=['GET', 'POST']) #firebase
def logincustomer():
    unsuccessful = 'Login failed, email or password is incorrect!'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('index.html', s=successful)
        except:
            return render_template('login_customer.html', us=unsuccessful)
    return render_template('login_customer.html')

@main.route('/loginvendor', methods=['GET', 'POST']) #firebase
def loginvendor():
    unsuccessful = 'Login failed, email or password is incorrect!'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('orderlist.html', s=successful)
        except:
            return render_template('login_vendor.html', us=unsuccessful)

    return render_template('login_vendor.html')

@main.route('/loginadmin', methods=['GET', 'POST']) #firebase
def loginadmin():
    unsuccessful = 'Login failed, email or password is incorrect!'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('adminView.html', s=successful)
        except:
            return render_template('login_admin.html', us=unsuccessful)

    return render_template('login_admin.html')

@main.route('/adminview')
def adminview():
    return render_template('adminView.html')

@main.route('/adminanalytics')
def adminanalytics():
    return render_template('adminAnalytics.html')
@main.route('/adminviewdeleted')
def adminviewdeleted():
    return render_template('adminViewDeleted.html')    

@main.route('/cart')
def cart():
    return render_template('cart.html')
    
@main.route('/checkout_cwl')
def checkout_cwl():
    return render_template('checkout_cwl.html')
    
@main.route('/checkout_card')
def checkout_card():
    return render_template('checkout_card.html')    

@main.route('/bill')
def bill():
    return render_template('bill.html')

@main.route('/orderlist')
def orderlist():
    return render_template('orderlist.html')

@main.route('/vendor_menu')
def vendor_menu():
    return render_template('vendor_menu.html')

@main.route('/vendor_analytics')
def vendor_analytics():
    return render_template('vendor_analytics.html')

@main.route('/vendorEmployee')
def vendorEmployee():
    return render_template('vendorEmployee.html')
