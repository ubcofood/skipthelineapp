# Skipthelineapp 

## Updated features in Assignment 3

- Export menu pdf in Vendor Menu page with pdfkit library integration
   - Note that this feature requires installation of both pdfkit and wkhtmltopdf packages before running the program, which can be done by running these commands:
   ```
   pip install pdfkit
   brew install wkhtmltopdf // Mac with homebrew installed
   ```
   - For windows, download the wkhtmltopdf program on http://wkhtmltopdf.googlecode.com/files/wkhtmltox-0.11.0_rc1-installer.exe and follow the instructions.
   
- Time display on Vendor order page using pytime library
- Time display on checkout pages with UBC ID and Credit/Debit Cards
- Export analytic pdf in Vendor/Admin Analytic page with pdfkit library integration
- Vendor Page UI fixes

- Firebase Integration



## Description

Skipthelineapp is an online food ordering system website serving UBC students across different vendors in the UNC building. The web application provides services for vendors, staff and customers (students) on campus. This application is a food ordering system with three interfaces i.e. vendor, admin and customer. Users can access the system with their unique credentials pre-registered on the website, and the login page has a selection menu that allows users to log in with the corresponding portal.

The web application allows customers to pay, order and collect food products without the need for them to physically wait in line. The food menus are presented in a card layout, allowing the customer to easily add items to their cart by tapping the add button. Each food product view includes product image, food description, price and allergen tags. The customer has either the option to pay with their UBC account via the flex dollar program or with their own credit/debit cards. Customers can order multiple items in a single order, and each order can be customizable which allows them to edit their dietary preferences. 

The program also has the vendor's portal allowing them to view current orders on display, including a detailed view of each customer's order associated with their order number. The vendors can view their daily transactions and revenue in the analytics tab, and export their sales data in pdf/table format. Vendors can also update their menus and product description, as well as manage employees and their roles.

The Admin portal provides access for new vendors to register and edit their profiles, it also has the functionality to remove a current vendor. The Admin Analytic tab provides a summary of all vendors and their performance, such as their daily transaction rate, monthly revenue rate and customer distribution. Each vendor has the option to disclose their sale data or otherwise, and only those data with the vendor's permission can only send to the admin's portal.

### Classes descriptions and functionalities:

Each user can interact with the system to perform an activity.

The login page has three navigation tabs allowing different types of users to log in accordingly.

The options available to the Admin are edit vendor list, update vendor logo, edit vendor's details, create vendor's account,add/remove vendors, export vendor data and view vendor analytics.

The options available to the Vendor are add food category, add food details, add food allergens, edit food descriptions, view order number, view order descriptions, update food order, edit menus, upload product picture, view revenue, view analytics and delete order.

The options available to the Customer are view menu, sign up and log in, create an order, add item into cart, checkout and view order details and status.

### Languages used:

Python/Flask Web Framework; HTML/CSS/JavaScript

### Breakdown of the code structure:

1. `/.idea` - project configuration files

1. `/env` - enviroment folder 
   - `/Lib/site-packages` Python packages
   - `/Scripts/` Python enviroments
   
1. `/foodtracker` - project folder
   - `/__pycache__` python cache
   - `/main` main folder
      - routes.py - html routes, create classes here before adding any new pages
   - `/static` - html resources
      - `/css` CSS folder, add css styles here
      - `/fonts` Fonts folder, add new font here
      - `/js` Javascripts foder, add new script here
   - `/template` - html files resource, where individual html page get stored
   
         -  `add.html` add new item 
         -  `adminAnalytics.html` Admin Analytics
         -  `adminView.html` Admin View
         -  `bill.html` Billing View
         -  `cart.html` Cart View
         -  `index.html` Customer View
         -  `login.html` Login Naviagtion View
         -  `login_admin.html` Admin Login View
         -  `login_customer.html` Customer Login View
         -  `login_vendor.html` Vendor Login View
         -  `view.html` Description View  
   -`models.py`- contains user model classes, add new classes here
   -`extensions.py`- flask_sqlalchemy extensions
 1. `README.md`- readme file  

### Methods and classes

- Customer Class: 
```
   - attributes: 
      - customer.cid --> customer id
      - customer.cname --> customer name
      - customer.cemail --> customer email
      - customer.cpassword --> customer password
      - customer.cphone --> customer phone number
```
   
- Admin Class: 
```
   - attributes:
      - admin.amail --> admin email
      - admin.apassword --> admin password   
```
- Vendor Class: 
```
   - attributes: 
      - vendor.vid --> vendor id
      - vendor.vname --> vendor name
      - vendor.vemail --> vendor email
      - vendor.vphone --> vendor phone number
```
- Item Class: 
```
   - attributes: 
      - items.iid --> item id
      - items.iname --> item name
      - items.idescription --> item description
      - items.iprice --> item price
      - items.vid --> vendor id
```      
     
- Order Class: 
```
   - attributes: 
      - order.ohash --> order hash id
      - order.vid --> vendor id
      - order.cid --> customer id
      - order.odate --> order date
      - order.ostatus --> order status
      - order.oprice --> order price  
```      

- Methods
```
   - index() --> show main page
   - indexmenu() --> show customer menu page
   - register() --> register account
   - login() --> login account
   - loginNext() --> resolve login issue when no user found or password incorrect
   - userorders() --> display user's order
   - showuserprofile() --> show user's profile
   - updateuserprofile() --> update user's profile
   - updateuserprofileNext() --> resolve error when user's input does not matches format
   - logout() --> user sign out
   - vendormenu() --> display menu for a vendor
   - vendorlogin() ---> log vendor in
   - vendorloginNext() --> resolve login issue when no vendor found or password incorrect
   - vendorhome() --> display vendor main page
   - vendorviewanalytics() --> display vendor analytics
   - acceptorreject() --> option for vendor to accept/reject order
   - restacceptedorders() --> complete order when vendor accept one
   - showmyrestmenu() --> display current vendor menu
   - additem() --> add an food item
   - additemNext() --> resolve issue when misinput an item description
   - updateitem() --> update a particular item
   - updateitemNext() --> resolve issue when misinput an item description during updating
   - deleteitem() --> delete an item
   - deleteitemNext() --> resolve issue when misinput an item description during deletion
   - showvendprofile() --> display vendor profile
   - updatevendprofile() --> update vendor profile
   - updatevendprofileNext() --> resolve issue when misinput vendor description during editing
   - vendlogout() --> vendor log out
   - payment() --> display payment menu
   - submitorder() --> submit user order
   - adminlogin() --> display admin login page 
   - adminloginNext() --> resolve error when admin misinput fields
   - vendregisterbyadmin() --> admin register a vendor
   - adminshowvendor() --> display all vendors
   - adminvendmenu() --> display menu from a vendor
   - adminlogout() --> admin logout
   - adminviewanalytics() --> display admin analytics
   - exportanalytics() --> export analytics
```
## How to run the program?
1. Before running the program, install the python and flask environments and make sure they are updated to the latest version. The python interpreter version cannot be earlier than 3.11. To install flask and its python dependencies, check out https://flask.palletsprojects.com/en/2.2.x/installation/.

1. Download the project files from the repository, open the project folder in your code editor/IDE.
2. In terminal, type the following commands to preconfigure the environment 
```
 #start environment
 env\scripts\activate.bat

 #add packages
 pip install flask
 pip install flask-sqlalchemy
 pip install python-dotenv
 ```
3. Run the program with the `flask run` command in the terminal, and access the web application through http://127.0.0.1:5000/ in your browser.
