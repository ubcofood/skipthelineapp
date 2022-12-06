# Skipthelineapp 

## Updated features in Individual Project 📝


### Added "On the budget?" and "Protein" pages on Customer side of the website - Andela

-"On the budget?" page - **Spoonacular API**
 -To use Spoonacular API, we need to install it:
   ```
   pip install spoonacular
   ```
  - After that, we need to import it in the code and get our unique API KEY from https://spoonacular.com/food-api
   ```
  import spoonacular as sp
   ```
  - This page allows the customer to generate a random recipe on the click of "Get another recipe" button. The page will list the title of the recipe, number of servings, preparation time, ingridents and instructions for preparations alongside the image of the dish.
 
  ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/onthebudget.png?raw=true)
  
-"Protein" page - **USDA FoodData Central API**
 - To use this API we need a couple of supporting libraries to be imported at the start of the file:
   ```
   import requests
   import json
   ```
  - We also need to have our unique API key from https://fdc.nal.usda.gov/api-guide.html
  - This page highlights the importance of protein intake in one's diet and allows the customer to get information about protein content of any item they type into the search bar. Text typed into searchbar is then passed to USDA FoodData Central API, and a list of names of foods in that category is displayed alongside the protein content in grams. When typing into search bar again, customer can get data about protein content of another item.
 
![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/protein.png?raw=true)
 

### Paypal Integration and Admin Troubleshoot Page - Nick

- Added Paypal checkout integration on the Cart page, allowing current payment to send directly to merchant's account.
  - Customer can have the option to pay using paypal credit alongside with their credit/debit card. 
  - On the cart page, there are two buttons for payments. Clicking the pay with paypal button will direct user to the paypal authentication page. Once the transaction is completed, the page will direct user to the bill page.
  
  <img width="306" alt="Screenshot 2022-12-04 at 1 09 43 AM" src="https://user-images.githubusercontent.com/88886207/205482762-14a2b195-18de-4c79-aa0f-131dafcc507b.png">
  
- Added Troubleshoot Chat page under the admin portal, allowing admin manager to get help remotely by chatting with us.
  - Admin now has the ability to contact us to troubleshoot technical issues.
  - The admin help page comprises a conversation view and a message toolbar. Admins can click our profile and directly chat with us through weavy. The conversation will not disappear if user clicked other pages after.
  
  <img width="937" alt="Screenshot 2022-12-04 at 1 11 49 AM" src="https://user-images.githubusercontent.com/88886207/205482909-86140506-e75b-47e0-8675-4c080abc8d14.png">
  
   #### API used:


   - Weavy Chat API using JavaScript Library
   - Paypal payment REST API


### Text and phone call confirmations of the Order - Anirudh

- Added text message verification on chechout using the Vonage SMS API
  - Customers will recieve a text messagestating their order number and verifiying that it has been confirmed.
  - On pressing the checkout button, the customer will shortly recieve a text message confirming their order.

 <img width="180" alt="Screenshot 2022-12-04 at 1 09 43 AM" src="https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/63728.jpg">

- Added Phone call verification on chechout using the Twilio Voice API
  - Customers will recieve a phone call stating their order number and verifiying that it has been confirmed.
  - On pressing the checkout button, the customer will shortly recieve a phone call confirming their order.

   #### API used:

   - Vonage SMS API
   - Twilio Voice API

## Updated features in Assignment 3 📝

- Export menu pdf in Vendor Menu page with **pdfkit library** integration
   - Enables vendors to export their menus for promotional purposes
   - Note that this feature requires installation of both pdfkit and wkhtmltopdf packages before running the program, which can be done by running these commands:
   
   ```
   pip install pdfkit
   brew install wkhtmltopdf // Mac with homebrew installed
   ```
   - For windows, download the wkhtmltopdf program on http://wkhtmltopdf.googlecode.com/files/wkhtmltox-0.11.0_rc1-installer.exe and follow the instructions.
  
   - Sample Outputs:
      - See `analytic.pdf` file in the `sampleoutputs` folder
   
- Time display on Vendor order page using **pytime library**
  - Allow vendor to view the current time and order times from customers which helps them to prioritize orders based on their time.
  
  - Sample Outputs:
      ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/Screenshot%202022-11-14%20at%202.15.42%20PM.png?raw=true)
      
- Time display on checkout pages with UBC ID and Credit/Debit Cards
  - Allow customer to view the current time of ordering and the deadline for user to complete transaction before order gets expired.
  
  - Sample Outputs:
      ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/Screenshot%202022-11-14%20at%202.18.07%20PM.png?raw=true)
  
- Export analytic pdf in Vendor/Admin Analytic page with pdfkit library integration
  - Allow Vendor/Admin to download and export their sales data to print and organize right under the page.
  
  - Sample Outputs:
      ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/Screenshot%202022-11-14%20at%202.16.21%20PM.png?raw=true)
 
- Integrated scripts that allows the order panel to refresh page every ten seconds
  - Allow vendors to see new orders without the need of manually refresh the page, and the system will automatic show new order once customer has placed one.
  - Sample Outputs:
      - See video for sample outputs
      
- Vendor Page UI fixes
  - Improved design and layouts, used custom titles and different icon to help user differentiate the pages.
  - Cancel button on the checkout page allows user to cancel order immediately
  - Sample Outputs:
  
      ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/Screenshot%202022-11-14%20at%202.15.54%20PM.png?raw=true)
      
  
- Firebase Integration - **Pyrebase library**
  - Allow user to login to the system with pre-registered accounts, firebase allows quick configuration that enable us to register accounts through the portal and manage their data. In Firebase, we store all the information and images needed to run this application. 
  - To install needed libraries run:
   ```
   pip install pyrebase
   ```
  - Sample Outputs:
      - Registered accounts in Firebase
       ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/firebaseauth.png?raw=true)
      - Storage of media files in Firebase
       ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/firebasestorage.png?raw=true)
      - Firebase NoSQL database (example showing how food items are stored with unique keys)
       ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/firebasedb.png?raw=true)
  
- Email receipts - **ssl and smtp libraries** (come preinstalled with python)
  - When an order is completed, the system will generate an email receipt that sends to user's email they registrated with. This allow user to view their email receipts without having to saving the entire page.
  - Sample Outputs:
       ![alt text](https://github.com/ubcofood/skipthelineapp/blob/main/sampleoutputs/emailreceipt.png?raw=true)



## Description 📄

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

### Languages used 🧑‍💻

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
## How to run the program 💻 ?
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
