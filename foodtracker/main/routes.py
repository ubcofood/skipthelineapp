from flask import Blueprint,render_template 

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

@main.route('/logincustomer')
def logincustomer():
    return render_template('login_customer.html')

@main.route('/loginvendor')
def loginvendor():
    return render_template('login_vendor.html')

@main.route('/loginadmin')
def loginadmin():
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

