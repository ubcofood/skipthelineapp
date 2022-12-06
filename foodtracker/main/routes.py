from flask import *
import googletrans 
from googletrans import Translator
import pyrebase
import spoonacular as sp
import random
import requests
import json


config = {
   "apiKey" : "AIzaSyA4av3lN5gUTSXLSMuBQeigqOZuQiz5fjo",
    "authDomain": "pythontrial-151b6.firebaseapp.com",
    "databaseURL": "https://pythontrial-151b6-default-rtdb.firebaseio.com",
    "projectId": "pythontrial-151b6",
    "storageBucket": "pythontrial-151b6.appspot.com",
    "messagingSenderId": "749934275221",
    "appId": "1:749934275221:web:ff9e8d5201675414ff499c"
}
api = sp.API('c4e983e132c1412a9ab494902242598c')

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

storage = firebase.storage()

db = firebase.database()

main = Blueprint('main',__name__)

def call_API(foodName, apiKey):
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?query={foodName}&dataType=Branded&pageSize=25&pageNumber=2&sortBy=dataType.keyword&sortOrder=asc&brandOwner=Kar%20Nut%20Products%20Company&api_key=gjfigRBqjrJISugOEoF7O9E45ilS2jEUK4He5gjY'
    r = requests.get(url)
    print(r.status_code)  # 200
    
    ret = r.json()

    items= []
    for i in ret['foods']:

        lala = i['brandName']+" "
        lala+=i['brandOwner']+" "
        if('subbrandName' in i):
            lala+=i['subbrandName']+" "
         
        if(len(i['foodNutrients'])>0):
            lala+=str(i['foodNutrients'][0]['value'])+ "g protein"
        items.append(lala)

    # for i in (1,50):
    #     print(ret[i]['description'])
    #     print(ret[i]['brandOwner'])
    #     print(ret[i]['foodNutrients'][0]['amount']) #protein
    #     print(ret[i]['foodNutrients'][1]['amount']) #fat
    #     print(ret[i]['foodNutrients'][2]['amount']) #carbs
    #     print(ret[i]['foodNutrients'][4]['amount']) #kcal
    print(type(ret['foods']))
    print(len(ret['foods']))

    return items


@main.route('/', methods=['GET', 'POST']) #firebase
def index():
    uid='testcustomer'
    if request.method == 'POST' and request.form['submit'] == 'tuna':
        foodinfo = db.child("food").get().val()
        for val in foodinfo:
            if db.child("food").child(val).get().val()['foodName']=='Tuna roll':
               db.child("carts").child(uid).push(val)
    elif request.method == 'POST' and request.form['submit'] == 'blt':
        foodinfo = db.child("food").get().val()
        for val in foodinfo:
            if db.child("food").child(val).get().val()['foodName']=='BLT sandwich':
               db.child("carts").child(uid).push(val)
    return render_template('index.html', randtext="lalal")

@main.route('/protein', methods=['GET', 'POST'])
def protein():
    if request.method == 'POST':
        foodname = request.form['searchfood']
        ans = call_API(foodname, "gjfigRBqjrJISugOEoF7O9E45ilS2jEUK4He5gjY")
        return render_template('protein.html',randtext=foodname, listitems= ans)
    return render_template('protein.html')

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/onthebudget')
def budget():
    

    n = random.randint(1, 100)
    response = api.get_recipe_information(n)
    data = response.json()
    ings="Ingredients: \n"
    instructions ="Instructions: \n"

    if data['extendedIngredients']!=None:
        for ing in data['extendedIngredients']:
            ings+=ing['original']+"\n"

    if data['instructions']!=None:
        instructions+=data['instructions'].replace(".", "\n")

    return render_template('onthebudget.html', title =data['title'], link =data['image'],servings="Servings: "+str(data['servings']),preptime="Ready in "+str(data['readyInMinutes'])+" minutes", ingredients = ings, instructions=instructions)

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
            return redirect(url_for('main.index'))
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
            return redirect(url_for('main.orderlist'))
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
            return redirect(url_for('main.adminview'))
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
