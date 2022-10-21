# Skipthelineapp 

## Introduction

Skipthelineapp is an online food ordering system website serving UBC students across different vendors in the UNC building. The web application provides services for vendors, staff and customers (students) on campus. This application is a food ordering system with three interfaces i.e. vendor, admin and customer. Users can access the system with their unique credentials pre-registered on the website, and the login page has a selection menu that allows users to log in with the corresponding portal.

The web application allows customers to pay, order and collect food products without the need for them to physically wait in line. The food menus are presented in a card layout, allowing the customer to easily add items to their cart by tapping the add button. Each food product view includes product image, food description, price and allergen tags. The customer has either the option to pay with their UBC account via the flex dollar program or with their own credit/debit cards. Customers can order multiple items in a single order, and each order can be customizable which allows them to edit their dietary preferences. 

The program also has the vendor's portal allowing them to view current orders on display, including a detailed view of each customer's order associated with their order number. The vendors can view their daily transactions and revenue in the analytics tab, and export their sales data in pdf/table format. Vendors can also update their menus and product description, as well as manage employees and their roles.

The Admin portal provides access for new vendors to register and edit their profiles, it also has the functionality to remove a current vendor. The Admin Analytic tab provides a summary of all vendors and their performance, such as their daily transaction rate, monthly revenue rate and customer distribution. Each vendor has the option to disclose their sale data or otherwise, and only those data with the vendor's permission can only send to the admin's portal.

### Classes descriptions and functionalities:

Each user can interact with the system to perform an activity.

The login page has three navigation tabs allowing different types of user to log in accordingly.

The options avaliable to the Admin are edit vendor list, update vendor logo, edit vendor's details, create vendor's account,add/remove vendors, export vendor data and view vendor analytics.

The options available to the Vendor are add food category, add food details, add food allergens, edit food descriptions, view order number, view order descriptions, update food order, edit menus, upload product picture, view revenue, view analytics and delete order.

The options available to the Customer are view menu, sign up and log in, create an order, add item into cart, checkout and view order details and status.

### Language used:

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

## How to run the program?
1. Before running the program, install the python and flask enviroment, make sure they are updated to the latest version. The python interpreter version cannot be earlier than 3.11. To install flask and their python dependencies, checkout https://flask.palletsprojects.com/en/2.2.x/installation/.

1. Download the project files from the repository, open the project folder in your code editor/IDE.
2. In terminal, type the following commands to preconfigure the enviroment 
```
 #start envirnoment
 env\scripts\activate.bat

 #add packages
 pip install flask
 pip install flask-sqlalchemy
 pip install python-dotenv
 ```
3. Run the program with the `flask run` command in the terminal, and access the web application through http://127.0.0.1:5000/ in your browser.
